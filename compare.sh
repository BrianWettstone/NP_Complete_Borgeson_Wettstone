#!/bin/sh

# Ignore this file, it is not working properly. Has to do with the run test cases bash scripts
#   Dont feel like fixing

echo "Starting comparison"
echo


bash approximate_solution/test_cases/run_test_cases.sh > ./approximate.txt
bash exact_solution/test_cases/run_test_cases.sh > ./exact.txt

cmp approximate exact
status=$?
if [[ $status = 0 ]]; then
  echo "Files are same"
else
  echo "Files are diff"
fi
