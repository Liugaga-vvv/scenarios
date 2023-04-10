# Data Volume Management

## Introduction

Data volumes are a standard operation for data persistence in Docker, and in this section, I will take you through the standard operations on data volumes in practice.

## Target

Your goal is to create a data volume called `my-vol` using the `docker` command, and add a file called `test.txt` to its volume.

## Result Example

Here's an example of what you should be able to accomplish by the end of this challenge:

1. Create a data volume named `my-vol`.

   ![challenge-docker-volume-management-1-1](assets/challenge-docker-volume-management-1-1.png)

2. Get `Mountpoint` by data volume details.

   ![challenge-docker-volume-management-1-2](assets/challenge-docker-volume-management-1-2.png)

3. Go to `Mountpoint` and create the `test.txt` file.

   ![challenge-docker-volume-management-1-3](assets/challenge-docker-volume-management-1-3.png)

## Requirements

To complete this challenge, you will need:

- Know how to create a data volume using the `dokcer` command.
- Create a file using the `root` user.
