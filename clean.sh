#!/usr/bin/bash

rm -rf build

find . -name "__pycache__" -type d | xargs rm -rf
find . -name ".pytest_cache" -type d | xargs rm -rf
find . -name "Budget_Bee.egg-info" -type d | xargs rm -rf