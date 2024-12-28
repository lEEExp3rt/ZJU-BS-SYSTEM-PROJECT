#!/user/bin/bash

rm -rf bin/

cd src/
find . -name "__pycache__" -type d | xargs rm -rf