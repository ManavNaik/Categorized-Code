max_of_three() {
    if [ $1 -ge $2 ] && [ $1 -ge $3 ]; then
        echo $1
    elif [ $2 -ge $1 ] && [ $2 -ge $3 ]; then
        echo $2
    else
        echo $3
    fi
}
num1=25
num2=17
num3=42
largest=$(max_of_three $num1 $num2 $num3)
echo "The largest number among $num1, $num2, and $num3 is: $largest"