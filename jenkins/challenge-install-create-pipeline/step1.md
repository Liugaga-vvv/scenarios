# Install JDK

## Introduction

Jenkins is developed in Java, so its runtime environment requires JDK.

There are various ways to install JDK, such as binary installation, source package installation, etc. Since our challenge environment is Ubuntu, which has java repositories, it is easiest to install directly using the apt command.

## Target

Your goal is to follow `JDK11` and configure the `JAVA_HOME` environment variable on Ubuntu OS.

## Result Example

Here's an example of what you should be able to accomplish by the end of this challenge:

1. Update the Ubuntu package list.
   ![challenge-install-create-pipeline-1-2](assets/challenge-install-create-pipeline-1-2.png)

2. Install the OpenJDK 11.
   ![challenge-install-create-pipeline-1-3](assets/challenge-install-create-pipeline-1-3.png)

3. Find out where apt installed `Java` on Ubuntu.
   ![challenge-install-create-pipeline-1-4](assets/challenge-install-create-pipeline-1-4.png)

4. With the location of the Java installs on the clipboard, open up the server’s environment file with vim.
   ![challenge-install-create-pipeline-1-5](assets/challenge-install-create-pipeline-1-5.png)

5. Force the Ubuntu terminal to reload the environment configuration file.

   ```bash
   source /etc/environment
   ```

6. Be able to echo the `JAVA_HOME` environment variable in an Ubuntu terminal window.
   ![challenge-install-create-pipeline-1-6](assets/challenge-install-create-pipeline-1-6.png)

## Requirements

To complete this lab, you will need:

- Ubuntu operating system installed.
- A user account with administrator privileges.
- Access to the Internet.
