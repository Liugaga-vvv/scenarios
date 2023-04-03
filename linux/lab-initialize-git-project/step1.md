# Using Git Init to Create a New Repository

> Tips: before we get started, make sure you have Git installed on your system. If you haven't already installed it, you can download and install it from the [official website](https://git-scm.com/downloads).

To create a new Git repository using the `git init` command, follow these steps:

1. Open your terminal or command prompt and navigate to the `~/myrepo` directory where you want to create the repository.
2. Run the following command to initialize a new Git `git init`.
   This will create a new `.git` directory in your current directory, which is where Git will store all the meta-data and version history for your project.
3. You can now start adding files and committing changes to your repository. Here's an example that create a new file to the Workspace, add it to the Index, and commit it to the Repository.

```bash
touch README.md

# Add the file to the repository
git add README.md

# Commit the changes with a message
git commit -m "Initial commit"
```

Congratulations! You have now created a new Git repository using the `git init` command.
