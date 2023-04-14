# Checking the Status of Your Repository

## Introduction

In this step, you will learn how to use the `git status` command to check the current status of your repository.

## Target

- View the status of your repository before and after making changes.
- Understand the output of the git status command.

## Result Example

Suppose you have a file called `my_file.txt` in your repository, and you have made changes to it. Before staging or committing these changes, you can use the `git status` command to view the current status of your repository. The output of this command will show that there are changes to be committed:

```bash
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   my_file.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

After staging and committing the changes, you can use the `git status` command again to verify that your repository is up to date. The output of this command will show that your repository is up to date:

```bash
On branch master
nothing to commit, working tree clean
```

## Requirements

- A Git repository with at least one file.
- Make changes to the file.
- View the current status of your repository before and after staging and committing the changes.
- Understand the output of the git status command.
