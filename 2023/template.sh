#!/bin/bash

set -e

echo "What day are you starting? "
read DAY

mkdir $DAY
cp ./2023-template/*.py ./$DAY

mv ./$DAY/puzzle.py ./$DAY/puzzle$DAY.py
mv ./$DAY/test_puzzle.py ./$DAY/test_puzzle$DAY.py

if [[ ${DAY:0:1} == 0 ]]; then
    sed -i "" "s/day = .../day = ${DAY:1}/g" ./$DAY/puzzle$DAY.py 
else
    sed -i "" "s/day = .../day = $DAY/g" ./$DAY/puzzle$DAY.py 
fi


sed -i "" "s/from puzzle/from puzzle$DAY/" ./$DAY/test_puzzle$DAY.py
