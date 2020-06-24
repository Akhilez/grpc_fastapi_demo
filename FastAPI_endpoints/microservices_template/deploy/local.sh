#!/bin/bash
set -x


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )/.."

# gRPC stuff
cd $DIR/db_based_service
python rpc_server.py &

# base stuff
cd $DIR/base_services
uvicorn main:app --reload &

jobs

