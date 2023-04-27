# Networking With Ingress on Kubernetes

In this lab, you will learn how to use Ingress to route external traffic to services running in a Kubernetes cluster.

## Introduction

Kubernetes Ingress is a powerful tool for managing external access to services in a Kubernetes cluster. Ingress acts as a layer 7 load balancer, allowing you to route traffic to different services based on the incoming URL path or hostname.

In this lab, we will create a sample application and expose it to the outside world using Ingress. We will use `nginx-ingress` as the Ingress controller, which is a popular and widely-used solution for Kubernetes Ingress.
