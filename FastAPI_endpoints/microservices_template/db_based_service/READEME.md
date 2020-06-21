pb files generation command, run it from the db_based_service folder:

python -m grpc_tools.protoc -I . --python_out=./ --grpc_python_out=./ ./proto_files/structures.proto


Add current directory and db directory to PYTHONPATH by  running in current directory and db directory:

export PYTHONPATH=.

After adding that upgrade head, stamp head and do a revision
 - alembic upgrade head
 - alembic stamp head
 - alembic revision --autogenerate -m "baseline"
 This will create the first entry in the versions folder of alembic

If the --autogenerate flag isn't added it'll create a basic version .py file which will just have pass in both upgrade() and downgrade() functions

To bring the databse itself up to date run:
- alembic upgrade head
