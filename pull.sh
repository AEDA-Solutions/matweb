#!/bin/bash

git add --all
d=$(date +%Y-%m-%d)
git commit -m "lol $d"
git push

