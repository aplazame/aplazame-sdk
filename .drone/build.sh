#!/bin/bash

set -e 

cat $HOME/.ssh/id_rsa
ls -las $HOME/.ssh

git pull origin master

cat $HOME/.ssh/id_rsa.pub

make init-test
make test
make coverage
