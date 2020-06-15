from fastapi import FastAPI

from proto_files.structures_pb2 import SampleRequest
from grpc_client import stub

app = FastAPI()

@app.get("/")
def index():
    print(stub.SampleMethod(SampleRequest(id="some id")))
    return {"Some Key": "Some Value"}