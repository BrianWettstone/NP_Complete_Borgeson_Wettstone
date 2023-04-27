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
echo $(date)
echo "test 7 - should be unsatisfiable"
python3 ../exact_solution.py < test7.txt
echo $(date)
echo "test 8 - should be unsatisfiable"
python3 ../exact_solution.py < test8.txt
echo $(date)
echo "test 9 - should be unsatisfiable"
python3 ../exact_solution.py < test9.txt
echo $(date)
echo "test 10 - should be unsatisfiable"
python3 ../exact_solution.py < test10.txt
echo $(date)
echo "test 11 - should be unsatisfiable"
python3 ../exact_solution.py < test11.txt
echo $(date)
echo "test 12 - should be unsatisfiable"
python3 ../exact_solution.py < test12.txt
echo $(date)
echo "test 13 - should be unsatisfiable"
python3 ../exact_solution.py < test13.txt
echo $(date)
echo "test 14 - should be unsatisfiable"
python3 ../exact_solution.py < test14.txt
echo $(date)
echo "test 15 - should be unsatisfiable"
python3 ../exact_solution.py < test15.txt
echo $(date)
echo "test 16 - should be unsatisfiable"
python3 ../exact_solution.py < test16.txt
echo $(date)
echo "test 17 - should be unsatisfiable"
python3 ../exact_solution.py < test17.txt
echo $(date)
