#!/bin/bash

set -e 

make init-test

echo branch: $DRONE_BRANCH

if [ "$DRONE_BRANCH" = "release" ];
	then make coverage;
fi
