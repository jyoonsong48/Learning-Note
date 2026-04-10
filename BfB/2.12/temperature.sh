min_temperature=10
max_temperature=30
temperature=$1

if [[ temperature < 10 ]]
then
echo "TOO COLD!"
elif [[ temperature > 30 ]]
then
echo "TOO HOT!"
else
echo "Just right!"
fi