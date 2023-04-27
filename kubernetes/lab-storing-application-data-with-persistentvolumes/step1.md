# Create a PersistentVolume

In this step, you will create a PersistentVolume that can be used to store data. You will create a YAML file called `pv.yaml` with the following content:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /mnt/data
```

This file creates a PersistentVolume with a capacity of 1Gi and an access mode of ReadWriteOnce. The `hostPath` field specifies that the data will be stored on the host machine at the path `/mnt/data`. The `persistentVolumeReclaimPolicy` field is set to Retain, which means that the data will be preserved even if the PersistentVolume is deleted.

Apply the PersistentVolume to your cluster with the following command:

```shell
kubectl apply -f pv.yaml
```
