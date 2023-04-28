# Creating a New User Group

## Introduction

One of the most important tasks for a Linux administrator is to manage user groups. By creating groups, you can assign permissions and privileges to multiple users at once. In this step, you will learn how to create a new user group.

## Target

Your task is to create a new user group called `sales`.

## Result Example

You can use the `getent group sales` command to check if it was created successfully.

```bash
sales:x:1001:
```

## Requirements

- You must have administrative privileges to create a new group.
- If the group already exists, the command will display an error message.
