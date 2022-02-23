import os
import sys
import traceback
import inspect
import logging
from pathlib import Path

import emails
from emails import JinjaTemplate
from starlette.requests import Request
from datetime import datetime, timedelta
from urllib.parse import urlparse

import config
# from urlparse import urlparse  # Python 2

logger = logging.getLogger(__name__)

def get_crash_report(tb, raw_content, error_type, error_message, request:Request=None):
    """
    it Extracts traceback information into a list of dict
    and returns last elemant of list

    tb = traceback object
    raw_content = parsed trackback content
    error_type = error class name
    error_message = message string from exception
    request = starlette.requests.Request 

    """
    try:
        info = []
        data = {}
        tb_level = tb

        # https://docs.python.org/2/library/traceback.html#traceback.extract_tb
        extracted_tb = traceback.extract_tb(tb)  
        # logger.debug('extracted_tb =>')
        # logger.debug(extracted_tb)
        # list of FrameSummary objects 

        for (filepath, line, module, code) in extracted_tb:

            source_code, module_lineno = inspect.getsourcelines(tb_level.tb_frame)
            # logger.debug(inspect.getsourcelines(tb_level.tb_frame))
            # ([
            # "@router.get('/')\n", 
            # 'def execute():\n', 
            # "    dict_={'error':500,'no':1}\n", 
            # "    return dict_['none']\n" -----------------------> ## Creating KeyError ##
            # ], 6)
            base_error_message = f"{request.method}: {request.url}"
            headers = request.scope.get("headers", None)
            headers = [[word.decode("utf8") for word in sets] for sets in headers] if headers else None
            query_params = "{}".format(request.scope.get("query_string", '').decode('utf-8'))
            path_params = "{}".format(request.scope.get("path_params", ''))

            # https://stackoverflow.com/questions/9626535/get-protocol-host-name-from-urls
            parsed_uri = urlparse(str(request.url))
            host_name = "{uri.scheme}://{uri.netloc}/".format(uri=parsed_uri)
            app_name = "{uri.netloc}".format(uri=parsed_uri)

            data = {
                "app": app_name,
                "host": host_name,
                "req_type": f"{request.method}",
                "req_url": f"{request.url}",
                "headers": f"{headers}",
                "error_type": f"{error_type.__name__}",
                "error_message": str(error_message),
                "query_params": f"{query_params}",
                "path_params": f"{path_params}",
                "file": f"{filepath}",
                "error_line_number": line,
                "module": "".join(module),
                "error_line": "".join(code),
                "source_code": source_code,
                "raw_trackback_content":raw_content
                }
                
            # overwritting next tb_level
            tb_level = getattr(tb_level, 'tb_next', None)
            # logger.debug(tb_level)
            info.append(data)

        # last Frame
        report = info[len(info)-1]

        # logger.debug(report)
        if report is not None:
            content = f"""
[{datetime.now()}]\n
From                        => {report['host']}
Type                        => {report['req_type']}
URL                         => {report['req_url']}
Path Params                 => {report['query_params']}
Query Params                => {report['path_params']}
Location                    => {report['file']} at line no {report['error_line_number']}
TraceBack                   => \n{report['raw_trackback_content']}\n{'='*100}\n
"""
            repeated = "not-configured"
            if config.ONCE_A_DAY_MAIL_REPORT:
                # maintaine a log file to send mail at EOD
                repeated = prepare_log_file(content)

            # sending instant mail while occurring error
            if config.INSTANT_MAIL_REPORT:
                # formatting for jinja env
                # format headers
                formatted_headers = str(report['headers']).replace("],","]\n").replace("[[","[").replace("]]","]\n")
                report['headers'] = formatted_headers
                # err line
                err_code = "".join(report["error_line"]).replace(" ","&nbsp;")
                # format source_code
                formatted_source_code = "".join(report["source_code"]).replace('\n', "<br>")
                formatted_source_code = formatted_source_code.replace(" ","&nbsp;")
                formatted_source_code = formatted_source_code.replace(err_code, "<span style='background-color: #dd3651;color: #f7f2f2;'> " + err_code + " </span></strong>")
                report["source_code"] = formatted_source_code

                # # format traceback
                # formatted_raw_content = "".join(report["raw_trackback_content"]).replace("\n", "<p style='margin-bottom:9px'></p>")
                formatted_raw_content = "".join(report["raw_trackback_content"]).replace("\n", "<br>")
                formatted_raw_content = formatted_raw_content.replace(" ","&nbsp;")
                formatted_raw_content = formatted_raw_content.replace(err_code, "<span style='background-color: #dd3651;color: #f7f2f2;'> " + err_code + " </span>")
                report["raw_trackback_content"] = formatted_raw_content
                
                if repeated in [False,"not-configured"]:
                    # send instant mail
                    send_instant_crash_report_mail(data)

            return data
    except Exception as e:
        error_type, error_message, error_traceback = sys.exc_info()
        tb_content="".join(
        traceback.format_exception(
            etype=type(e), value=e, tb=e.__traceback__
        ))
        logger.debug("Crash Reporter Crashed!")
        logger.debug(error_type)
        logger.debug(error_message)
        logger.debug(tb_content)


