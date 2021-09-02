### Building Custom CentOS Ansible Node image
```
cd ~/Training/jenkins-aug-2021
git pull
cd Day4/centos-ansible
cp /home/rps/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/centos-ansible-node .
```

### List and see if the new docker image shows up
```
docker images
```
The expected output is
<pre>
REPOSITORY                                           TAG       IMAGE ID       CREATED         SIZE
<b>tektutor/centos-ansible-node                         latest    fb40ae31dd0e   9 minutes ago   257MB</b>
tektutor/ubuntu-ansible-node                         latest    009afa27da10   23 hours ago    220MB
ubuntu                                               16.04     38b3fa4640d4   5 weeks ago     135MB
hello-world                                          latest    d1165f221234   6 months ago    13.3kB
centos                                               8         300e315adb2f   8 months ago    209MB
xebialabs/xl-release                                 8.2       95a054bc36b1   2 years ago     450MB
jfrog-docker-reg2.bintray.io/jfrog/artifactory-oss   4.1.0     c5f6c78afc2b   5 years ago     409MB
</pre>

### Let's create centos1 and centos2 containers to use them as ansible nodes
```
docker run -d --name centos1 --hostname centos1 -p 2003:22 -p 8003:80 tektutor/centos-ansible-node
docker run -d --name centos2 --hostname centos2 -p 2004:22 -p 8004:80 tektutor/centos-ansible-node
```

### Check if the centos1 and centos2 containers are up and running
```
docker ps
```
The expected output is
<pre>
[jegan@localhost jenkins-aug-2021]$ docker ps
CONTAINER ID   IMAGE                                 COMMAND               CREATED         STATUS         PORTS                                                                          NAMES
<b>
f583f8e085c1   tektutor/centos-ansible-node:latest   "/usr/sbin/sshd -D"   8 minutes ago   Up 8 minutes   0.0.0.0:2004->22/tcp, :::2004->22/tcp, 0.0.0.0:8004->80/tcp, :::8004->80/tcp   centos2
c520941d56fd   tektutor/centos-ansible-node:latest   "/usr/sbin/sshd -D"   8 minutes ago   Up 8 minutes   0.0.0.0:2003->22/tcp, :::2003->22/tcp, 0.0.0.0:8003->80/tcp, :::8003->80/tcp   centos1</b>
a8a4985cf4ab   tektutor/ubuntu-ansible-node          "/usr/sbin/sshd -D"   22 hours ago    Up 8 minutes   0.0.0.0:2002->22/tcp, :::2002->22/tcp, 0.0.0.0:8002->80/tcp, :::8002->80/tcp   ubuntu2
d65dfee152f4   tektutor/ubuntu-ansible-node          "/usr/sbin/sshd -D"   22 hours ago    Up 8 minutes   0.0.0.0:2001->22/tcp, :::2001->22/tcp, 0.0.0.0:8001->80/tcp, :::8001->80/tcp   ubuntu1
</pre>

### See if you can SSH into the centos1 and centos2 containers
```
ssh -p 2003 root@localhost
exit
ssh -p 2004 root@localhost
```
