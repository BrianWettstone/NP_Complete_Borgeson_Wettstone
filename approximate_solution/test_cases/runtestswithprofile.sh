
for i in {1..21}
do
  echo "Currently running number $i"
  kernprof -lv ../cs412_max3sat_approx.py < ./test"$i".txt > cs412_max3sat_approx_profile"$i".txt
  echo "Finished $i"
  echo
done