def check_duplicate_entry(latest,old_file_lines):
    """ Split list into lists by particular value """
    size = len(old_file_lines)
    # Split list into lists by particular value
    # and that value here is "="*100
    idx_list = [idx + 1 for idx, val in
                enumerate(old_file_lines) if val == "="*100]

    res = [old_file_lines[i: j] for i, j in
            zip([0] + idx_list, idx_list +
            ([size] if idx_list[-1] != size else []))]
    
    # Removing [date time] label;Because, Its unique for every log
    for item in res:
        item.pop(0) 
    latest.pop(0)

    if latest in res:
        return True
    else:
        return False
        
    

def prepare_log_file(content)->bool:
    """Insert given list of strings as a new lines at the beginning of a file
        and returns True while error occurres more then once to prevent instant mail
    """
    # define name of original file
    file_name = f"./app/crash_logs/{str(datetime.now().date())}.log"
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    
    existing_logs=[]
    new_log=[y for y in (x.strip() for x in content.splitlines()) if y]
    try:
        # getting crash logs from current file which is formatted as list of strings
        with open(file_name, 'r') as read_obj:
            for line in read_obj:
                # removing  \n suffix , white spaces, empty lines
                line = line.rstrip('\n')
                line = line.strip()
                if line != "":
                    existing_logs.append(line)

        if check_duplicate_entry(new_log,existing_logs):
            # ERROR OCCURRED MORE THEN ONCE!
            logger.error(f"LOG MATCHED : Please check '{file_name}' for more information!")
            return True
        else:
            # open given original file in read mode and dummy file in write mode
            with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
                # Write given line to the dummy file
                write_obj.write(content)
                # Read lines from original file one by one and append them to the dummy file
                for line in read_obj:
                    write_obj.write(line)
            # remove original file
            os.remove(file_name)
            # Rename dummy file as the original file
            os.rename(dummy_file, file_name)
            return False
    except FileNotFoundError as fnfe:
        error_type, error_message, error_traceback = sys.exc_info()
        logger.debug(f'{error_type.__name__}; So, Creating New "{file_name}" to keep this error log')
        # creating new log file 
        with open(file_name, 'a+') as fresh_file:
            fresh_file.write(content)

def send_email(email_to: str, subject_template="", html_template="", environment={}, email_cc=None, email_bcc=None):
    assert config.EMAILS_ENABLED, "no provided configuration for email variables"
    if email_cc:
        email_cc = email_cc.split(',')
    if email_bcc:
        email_bcc = email_bcc.split(',')

    from_name, from_email = (config.EMAIL_FROM_NAME, config.EMAIL_FROM_EMAIL)

    logger.info(f'From Name: {from_name}, From Email: {from_email}')
        
    message = emails.Message(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=(from_name, from_email),
        cc=email_cc,
        bcc=email_bcc
    )
    smtp_options = {"host": config.SMTP_HOST, "port": config.SMTP_PORT}
    if config.SMTP_TLS:
        smtp_options["tls"] = True
    if config.SMTP_USER:
        smtp_options["user"] = config.SMTP_USER
    if config.SMTP_PASSWORD:
        smtp_options["password"] = config.SMTP_PASSWORD
    response = message.send(to=email_to, render=environment, smtp=smtp_options)
    logging.info(f"send email result: {response.__dict__}")

    return response




def send_instant_crash_report_mail(report):
    if config.INSTANT_MAIL_TO:
        mail_to = config.INSTANT_MAIL_TO.split(',')
        subject = f"Internal Server Error - {report['host']}"
        email_template_path = Path(config.EMAIL_TEMPLATES_DIR) / "crash_report.html"
        with open(email_template_path) as f:
            template_str = f.read()
        send_email(
            email_to=mail_to,
            html_template=template_str,
            subject_template=subject,
            environment=report
        )
    else:
        logger.debug("Crash reporter has not configured properly to send emails!; Please specify the recipient(s)")



def send_crash_log_mail(file_name:str):
    if config.ONCE_A_DAY_MAIL_TO:
        mail_to = config.ONCE_A_DAY_MAIL_TO.split(',')
        subject = f"Crash Report for - {datetime.now().date()-timedelta(1)}"
        message = emails.Message(
            subject=JinjaTemplate(subject),
            html=f"<p>crash logs for {str(datetime.now().date()-timedelta(1))}</p>",
            mail_from=('TalentFind System', config.EMAILS_FROM_EMAIL),
            mail_to=mail_to
        )
        message.attach(filename=f"{str(datetime.now().date())}.txt",data=open(file_name,'rb'))
        smtp_options = {"host": config.SMTP_HOST, "port": config.SMTP_PORT}
        if config.SMTP_TLS:
            smtp_options["tls"] = True
        if config.SMTP_USER:
            smtp_options["user"] = config.SMTP_USER
        if config.SMTP_PASSWORD:
            smtp_options["password"] = config.SMTP_PASSWORD
        response = message.send(smtp=smtp_options)
        logging.info(f"send email result: {response.__dict__}")
    else:
        logger.debug("Crash reporter has not configured properly to send emails!; Please specify the recipient(s)")
