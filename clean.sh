#!/user/bin/bash

rm -rf bin/

find . -name "__pycache__" -type d | xargs rm -rf
find . -name ".pytest_cache" -type d | xargs rm -rf