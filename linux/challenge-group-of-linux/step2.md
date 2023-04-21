# Adding Users to a Group

## Introduction

Once you have created a new user group, the next step is to add users to the group. By doing this, you can grant permissions and privileges to multiple users at once. In this step, you will learn how to add users to a user group.

## Target

Your task is to add two users, `john` and `jane`, to the `sales` group.

## Result Example

```bash
uid=1007(john) gid=1009(john) groups=1009(john),1008(sales)
uid=1008(jane) gid=1010(jane) groups=1010(jane),1008(sales)
```

## Requirements

- You must have administrative privileges to add users to a group.
- The users must already exist on the system.
