#!/bin/bash

# install requirements
make init.deploy

# publish on pypi
make publish

# commit to master
git commit -m "update release version"
git push origin master
