# Using the Whereis Command

## Introduction

The `whereis` command is used to locate the binary, source, and manual-page files for a command.

## Target

- To find the location of the binary, source, and manual-page files for the `ls` command.
- To find the location of the binary, source, and manual-page files for the `grep` command.
- To find the location of the binary, source, and manual-page files for the `tar` command.

## Result Example

The result of the location of the binary, source, and manual-page files for the `ls` command:

```bash
ls: /bin/ls /usr/share/man/man1/ls.1.gz
```

The result of the location of the binary, source, and manual-page files for the `grep` command:

```bash
grep: /bin/grep /usr/share/man/man1/grep.1.gz /usr/share/info/grep.info.gz
```

The result of the location of the binary, source, and manual-page files for the `tar` command:

```bash
tar: /usr/lib/tar /bin/tar /usr/include/tar.h /usr/share/man/man1/tar.1.gz
```

## Requirements

- You should have a basic understanding of the command line interface.
- You should have a Linux system with the `whereis` command installed.
