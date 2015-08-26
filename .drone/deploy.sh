#!/bin/bash

# install requirements
make init-deploy

# package versioning
python setup.py versioning

# publish on pypi
make publish
