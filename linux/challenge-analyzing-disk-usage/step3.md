## Find the Largest File and Move it to the Directory

### Introduction

The `du` command can also be used to find the largest file or directory on a system.

### Target

Find the largest file in the `~/myrepo` directory and move it to `/tmp` directory.

### Result Example

The following example is only the effect of local operation, and has nothing to do with the actual effect.

```bash
46G ~/myrepo
37G ~/myrepo/largest_file.txt
5.6G ~/myrepo/a.txt
1.5G ~/myrepo/b.txt
...
```

### Requirement

- Find the largest file in the `~/myrepo` directory.
- Move the file to the `/tmp` directory.
