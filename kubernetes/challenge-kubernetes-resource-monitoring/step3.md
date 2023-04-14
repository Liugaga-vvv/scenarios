# Create Prometheus Deployment

## Introduction

Prometheus is flexible in how it can be deployed in Kubernetes by way of `Prometheus Operator`, or directly using Deployment.

A Create Prometheus Deployment challenge is provided here to help users deepen their understanding and skills in using Prometheus deployments and configurations.

## Target

Your goal is to complete a Prometheus deployment in Kubernetes, which requires the Namespace and ClusterRole from `step 1` and the ConfigMap from `step 2`.

## Result Example

Here's an example of what you should be able to accomplish by the end of this challenge:

1. Create a file called `prometheus-deployment.yaml` and copy the following content to the [Prometheus Deployment File](https://raw.githubusercontent.com/joker-bai/kube-prometheus/main/deployment.yaml). In this configuration we will mount the Prometheus config map as a file inside `/etc/prometheus` as explained in the previous section.

   ![challenge-kubernetes-reousrce-monitoring-3-1](assets/challenge-kubernetes-resource-monitoring-3-1.png)

2. Create a deployment on monitoring namespace using the above file.

   ![challenge-kubernetes-reousrce-monitoring-3-2](assets/challenge-kubernetes-resource-monitoring-3-2.png)

3. Check that Prometheus has been successfully deployed.

   ![challenge-kubernetes-reousrce-monitoring-3-3](assets/challenge-kubernetes-resource-monitoring-3-3.png)

If all Pods are Running, it means Prometheus deployment is successful.

## Requirements

To complete this challenge, you will need:

- A Kubernetes cluster has been installed and configured as required.
- You have basic knowledge of Kubernetes and YAML orchestration.
- You are ready to create a Prometheus Deployment and Service.
