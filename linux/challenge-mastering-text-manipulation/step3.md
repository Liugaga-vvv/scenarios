# Replace Text In A File Using SED

## Introduction

`sed` is a stream editor for modifying text data. It allows you to make changes to a file without opening it in an editor, and can be used for a wide range of tasks, from replacing text in a file to performing complex transformations on your data.

## Target

In this step, you will use the `sed` command to replace text in a file.

## Result Example

Suppose you have a file called `text.txt` that contains the following lines of text:

```
This is line 1.
This is line 2.
This is line 3.
```

In the current path `/home/labex/`, to replace `line` with `string` in this file, you can use the `sed` command, and save the output of `sed` to `text_output.txt`.

The output will be:

```
This is string 1.
This is string 2.
This is string 3.
```
