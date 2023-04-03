# Solution

To find all files in the current directory and its subdirectories with the `.txt` extension, use the following command:

```bash
find . -name "*.txt"
```

To find all files in the current directory and its subdirectories that are larger than 1 megabyte, use the following command:

```bash
find . -size +1M
```

To find all files in the current directory and its subdirectories that were modified less than 7 days ago, use the following command:

```bash
find . -mtime -7
```

To find all files on the system with the word "report" in the filename, use the following command:

```bash
locate report
```

To find all files on the system with the `.docx` extension, use the following command:

```bash
locate *.docx
```

To find the location of the `grep` command, use the following command:

```bash
which grep
```

To find the location of the `tar` command, use the following command:

```bash
which tar
```

To find the location of the `ls` command, use the following command:

```bash
which ls
```

To find the location of the binary, source, and manual-page files for the `ls` command, use the following command:

```bash
whereis ls
```

To find the location of the binary, source, and manual-page files for the `grep` command, use the following command:

```bash
whereis grep
```

To find the location of the binary, source, and manual-page files for the `tar` command, use the following command:

```bash
whereis tar
```
