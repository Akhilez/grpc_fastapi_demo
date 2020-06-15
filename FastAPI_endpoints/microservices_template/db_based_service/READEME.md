pb files generation command, run it from the db_based_service folder:

python -m grpc_tools.protoc -I . --python_out=./ --grpc_python_out=./ ./proto_files/structures.proto
