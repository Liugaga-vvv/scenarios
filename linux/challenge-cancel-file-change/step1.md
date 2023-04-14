# Undo the Changes You Made

## Introduction

As a Git user, it's important to know how to undo changes you made to a file in the working directory. The `restore` command can be used to discard the changes and restore the file to its previous state.

## Target

Your goal is to use the `git restore` command to undo changes you made to a file in a Git repository. Before you execute this command, you should go into the `~/myrepo` directory to complete the operation.

## Result Example

Here's an example of what you should be able to accomplish by the end of this challenge:

1. Make changes to the file `myfile.txt` in the working directory.

   ```bash
   On branch master
   Changes not staged for commit:
   (use "git add <file>..." to update what will be committed)
   (use "git restore <file>..." to discard changes in working directory)
   modified: myfile.txt
   ```

2. Use the restore command to undo the changes and restore the file `myfile.txt` to its previous state.

   ```bash
   On branch master
   nothing to commit, working tree clean
   ```

## Requirements

To complete this lab, you will need:

- A Git repository with at least one commit.
- A basic understanding of Git concepts like commits, branches, and the staging area.
