from views import index
import pathlib


PROJECT_ROOT=pathlib.Path(__file__).parent

def setup_routes(app):
    app.router.add_get('/',index)
    setup_static(app)


def setup_static(app):
    app.router.add_static('/static/',path=PROJECT_ROOT/'static',name='static')
