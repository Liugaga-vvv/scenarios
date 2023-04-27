# Describe a Deployment

In this step, you will learn how to use the `describe` command to view information about a Kubernetes Deployment.

1. Create a file called `myapp-deployment.yaml` with the following content:

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: myapp-deployment
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: myapp-deployment
     template:
       metadata:
         labels:
           app: myapp-deployment
       spec:
         containers:
           - name: myapp-container
             image: nginx:latest
             ports:
               - containerPort: 80
   ```

   Create the deployment using the following command:

   ```bash
   kubectl apply -f myapp-deployment.yaml
   ```

2. Describe the deployment:

   ```bash
   kubectl describe deployment myapp-deployment
   ```

This command will retrieve detailed information about the specified Deployment, including status, labels, annotations, events, and more.
