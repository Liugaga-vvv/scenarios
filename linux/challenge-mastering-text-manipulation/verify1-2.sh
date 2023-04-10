#!/bin/bash
FILE=/home/labex/example_output.txt
test -f "$FILE"
echo -e "This is line 1.\nThis is line 2.\nThis is line 3." > test_output1.txt
diff example_output.txt test_output1.txt
