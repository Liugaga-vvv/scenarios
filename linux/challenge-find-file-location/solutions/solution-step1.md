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
