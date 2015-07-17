#!/bin/bash

make init
make test

echo $SLACK_WEBHOOOK_URL
echo $COVERALLS_REPO_TOKEN
