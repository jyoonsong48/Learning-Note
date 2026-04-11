for (( i=1; i<=5; i++ ))
do
    if [[ $i -eq 2 ]]
    then
    echo "fizz"
    else
    echo "buzz"
    fi
done