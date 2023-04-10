# Delete Docker Container

## Introduction

Removing or deleting the container means destroying all the processes running inside the container and then deleting the Container.

## Target

Your goal is to stop the running container and delete it.

## Result Example

Here's an example of what you should be able to accomplish by the end of this challenge:

1. Start a `web4` container using the `nginx:1.23.1` image.

   ![challenge-container-lifecycle-management-3-1](assets/challenge-container-lifecycle-management-3-1.png)

2. Try to delete the running `web4` container. But the docker daemon throws an error. We can not delete a running docker container.

   ![challenge-container-lifecycle-management-3-2](assets/challenge-container-lifecycle-management-3-2.png)

3. Stop the `web4` container.

   ![challenge-container-lifecycle-management-3-3](assets/challenge-container-lifecycle-management-3-3.png)

4. Delete the `web4` container.

   ![challenge-container-lifecycle-management-3-4](assets/challenge-container-lifecycle-management-3-4.png)

## Requirements

To complete this lab, you will need:

- Ensure that `Docker` is installed and functioning.
- A running container.
