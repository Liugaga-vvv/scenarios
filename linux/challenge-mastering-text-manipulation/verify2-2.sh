#!/bin/bash
FILE=/home/labex/data_output.txt
test -f "$FILE"
echo -e "John Smith\nJane Doe\nBob Johnson" > test_output2.txt
diff data_output.txt test_output2.txt
