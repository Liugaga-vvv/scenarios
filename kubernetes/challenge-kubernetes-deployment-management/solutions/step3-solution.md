# Note

1. Use `kubectl rollout history deployment helloworld` command to list the historical versions of hello-world.
2. Use `kubectl rollout history deployment helloworld --revision=1` command to check the first version for more information.
3. Use `kubectl rollout undo deployment helloworld --to-revision=1` command to rollback the hello-world deployment to the previous revision.
