# Set Up a Basic Proxy

In this step, you will set up a basic proxy that can forward requests to the Kubernetes API server using the Kubernetes proxy command.

Here is the basic command you will use to set up the proxy:

```bash
kubectl proxy
```

This command will start a proxy server on your local machine that listens on port 8001. You can test the proxy by making a request to `http://localhost:8001/api/v1/pods` (assuming you have pods running in your cluster).
