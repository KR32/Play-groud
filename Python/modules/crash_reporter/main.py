from sqlalchemy.sql import base
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.api.api_v1.api import api_router
from app.api.api_v1.sub_api import sub_api_router
from app.core import config
from app.crash_reporter import get_crash_report
from app.db.session import Session
from app.crud.user.user import get
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.encoders import jsonable_encoder

import os
import sys
import logging
import traceback

logger = logging.getLogger(__name__)
app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/v1/openapi.json")

"""
Removed "openapi_prefix" from the application.
https://fastapi.tiangolo.com/advanced/behind-a-proxy/?h=root_path#about-root_path
"""
tfapp = FastAPI(title=config.PROJECT_NAME)
subapp = FastAPI(title=config.PROJECT_NAME)

# gzip conmpression middleware
tfapp.add_middleware(GZipMiddleware, minimum_size=1000)

# CORS
origins = []

# Set all CORS enabled origins
if config.BACKEND_CORS_ORIGINS:
    origins_raw = config.BACKEND_CORS_ORIGINS.split(",")
    for origin in origins_raw:
        use_origin = origin.strip()
        origins.append(use_origin)
    tfapp.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),
    subapp.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),

tfapp.include_router(api_router, prefix="/v1")
subapp.include_router(sub_api_router)

app.mount("/api", tfapp)
app.mount("/subapi", subapp)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    _schema = "public"
    # setting search_path to public schema only if current stack is 
    # running as demo server.
    if config.SERVER_TYPE == "DEMO":
        logger.debug(f"_schema: {_schema}")
        request.state.db.execute(f"SET search_path TO {_schema}")
    # endif
    response = await call_next(request)
    request.state.db.close()
    return response


@tfapp.exception_handler(Exception)
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
