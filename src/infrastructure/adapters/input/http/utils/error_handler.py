from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import NoResultFound # refactor required
from starlette.middleware.base import BaseHTTPMiddleware

from src.domain.utils.exceptions import NotFound


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            if isinstance(e, ValueError):
                return JSONResponse(status_code=400, content={'error': "ValueError: {}".format(e)})
            elif isinstance(e, AttributeError):
                return JSONResponse(status_code=400, content={'error': "AttributeError: {}".format(e)})
            elif isinstance(e, KeyError):
                return JSONResponse(status_code=400, content={'error': "KeyError: {}".format(e)})
            elif isinstance(e, TypeError):
                return JSONResponse(status_code=400, content={'error': "TypeError: {}".format(e)})
            elif isinstance(e, NotFound):
                return JSONResponse(status_code=404, content={'error': "NotFound: {}".format(e)})
            elif isinstance(e, NoResultFound):
                return JSONResponse(status_code=404, content={'error': "NoResultFound: {}".format(e)})
            else:
                return JSONResponse(status_code=500, content={'error': "InternalServerError: {}".format(e)})
