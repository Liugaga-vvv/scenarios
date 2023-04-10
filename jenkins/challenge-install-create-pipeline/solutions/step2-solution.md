# Note

- Input `groupadd tomcat` command to create a new user group
- Input `useradd -g tomcat -d /opt/tomcat tomcat` command to create a new user
- Input `wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.73/bin/apache-tomcat-9.0.73.tar.gz` command to download `tomcat 9` archive
- Input `tar -xvzf apache-tomcat-9.0.70.tar.gz -C /opt/tomcat --strip-components 1` command to untar the archive and change the name
- Input `chown -R tomcat:tomcat /opt/tomcat` command to change the owner of a directory
