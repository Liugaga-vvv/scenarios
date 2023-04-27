# Labels and Annotations

Labels and annotations can be used to add metadata to nodes in your cluster. This metadata can be used to select nodes for specific tasks or to filter nodes based on certain criteria.

1. To view the labels and annotations for a specific node, run the following command:

   ```bash
   kubectl get node minikube --show-labels=true
   ```

   This will display the labels and annotations for the specified node.

2. To add a label to a node, run the following command:

   ```bash
   kubectl label node minikube org=labex
   ```

3. To add an annotation to a node, run the following command:

   ```bash
   kubectl annotate node minikube environment=production
   ```

4. Use the following command to check the labels on the node:

   ```bash
   kubectl get nodes --show-labels
   ```

   This will output a list of all the nodes in the cluster along with their labels,Nodes can be labeled to help identify their purpose or characteristics.
