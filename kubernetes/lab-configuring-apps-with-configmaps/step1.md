# Create a Configmap

In this step, you will create a ConfigMap containing the configuration data for your application.

Create a file named `configmap.yaml` in `/home/labex/project/` directory with the following contents:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
  DATABASE_URL: postgres://user:password@host:port/dbname
```

This ConfigMap contains a single key-value pair, where the key is `DATABASE_URL` and the value is a PostgreSQL database connection string.

To create the ConfigMap, run the following command:

```bash
kubectl apply -f configmap.yaml
```
