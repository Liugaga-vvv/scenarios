# Adding Changes to the Staging Area

## Introduction

In this step, you will learn how to use the `git add` command to stage changes to your repository.

## Target

- Go to the `~/myrepo` directory for operations.
- Stage changes to a file in your repository.
- View the status of the repository to verify that the changes have been staged.

## Result Example

Suppose you have a file called `my_file.txt` in your repository, the output of the `git status` command will show that the changes to `my_file.txt` have been staged:

```bash
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: my_file.txt
```

## Requirements

- A Git repository with at least one file.
- Make changes to the file.
- Verify that the changes have not been staged.
- Stage the changes.
- Verify that the changes have been staged.
