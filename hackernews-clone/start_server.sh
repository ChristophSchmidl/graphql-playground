#!/bin/bash

# To make sure that you can call this script from wherever you want
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python "$DIR"/hackernews/manage.py runserver 0.0.0.0:8000
