# Create a PersistentVolumeClaim

In this step, you will create a PersistentVolumeClaim that will be used to request storage from the PersistentVolume you created in Step 1. You will create a YAML file called `pvc.yaml` with the following content:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
```

This file creates a PersistentVolumeClaim with an access mode of ReadWriteOnce and a request for 500Mi of storage from the PersistentVolume.

Apply the PersistentVolumeClaim to your cluster with the following command:

```shell
kubectl apply -f pvc.yaml
```
