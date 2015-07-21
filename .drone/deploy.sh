#!/bin/bash

git add -A
git commit -am 'drone builder'
git push origin HEAD:master --force
