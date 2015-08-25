#!/bin/bash

set -e 

make init-test

case $DRONE_BRANCH in
    dev)
        echo pull request
        ;;

    @(master|release) )
        make coverage
        ;;

    *)
        echo "Unknown"
        ;;
esac
