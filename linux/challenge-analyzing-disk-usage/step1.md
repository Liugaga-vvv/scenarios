## View Disk Usage Statistics for Mounted File-systems

### Introduction

The `df` command displays the amount of disk space available and used on mounted file-systems, such as hard drives, USB drives, and network drives.

### Target

View disk usage statistics for all mounted file-systems.

### Result Example

The following example is only the effect of local operation, and has nothing to do with the actual effect.

```bash
Filesystem Size Used Avail Use% Mounted on
/dev/sda1 20G 15G 4.2G 79% /
tmpfs 1.5G 12K 1.5G 1% /dev/shm
/dev/sdb1 50G 35G 15G 71% /mnt/backup
```

### Requirement

- Display sizes in human-readable format.
