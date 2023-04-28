# Kubernetes Cordon and Uncordon Command

In a Kubernetes cluster, nodes can go into various states, such as "ready" or "not ready". The `cordon` and `uncordon` commands are used to control the scheduling of pods on a particular node. The `cordon` command marks a node as "unschedulable", preventing new pods from being scheduled on that node, while the `uncordon` command marks a node as "schedulable" again, allowing new pods to be scheduled on that node. In this lab, we will explore how to use these commands to control the scheduling of pods on nodes in a Kubernetes cluster.
