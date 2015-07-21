#!/bin/bash

git add -A
git commit -m 'drone builder'
git push deploy HEAD:master --force
