### Building a custom Ubuntu Ansible Node Docker Image

#### Let's create key pair for rps user
```
ssh-keygen
```
You may accept all defaults by hitting enter thrice :)

#### Building ansible ubuntu image
```
cd ~/jenkins-aug-2021
git pull
cd Day3/ubuntu-ansible
cp /home/rps/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/ansible-ubuntu-node .
```

#### Verify if the newly built image is listed
```
docker images
```








