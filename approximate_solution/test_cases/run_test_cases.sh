
for i in {1..21}
do
  echo "Currently running number $i"
  python3 ../cs412_max3sat_approx.py < ./test"$i".txt
  echo "Finished $i"
  echo
done
