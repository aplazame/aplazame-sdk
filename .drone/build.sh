#!/bin/bash

set -e 

make init.test

case $DRONE_BRANCH in
    release)
        make coverage
        python setup.py versioning
        ;;

    master)
        make coverage
        ;;

    *)
        make test
        echo *$DRONE_BRANCH* pull request, all checks have passed
        ;;
esac
