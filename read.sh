# echo "enter input"
# read num
# echo $num


read -p "Enter your age: " age

if [ $age -lt 0 ]; then
  echo "$age is not a valid age"
elif [ $age -le 12 ]; then
  echo "$age:is Child"
elif [ $age -le 19 ]; then
  echo "$age:is Teenager"
elif [ $age -le 59 ]; then
  echo "$age:is Adult"
else
  echo "$age:is too Old"
fi

# read -p "enter number:" sum

# echo $sum

# read -p "Enter Name: " name
# read -p "Enter Rollno: " roll
# read -p "Enter Collage: " collage
# echo "YOUR NAME: $name" >> data_read.txt
# echo "YOUR ROLLNO: $roll">> data_read.txt
# echo "YOUR COLLAGE: $collage">> data_read.txt

#!/bin/bash

count=1
while [ $count -le 5 ]; do
  echo "Count: $count"
  ((count++))
done