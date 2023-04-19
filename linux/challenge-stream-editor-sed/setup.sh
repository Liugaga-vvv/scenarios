#!/bin/zsh

echo "apple" >> fruits.txt
echo "banana" >> fruits.txt
echo "pear" >> fruits.txt
echo "apple" >> fruits.txt

echo "orange" >> /tmp/verify1.txt
echo "banana" >> /tmp/verify1.txt
echo "pear" >> /tmp/verify1.txt
echo "orange" >> /tmp/verify1.txt

echo "apple" >> fruits1.txt
echo "banana" >> fruits1.txt
echo "pear" >> fruits1.txt
echo "banana" >> fruits1.txt

echo "apple" >> /tmp/verify2.txt
echo "pear" >> /tmp/verify2.txt

echo "apple" >> fruits2.txt
echo "pear" >> fruits2.txt

echo "apple" >> /tmp/verify3.txt
echo "pear" >> /tmp/verify3.txt
echo "grape" >> /tmp/verify3.txt

echo "apple" >> fruits3.txt
echo "pear" >> fruits3.txt
echo "apple" >> fruits3.txt

echo "cherry" >> /tmp/verify4.txt
echo "pear" >> /tmp/verify4.txt
echo "apple" >> /tmp/verify4.txt
