# Modify Kubeconfig Files

## Introduction

Kubeconfig files are used to configure access to a Kubernetes cluster. They specify the following information:

- The cluster to use
- The user to authenticate with
- The context to use (which combines a cluster and user)

By default, `kubectl` uses the `~/.kube/config` file as the kubeconfig file. However, you can specify a different kubeconfig file with the `--kubeconfig` flag.
