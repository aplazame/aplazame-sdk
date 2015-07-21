#!/bin/bash

set -e 

cat $HOME/.ssh/id_rsa
ls -las .ssh

git pull origin master

make init-test
make test
make coverage
