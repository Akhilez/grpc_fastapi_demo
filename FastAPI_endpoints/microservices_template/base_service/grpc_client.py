import grpc

from proto_files.structures_pb2_grpc import SampleServiceStub

channel = grpc.insecure_channel('localhost:50051')
stub = SampleServiceStub(channel)


