# Scale the Application Deployment

## Introduction

If the number of user visits suddenly increases and the existing application cannot carry user requests, it is time to do horizontal scaling of the application.

## Target

Your goal is to expand the replicas of the `helloworld`.

## Result Example

Here's an example of what you should be able to accomplish by the end of this challenge:

1. Extend the number of replicas of the application to 5.

   ![challenge-kubernetes-deployment-management-4-1](assets/challenge-kubernetes-deployment-management-4-1.png)

2. Check if the status of all replicas is Running.

   ![challenge-kubernetes-deployment-management-4-2](assets/challenge-kubernetes-deployment-management-4-2.png)

3. Whether the application can be accessed correctly from the web page.

   ![challenge-kubernetes-deployment-management-4-3](assets/challenge-kubernetes-deployment-management-4-3.png)

## Requirements

To complete this challenge, you will need:

- Familiarity with the basics of Docker and Kubernetes.
- Skills in basic operations using Kubernetes command line tools (`kubectl`) and YAML files.
