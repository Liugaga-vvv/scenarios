# Create PV and PVC

The first step is to create a Pod with a Persistent Volume (PV) and a Persistent Volume Claim (PVC). PVs and PVCs are used to store and access data persistently across Pod restarts.

To do this, you will first create a PV.

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
  hostPath:
    path: "/mnt/data"
```

Save the above code in a file named `pv.yaml` and execute the following command:

```bash
kubectl apply -f pv.yaml
```

This command will create a PV named `my-pv` with a capacity of 1Gi and a host path of `/mnt/data`.

Next, you will create a PVC that requests 1Gi of storage from the PV.

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
      storage: 1Gi
```

Save the above code in a file named `pvc.yaml` and execute the following command:

```bash
kubectl apply -f pvc.yaml
```

This command will create a PVC named `my-pvc` that requests 1Gi of storage.
