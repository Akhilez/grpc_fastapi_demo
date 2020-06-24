#!/bin/bash

kill -9 `lsof -t -i:8000`
kill -9 `lsof -t -i:50051`
