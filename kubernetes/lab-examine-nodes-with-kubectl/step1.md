# Basic Node Information

The first thing you will do is get basic information about the nodes in your cluster.

1. To view a list of nodes in your cluster, run the following command:

   ```bash
   kubectl get nodes
   ```

   This will display a list of all the nodes in your cluster along with their status.

2. To get more detailed information about a specific node, run the following command:

   ```bash
   kubectl describe node minikube
   ```

   Replace `minikube` with the name of the node you want to examine. This will give you detailed information about the node's status, capacity, and usage.
