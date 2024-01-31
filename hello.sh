#!/bin/bash

a=2
b=2
c=$((a + b))

echo "Bash says: Hello, World!"
echo "$a + $b = $c"
mylist=("User1" "User2" "User3")
for user in "${mylist[@]}"; do 
	echo "$user"
done

