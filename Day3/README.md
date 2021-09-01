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
The output should show tektutor/ansible-ubuntu-node docker image
<pre>
[jegan@localhost jenkins-aug-2021]$ docker images
REPOSITORY                                           TAG       IMAGE ID       CREATED          SIZE
tektutor/ubuntu-ansible-node                         latest    009afa27da10   11 minutes ago   220MB
ubuntu                                               16.04     38b3fa4640d4   5 weeks ago      135MB
hello-world                                          latest    d1165f221234   5 months ago     13.3kB
xebialabs/xl-release                                 8.2       95a054bc36b1   2 years ago      450MB
jfrog-docker-reg2.bintray.io/jfrog/artifactory-oss   4.1.0     c5f6c78afc2b   5 years ago      409MB
</pre>







