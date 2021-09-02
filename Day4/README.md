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

### Let's create centos1 and centos2 containers to use them as ansible nodes
```
docker run -d --name centos1 --hostname centos1 -p 2003:22 -p 8003:80 tektutor/centos-ansible-node
docker run -d --name centos2 --hostname centos2 -p 2004:22 -p 8004:80 tektutor/centos-ansible-node
```

### Check if the centos1 and centos2 containers are up and running
```
docker ps
```

### See if you can SSH into the centos1 and centos2 containers
```
ssh -p 2003 root@localhost
exit
ssh -p 2004 root@localhost
```
