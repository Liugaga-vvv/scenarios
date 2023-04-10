echo -e "John Smith,25,New York\nJane Doe,30,Los Angeles\nBob Johnson,45,Chicago" > data.txt
awk -F ',' '{print $1}' data.txt
awk -F ',' '{print $1}' data.txt > data_output.txt
