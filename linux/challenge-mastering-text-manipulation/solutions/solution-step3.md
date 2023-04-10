echo -e "This is line 1.\nThis is line 2.\nThis is line 3." > text.txt
sed 's/line/string/g' text.txt
sed 's/line/string/g' text.txt > text_output.txt
