#!/bin/bash

git status

git pull origin master
git add -A
git commit -am 'drone builder'
git push origin master --force
