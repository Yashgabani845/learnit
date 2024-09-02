# Introduction to Docker

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow developers to package an application with all of its dependencies into a standardized unit for software development.

## Why Use Docker?

- **Consistency:** Docker ensures that your application runs the same way everywhere, from development to production.
- **Efficiency:** Containers are lightweight and share the host OS's resources, making them faster to start and stop compared to virtual machines.
- **Portability:** Once packaged into a Docker container, your application can run on any system that supports Docker.

## Key Concepts

### 1. Docker Image
A Docker image is a lightweight, standalone package that includes everything needed to run a piece of software, including the code, runtime, libraries, and configuration settings.

### 2. Docker Container
A container is a running instance of a Docker image. It’s the environment where your application runs. Multiple containers can be run from the same image, each operating independently.

### 3. Dockerfile
A Dockerfile is a text file that contains instructions on how to build a Docker image. It specifies the base image, dependencies, configurations, and commands that should be run.

### 4. Docker Hub
Docker Hub is a cloud-based registry service where Docker images can be stored and shared. You can find both official images and community-contributed images here.

## Basic Docker Commands

- **`docker pull [image-name]`**: Downloads a Docker image from Docker Hub.
- **`docker run [image-name]`**: Runs a container from a Docker image.
- **`docker ps`**: Lists all running containers.
- **`docker stop [container-id]`**: Stops a running container.
- **`docker rm [container-id]`**: Removes a stopped container.
- **`docker build -t [image-name] .`**: Builds a Docker image from a Dockerfile in the current directory.

## Example: Running a Simple Web Server

