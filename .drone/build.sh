#!/bin/bash

set -e 

make init-test

case $DRONE_BRANCH in
    master|release)
        make coverage
        ;;

    *)
        echo pull request, all checks have passed
        ;;
esac
