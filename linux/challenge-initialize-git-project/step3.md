# Cloning an Existing Repository with Depth

## Introduction

Sometimes, when you clone a Git repository, you may not need to download all of the repository's history. In this challenge, you will learn how to use the `git clone` command with the `--depth` option to clone an existing repository with a limited depth.

## Target

- To clone an existing `https://github.com/github/gitignore` repository with limited history using `git clone` and the `--depth` option.

## Result Example

To clone an existing repository with limited history, navigate to the `~/project` directory where you want to clone the repository .

This will create a new directory containing the repository's files and subdirectories with limited history.

```bash
Cloning into 'gitignore'...
remote: Enumerating objects: 8094, done.
remote: Counting objects: 100% (171/171), done.
remote: Compressing objects: 100% (118/118), done.
remote: Total 8094 (delta 78), reused 106 (delta 46), pack-reused 7923
Receiving objects: 100% (8094/8094), 2.81 MiB | 1.90 MiB/s, done.
Resolving deltas: 100% (4074/4074), done.
```

## Requirements

- Git installed on your local machine.
- Access to an existing Git repository.
