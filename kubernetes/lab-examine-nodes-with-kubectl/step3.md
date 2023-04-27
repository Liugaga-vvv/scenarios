# Taints and Tolerations

Taints and tolerations can be used to control which pods can be scheduled on which nodes in your cluster. A taint is a special label that marks a node as unsuitable for certain types of pods, and a toleration is a setting that allows a pod to be scheduled on a node with a matching taint.

1. To view the taints for a specific node, run the following command:

   ```bash
   kubectl describe node minikube | grep Taints
   ```

   This will display the taints for the specified node.

2. To add a taint to a node, run the following command:

   ```bash
   kubectl taint node minikube app=backend:NoSchedule
   ```

3. Create a toleration to a pod, run the following command:

   ```bash
   cat << EOF | kubectl apply -f -
   apiVersion: v1
   kind: Pod
   metadata:
     name: my-pod
   spec:
     containers:
       - name: my-container
         image: nginx
     tolerations:
       - key: app
         operator: Exists
         effect: NoSchedule
   EOF
   ```

   This pod uses `app` as the name of the taint and `NoSchedule` as the effect the taint should have.
