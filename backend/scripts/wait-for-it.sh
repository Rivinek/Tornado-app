#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

sleep 4

>&2 echo "Postgres is up - executing command"
exec $cmd
