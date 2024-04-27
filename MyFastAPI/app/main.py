from fastapi import FastAPI
from azure.functions import AsgiMiddleware

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Azure Functions와 호환되도록 FastAPI 앱을 AsgiMiddleware로 감싸줍니다.
