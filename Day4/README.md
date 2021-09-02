### Building Custom CentOS Ansible Node image
```
cd ~/Training/jenkins-aug-2021
git pull
cd Day4/centos-ansible
cp /home/rps/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/centos-ansible-node .
```
The above steps assume you already have created ssh key pairs, if not you need to create key pairs for rps user before trying the above commands.

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

### Try ssh into centos1
```
ssh -p 2003 root@localhost
```
The expected output is
<pre>
[jegan@localhost jenkins-aug-2021]$ ssh -p 2003 root@localhost
The authenticity of host '[localhost]:2003 ([::1]:2003)' can't be established.
ECDSA key fingerprint is SHA256:/A4sdguLI6swqmiYWS7JKBZy9Fk4LYEpJ+JduvxIOh0.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2003' (ECDSA) to the list of known hosts.
Last login: Thu Sep  2 05:13:43 2021 from 172.17.0.1
[root@centos1 ~]# exit
logout
Connection to localhost closed.
[jegan@localhost jenkins-aug-2021]$ 
</pre>

### Try ssh into centos2
```
ssh -p 2004 root@localhost
```
The expected output is
<pre>
[jegan@localhost jenkins-aug-2021]$ ssh -p 2004 root@localhost
The authenticity of host '[localhost]:2004 ([::1]:2004)' can't be established.
ECDSA key fingerprint is SHA256:/A4sdguLI6swqmiYWS7JKBZy9Fk4LYEpJ+JduvxIOh0.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2004' (ECDSA) to the list of known hosts.
Last login: Thu Sep  2 05:03:52 2021 from 172.17.0.1
[root@centos2 ~]# exit
logout
Connection to localhost closed.
</pre>

### In case you were not able to SSH into centos1, you may troubleshoot 
```
docker logs centos1
docker exec -it centos1 bash
```

### Ansible configuration file
- All ansible configurations are captures in a file called ansible.cfg.
- ansible.cfg could be maintained in multiple locations
    - ANSIBLE_CONFIG environment variable could be used to point to the ansible.cfg file kept at any locations that is accessible.
    - Current directory
    - Home directory of the user who runs the ansible ad-hoc/playbooks
    - /etc/ansible/ansible.cfg 
- Ansible looks for ansible.cfg file in the order listed above and whichever is found first it picks it
- this file can be used to configure the hosts file ansible should be using, enable/disable logs, configures timeouts, configure how many parallel connections ansible should make to ansible nodes,etc

### In case you have configured inventory path in ansible.cfg, you may run ad-hoc or playbooks as shown below
```
ansible all -m ping
ansible-playbook your-playbook.yml
```

### Understanding Ansible recommended directory structure
```
cd ~/Training/jenkins-aug-2021
git pull
cd Day4/Ansible/AnsibleRecommendedDirStructure
ansible all -m ping
```

### Try install nginx playbook on ubuntu and centos ansible nodes
```
cd ~/Training/jenkins-aug-2021
git pull
cd Day4/Ansible/before-refactoring
ansible-playbook install-nginx-playbook.yml
```

### Executing the refactored install nginx playbook
```
cd ~/Training/jenkins-aug-2021
git pull
cd Day4/Ansible/after-refactoring
ansible-playbook install-nginx-playbook.yml
```

### Executing provision docker container playbook
```
cd ~/Training/jenkins-aug-2021
git pull
cd Day4/Loops
ansible-playbook provision-containers-playbook.yml -K
```

In the above command, -K will ask for become password i.e root password of rps user.  This is required as we running the playbook on localhost as non-admin user, but we are trying to install softwares.
