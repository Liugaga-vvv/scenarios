# Build A Web Image

## Introduction

We usually use the `nginx` to run static applications such as websites. In this section, we will build our web image.

## Target

Your goal is to create a Docker container image and package a simple web application into it, then use that image to start the container and make it accessible properly.

## Result Example

Here's an example of what you should be able to accomplish by the end of this challenge:

1. Create a new file called `index.html` in the `/home/labex/Code` directory with the content `hello labex`.

   ![challenge-docker-image-and-registry-2-1](assets/challenge-docker-image-and-registry-2-1.png)

2. Create a new file called `Dockerfile` with the following contents

   ![challenge-docker-image-and-registry-2-2](assets/challenge-docker-image-and-registry-2-2.png)

3. Build your web image with the format of `your_dockerhub_id/web:1.1.0`.

   ![challenge-docker-image-and-registry-2-3](assets/challenge-docker-image-and-registry-2-3.png)

4. Push the created web image to the `dockerhub`.

   ![challenge-docker-image-and-registry-2-4](assets/challenge-docker-image-and-registry-2-4.png)

5. start a container called `web` with `your_dockerhub_id/web:1.1.0`, and we also need to map port `80` to the host.

   ![challenge-docker-image-and-registry-2-5](assets/challenge-docker-image-and-registry-2-5.png)

6. Use the `curl` command to visit `http://127.0.0.1` and check that the output is `hello labex`.

   ![challenge-docker-image-and-registry-2-6](assets/challenge-docker-image-and-registry-2-6.png)

## Requirements

To complete this challenge, you will need:

- Building with `Dockerfile`
- Specify the base image as `Nginx:latest`
- Expose port `80` in the `Dockerfile` using the EXPOSE command
- After the build is complete, make sure the container can run properly and respond to HTTP requests
