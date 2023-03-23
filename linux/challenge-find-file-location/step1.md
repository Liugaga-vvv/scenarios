# Using the Find Command

## Introduction

The `find` command is a powerful tool for locating files on a Linux system. It searches through one or more directory trees of a file system, locating files that match certain criteria.

## Target

- To find all files in the current directory and its subdirectories with the `.txt` extension.
- To find all files in the current directory and its subdirectories that are larger than 1 megabyte.
- To find all files in the current directory and its subdirectories that were modified less than 7 days ago.

## Result Example

Finding all files in the current directory and its subdirectories with the `.txt` extension:

```bash
./report.txt
./docx.txt
./subdirectory/d.txt
...
```

Finding all files in the current directory and its subdirectories that are larger than 1 megabyte:

```bash
./clash/clash
./clash/Country.mmdb
./dwm/.git/objects/pack/pack-46f7ed27f3f54357fda8f988dc3cd2de625a4331.pack
./vmware-tools-distrib/lib/icu/icudt44l.dat
./vmware-tools-distrib/lib/lib32/libgdk_pixbuf-2.0.so.0/libgdk_pixbuf-2.0.so.0
./vmware-tools-distrib/lib/lib32/libgio-2.0.so.0/libgio-2.0.so.0
./vmware-tools-distrib/lib/lib32/libglib-2.0.so.0/libglib-2.0.so.0
./vmware-tools-distrib/lib/lib32/libvmtools.so/libvmtools.so
./vmware-tools-distrib/lib/lib32/libgtk-x11-2.0.so.0/libgtk-x11-2.0.so.0
...
```

Find all files in the current directory and its subdirectories that were modified less than 7 days ago:

```bash
.
./c.docx
./report.txt
./a.bat
./docx.txt
./subdirectory
./subdirectory/d.txt
./subdirectory/e.report
...
```

## Requirements

- You should have a basic understanding of the command line interface.
- You should have a Linux system with the `find` command installed.
