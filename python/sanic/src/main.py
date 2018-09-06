import os

from sanic import Sanic, response


app = Sanic(__name__)


@app.route('/')
async def test(request):
    return response.json({'hello': 'world'})


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=9000,
        workers=len(os.sched_getaffinity(0)),
    )
