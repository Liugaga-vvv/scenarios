# Create Containers With Host Path

## Introduction

In many cases, we are not used to data volumes but instead. Use the native directory directly for data persistence. In this section, we will use the native directory to create containers.

## Target

Your goal is to create a container that uses `Host Path`, then copy the local files into the container and verify that the files in that container are the same as those in `Host Path`.

## Result Example

Here's an example of what you should be able to accomplish by the end of this challenge:

1. Create an `nginx` directory in the `/tmp` directory.

   ![challenge-docker-volume-management-3-1](assets/challenge-docker-volume-management-3-1.png)

2. Start the `nginx-host` container that mounts the `/tmp/nginx` directory to the `/usr/share/nginx/html` directory in the container.

   ![challenge-docker-volume-management-3-2](assets/challenge-docker-volume-management-3-2.png)

3. Check the specific mount details with the docker inspect command.

   ![challenge-docker-volume-management-3-3](assets/challenge-docker-volume-management-3-3.png)

4. Create a local file called `nginx.txt` with the content `hello nginx`.

   ![challenge-docker-volume-management-3-4](assets/challenge-docker-volume-management-3-4.png)

5. Copy the `nginx.txt` file to the `/usr/share/nginx/html` directory of the `nginx-host` container.

   ![challenge-docker-volume-management-3-5](assets/challenge-docker-volume-management-3-5.png)

6. Check the `/tmp/nginx` directory on the local machine to see if there is a `nginx.txt` file.

   ![challenge-docker-volume-management-3-6](assets/challenge-docker-volume-management-3-6.png)

## Requirements

To complete this challenge, you will need:

- Know the `Host Path` path you want to use.
- Know how to use some relevant commands inside the container to verify if the host directory or file can be accessed.
- Know how to start the container using Host Path.
- Be familiar with basic Linux commands, such as `cd`, `mkdir`, `touch`, etc.
