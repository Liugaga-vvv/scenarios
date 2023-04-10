# Viewing Differences Between Two States

## Introduction

In this step, you will learn how to use the `git diff` command to view the differences between two states of a file or between two different files.

## Target

- Make changes to a file in your repository.
- View the differences between the current state of the file and a previous state.

## Result Example

Suppose you have a file called `my_file.txt` in your repository, and you have made changes to it. After committing the changes, you can use the `git diff` command to view the differences between the current state of the file and the previous state. The `HEAD^` argument specifies the previous commit, and `HEAD` specifies the current commit. The output of this command will show the differences between the two commits:

```bash
diff --git a/my_file.txt b/my_file.txt
index 1234567..89abcdef 100644
--- a/my_file.txt
+++ b/my_file.txt
@@ -1,2 +1,3 @@
This is the first line.
This is the second line.
+This is the third line.
```

## Requirements

- A Git repository with at least one file.
- Make changes to the file.
- Commit the changes.
- View the differences between the current state of the file and a previous state.
