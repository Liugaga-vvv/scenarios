#!/bin/bash
FILE=/home/labex/text_output.txt
test -f "$FILE"
echo -e "This is string 1.\nThis is string 2.\nThis is string 3." > test_output3.txt
diff text_output.txt test_output3.txt
