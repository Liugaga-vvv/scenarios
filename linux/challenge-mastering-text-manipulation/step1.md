# Search For Specific Lines Using GREP

## Introduction

`grep` is a command-line utility for searching through text files for lines that match a specific pattern. It is an essential tool for any Linux user who works with text files, and can be used for a wide range of tasks, from finding specific words or phrases in a document to searching through log files for errors.

## Target

In this step, you will use the `grep` command to search for specific lines of text in a file.

## Result Example

Suppose you have a file called `example.txt` that contains the following lines of text:

```
This is line 1.
This is line 2.
This is line 3.
This is string 4.
This is string 5.
```

To search for lines in the current path `/home/labex/` that contain the word `line`, you can use the `grep` command, and save the output of `grep` to `example_output.txt`.

The output will be:

```
This is line 1.
This is line 2.
This is line 3.
```

## Requirements

- A Linux terminal or command prompt
- A text editor (such as `vi`, `nano`, or `emacs`)
- A text file to search
