# Describe a Service

In this step, you will learn how to use the `describe` command to view information about a Kubernetes Service.

1.  Create a file called `myapp-service.yaml` with the following content:

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: myapp-service
    spec:
      selector:
        app: myapp-deployment
      ports:
        - protocol: TCP
          port: 80
          targetPort: 80
    ```

    Create the service using the following command:

    ```bash
    kubectl apply -f myapp-service.yaml
    ```

2.  Use the following command to describe the service:

    ```bash
    kubectl describe service myapp-service
    ```

This command will retrieve detailed information about the specified Service, including status, labels, annotations, events, and more.
