# Test the Ingress Resource

Finally, we can test the Ingress resource to make sure everything is working correctly.

First, determine the IP address of the node:

```bash
kubectl get node -o wide
```

This command will get the kubernetes node address, The IP address labeled as `INTERNAL-IP`.

Next, add an entry to your `/etc/hosts` file to map the `example.com` domain to the IP address of the node:

```
echo "<IP_ADDRESS> example.com" | sudo tee -a /etc/hosts
```

Replace `<IP_ADDRESS>` with the internal IP address of the node address.

Then, get service nodeport for `ingress-nginx`.

```bash
kubectl get services -n ingress-nginx
```

This command will dcurisplay a list of services in the `ingress-nginx` namespace. Look for the `nginx-ingress-controller` service and note its `NodePort`.

Finally, use `curl` to make an HTTP request to the Ingress endpoint:

```bash
curl http://example.com: < NodePort > /
```

Replace `<NodePort>` with the `NodePort` of the `nginx-ingress-controller` service.

If everything is set up correctly, you should see the Nginx welcome page.

You can also test the Ingress by using a web browser to visit `http://example.com:<NodePort>/nginx`.

Congratulations, you have successfully set up an Ingress resource in Kubernetes and tested it to ensure that it is working correctly.
