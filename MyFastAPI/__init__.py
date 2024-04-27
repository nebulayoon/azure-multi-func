import azure.functions as func
from fastapi.middleware.wsgi import WSGIMiddleware
from .app.main import app as fastapi_app


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    wsgi_app = WSGIMiddleware(fastapi_app)
    return func.WsgiMiddleware(wsgi_app).handle(req, context)
