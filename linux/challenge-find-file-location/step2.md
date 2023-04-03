# Using the Locate Command

## Introduction

The `locate` command is a fast way to find files on a Linux system. It uses a pre-built index of the file system to quickly find files by name.

## Target

- To find all files on the system with the word "report" in the filename.
- To find all files on the system with the `.docx` extension.

## Result Example

Finding all files on the system with the word "report" in the filename:

```bash
/var/lib/dpkg/info/python3-reportlab-accel:amd64.md5sums
/var/lib/dpkg/info/python3-reportlab.list
/var/lib/dpkg/info/python3-reportlab.md5sums
/var/lib/dpkg/info/python3-reportlab.postinst
/var/lib/dpkg/info/python3-reportlab.prerm
/var/lib/systemd/deb-systemd-helper-enabled/apport-autoreport.path.dsh-also
/var/lib/systemd/deb-systemd-helper-enabled/paths.target.wants/apport-autoreport.path
...
```

Finding all files on the system with the `.docx` extension:

```bash
/etc/systemd/system/paths.target.wants/apport-autoreport.path
/home/sorria/.local/share/omf/.github/ISSUE_TEMPLATE/bug_report.md
/home/sorria/oh-my-fish/.github/ISSUE_TEMPLATE/bug_report.md
/lib/systemd/system/apport-autoreport.path
/lib/systemd/system/apport-autoreport.service
/usr/lib/firefox/crashreporter
/usr/lib/firefox/crashreporter.ini
...
```

## Requirements

- You should have a basic understanding of the command line interface.
- You should have a Linux system with the locate command installed.
