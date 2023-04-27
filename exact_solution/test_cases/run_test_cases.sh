#!/bin/sh
echo "test 1"
python3 ../exact_solution.py < test1.txt
echo "test 2 - 6 variables"
python3 ../exact_solution.py < test2.txt
echo "test 3 - should be unsatisfiable"
python3 ../exact_solution.py < test3.txt
echo "test 4 - should be unsatisfiable"
python3 ../exact_solution.py < test4.txt
echo "test 5 - should be unsatisfiable"
python3 ../exact_solution.py < test5.txt
echo "test 6 - should be unsatisfiable"
python3 ../exact_solution.py < test6.txt
#echo "test 7 - should be unsatisfiable"
#python3 ../exact_solution.py < test7.txt
