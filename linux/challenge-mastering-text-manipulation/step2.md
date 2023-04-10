# Extract Specific Fields Using AWK

## Introduction

`awk` is a powerful command-line tool for processing and manipulating text data in files. It allows you to perform a wide range of text manipulation tasks, including searching for patterns, filtering data, and performing calculations.

## Target

In this step, you will use the `awk` command to extract specific fields from a file.

## Result Example

Suppose you have a file called `data.txt` that contains the following lines of text:

```
John Smith,25,New York
Jane Doe,30,Los Angeles
Bob Johnson,45,Chicago
```

In the current path `/home/labex/`, to extract only the names from this file, you can use the `awk` command, and save the output of `awk` to `data_output.txt`.

The output will be:

```
John Smith
Jane Doe
Bob Johnson
```

## Requirements

- A Linux terminal or command prompt
- A text editor (such as `vi`, `nano`, or `emacs`)
- A text file to manipulate
