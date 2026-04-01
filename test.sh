
#read X
#read Y
#read Z

read X
read Y
read Z

if [[ "$X" -eq "$Y" && "$Y" -eq "$Z" ]]; then
  echo "EQUILATERAL"

elif [[ "$X" -ne "$Y" && "$Y" -ne "$Z" ]]; then
  echo "SCALENE"

else
  echo "ISOSCELES"
fi