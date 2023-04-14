# Start Docker Container

## Introduction

This section will take you through two ways to start a container: to change the state of the container to run.

## Target

Your goal is to start the container using two different ways, the first is to create the container and then start it, and the second is to start the container directly using the `docker run` command.

## Result Example

Here's an example of what you should be able to accomplish by the end of this challenge:

1. Start by pulling the image `nginx:1.22.1` to the host.

   ![challenge-container-lifecycle-management-1-1](assets/challenge-container-lifecycle-management-1-1.png)

2. Create a new container called `web1` using the `nginx:1.22.1` image.

   ![challenge-container-lifecycle-management-1-2](assets/challenge-container-lifecycle-management-1-2.png)

3. Start the container and let its state become Running.

   ![challenge-container-lifecycle-management-1-3](assets/challenge-container-lifecycle-management-1-3.png)

4. Use the `docker inspect web1` command to see specific status details.

   ![challenge-container-lifecycle-management-1-4](assets/challenge-container-lifecycle-management-1-4.png)

5. Create a new container called `web2` using the `nginx:1.22.1` image with the `docker run` command.

   ![challenge-container-lifecycle-management-1-5](assets/challenge-container-lifecycle-management-1-5.png)

## Requirements

To complete this lab, you will need:

- A working Docker installation.
- Know the commands of Docker.
