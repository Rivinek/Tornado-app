#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

until ping -c1 postgresapp  &>/dev/null; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
