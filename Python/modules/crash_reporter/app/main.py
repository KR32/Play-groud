import os
import sys
import logging
import traceback
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response
from fastapi.middleware.gzip import GZipMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.crash_reporter import get_crash_report
import config

logger = logging.getLogger(__name__)
app = FastAPI(title="API Crash Reporter", openapi_url="/api/v1/openapi.json")

# gzip conmpression middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

@app.get('/')
def sample_endpoint(request: Request):
    data = {"message": "Hello World"}
    return data['unknownkey']


@app.exception_handler(Exception)
async def validation_exception_handler(request: Request, exc: Exception):
    error_type, error_message, error_traceback = sys.exc_info()
    # (<class 'KeyError'>, KeyError('none'), <traceback object at 0x7f819c509be0>)
    content = "".join(
        traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
    )
    # triggering crash reporter
    if config.INSTANT_MAIL_REPORT:
        info = get_crash_report(
            error_traceback, content, error_type, error_message, request
        )
    if content:
        logger.error(content)
    raise StarletteHTTPException(status_code=500, detail="Internal Server Error!")
