import datetime
import json
import logging

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response, StreamingResponse
from starlette.types import ASGIApp

logger = logging.getLogger(__name__)

logging.basicConfig()
logging.root.setLevel(logging.INFO)

logging.basicConfig(level=logging.INFO)

STATUS_MESSAGES = {
    200: 'Status OK',
    201: 'Created',
    202: 'Updated',
    204: 'Deleted',
    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Request Entity Too Large',
    414: 'Request Uri Too Long',
    415: 'Unsupported Media Type',
    416: 'Requested Range Not Satisfiable',
    417: 'Expectation Failed',
    422: 'Unprocessable Entity',
    423: 'Locked',
    424: 'Failed Dependency',
    428: 'Precondition Required',
    429: 'Too Many Requests',
    431: 'Request Header Fields Too Large',
    451: 'Unavailable For Legal Reasons',
    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'Http Version Not Supported',
    507: 'Insufficient Storage',
    511: 'Network Authentication Required'
}


class Renderer(BaseHTTPMiddleware):
    def __init__(
            self,
            app: ASGIApp,
            dispatch=None,
    ):
        super().__init__(app, dispatch)

    async def read_bytes(self, generator):
        body = b""
        async for data in generator:
            body += data
        return body

    async def resolve_response(self, streaming: StreamingResponse) -> Response:
        content = await self.read_bytes(streaming.body_iterator)
        content_data = json.loads(content)
        resp_data = {'success': streaming.status_code // 100 not in (4, 5)}
        if resp_data['success']:
            if content_data.get('message'):
                resp_data['message'] = content_data.get('message')
            else:
                resp_data['message'] = STATUS_MESSAGES[streaming.status_code]

            if content_data.get('data'):
                resp_data['data'] = content_data.get('data')

        else:
            resp_data['message'] = STATUS_MESSAGES[streaming.status_code]

        status_code = streaming.status_code
        response = json.dumps(resp_data).encode()
        logger.info(f'{response} {datetime.datetime.now()}')
        return Response(response, status_code)

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        return await self.resolve_response(response)
