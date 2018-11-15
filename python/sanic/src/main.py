import os

from sanic import Sanic, response
from sanic.exceptions import SanicException


app = Sanic(__name__)


@app.route('/')
async def test(request):
    return response.json({'hello': 'world'})


@app.exception(SanicException)
async def sanic_exception_handler(request, exception):
    return response.json({
        'error': {
            'exception': getattr(exception, 'message', None) or str(exception),
            'status_code': getattr(exception, 'status_code', None),
        }
    })


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=9000,
        workers=os.cpu_count(),
    )
