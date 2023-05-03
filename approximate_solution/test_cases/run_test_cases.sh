#!/bin/sh
echo "test 1"
python3 ../cs412_max3sat_approx.py < test1.txt
echo "test 2 - 6 variables"
python3 ../cs412_max3sat_approx.py < test2.txt
echo "test 3 - should be unsatisfiable"
python3 ../cs412_max3sat_approx.py < test3.txt
echo "test 4 - should be unsatisfiable"
python3 ../cs412_max3sat_approx.py < test4.txt
echo "test 5 - should be unsatisfiable"
python3 ../cs412_max3sat_approx.py < test5.txt
echo "test 6 - should be unsatisfiable"
python3 ../cs412_max3sat_approx.py < test6.txt
#echo "test 7 - should be unsatisfiable"
#python3 ../cs412_max3sat_approx.py < test7.txt
