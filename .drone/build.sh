#!/bin/bash

set -e 

make init-test
make test
make coverage
