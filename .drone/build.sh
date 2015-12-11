#!/bin/bash

set -e 

make init.test

case $DRONE_BRANCH in
    release)
        make coverage
        python setup.py versioning
        git commit -m "update release version" aplazame_sdk/__init__.py
        ;;

    master)
        make coverage
        ;;

    *)
        make test
        echo *$DRONE_BRANCH* pull request, all checks have passed
        ;;
esac
