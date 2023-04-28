# Update the Configmap

In this step, you will update the ConfigMap and see how it affects your application.

Update the `configmap.yaml` file with a new value for the `DATABASE_URL` key:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
  DATABASE_URL: postgres://newuser:newpassword@newhost:newport/newdbname
```

This updates the `DATABASE_URL` key to a new value.

To update the ConfigMap, run the following command:

```bash
kubectl apply -f configmap.yaml
```
