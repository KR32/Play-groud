import os
import logging

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

def getenv_boolean(var_name, default_value=False):
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ("TRUE", "1")
    return result


# smpt
SMTP_TLS = getenv_boolean("SMTP_TLS", True)
SMTP_PORT = None
_SMTP_PORT = os.getenv("SMTP_PORT")
if _SMTP_PORT is not None:
    SMTP_PORT = int(_SMTP_PORT)
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# app config
EMAILS_ENABLED=getenv_boolean("EMAILS_ENABLED", True)
EMAIL_TEMPLATES_DIR = os.getenv("EMAIL_TEMPLATES_DIR")
EMAIL_FROM_EMAIL=os.getenv("EMAIL_FROM_EMAIL")
EMAIL_FROM_NAME=os.getenv("EMAIL_FROM_NAME")
INSTANT_MAIL_REPORT=getenv_boolean("INSTANT_MAIL_REPORT")
ONCE_A_DAY_MAIL_REPORT=getenv_boolean("ONCE_A_DAY_MAIL_REPORT")
INSTANT_MAIL_TO=os.getenv("INSTANT_MAIL_TO")
ONCE_A_DAY_MAIL_TO=os.getenv("ONCE_A_DAY_MAIL_TO")