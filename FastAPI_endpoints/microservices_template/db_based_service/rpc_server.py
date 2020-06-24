from concurrent import futures
import grpc
from proto_files.structures_pb2_grpc import SampleServiceServicer, add_SampleServiceServicer_to_server
from proto_files.structures_pb2 import SampleResponse


class SampleServiceService(SampleServiceServicer):
    def SampleMethod(self, request, context):
        print("This was hit")
        return SampleResponse(status=400, data="Succesfully passed data from microservice")


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SampleServiceServicer_to_server(SampleServiceService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    try:
        print("Server has been started on port 50051")
        server()
    except KeyboardInterrupt:
        print("\nServer stopped yo!!")
