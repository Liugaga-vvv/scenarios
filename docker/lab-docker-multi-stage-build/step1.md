# Create A Dockerfile With Multi-stage Build

The first step in using Docker Multi-stage Build is to create a Dockerfile with multiple stages. To do this, follow these steps:

1. Create a new directory called `myapp` and navigate into it:

```bash
mkdir myapp
cd myapp
```

2. Download NodeJS source code

```bash
git clone https://github.com/joker-bai/nodejs-example.git .
```

3. Create a new file called `Dockerfile` in the `myapp` directory:

```bash
touch Dockerfile
```

4. Open the `Dockerfile` file in a text editor, and add the following content:

```Dockerfile
# Stage 1: Build the application
FROM node:14-alpine AS base
WORKDIR /app
COPY . ./
RUN npm install

# Stage 2: Create the final image
FROM node:14-alpine
WORKDIR /app
COPY --from=base /app/ .
EXPOSE 3000
CMD [ "npm", "start" ]
```

This Dockerfile uses two stages. The first stage builds the application by installing the required dependencies and running the build script, and the second stage creates the final image by copying the compiled code from the first stage, installing only the production dependencies, and exposing the necessary port.
