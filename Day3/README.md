### For cloning this repository
```
cd /home/rps
mkdir Training
cd Training
git clone https://github.com/tektutor/jenkins-aug-2021.git
```

### Building a custom Ubuntu Ansible Node Docker Image

#### Let's create key pair for rps user
```
ssh-keygen
```
You may accept all defaults by hitting enter thrice :)

#### Building ansible ubuntu image
```
cd ~/Training/jenkins-aug-2021
git pull
cd Day3/ubuntu-ansible
cp /home/rps/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/ansible-ubuntu-node .
```

### Let's remove the existing containers
```
docker rm -f $(docker ps -aq)
```

#### Verify if the newly built image is listed
```
docker images
```
The output should show tektutor/ansible-ubuntu-node docker image <b>highlighted</b> below
<pre>
[jegan@localhost jenkins-aug-2021]$ docker images
REPOSITORY                                           TAG       IMAGE ID       CREATED          SIZE
<b>
tektutor/ubuntu-ansible-node                         latest    009afa27da10   11 minutes ago   220MB
</b>
ubuntu                                               16.04     38b3fa4640d4   5 weeks ago      135MB
hello-world                                          latest    d1165f221234   5 months ago     13.3kB
jfrog-docker-reg2.bintray.io/jfrog/artifactory-oss   4.1.0     c5f6c78afc2b   5 years ago      409MB
</pre>

### Let us create two ubuntu ansible node containers
```
docker run -dit --name ubuntu1 --hostname ubuntu1 -p 2001:22 -p 8001:80 tektutor/ubuntu-ansible-node
docker run -dit --name ubuntu2 --hostname ubuntu2 -p 2002:22 -p 8002:80 tektutor/ubuntu-ansible-node
```
#### Verify if you can see ubuntu1 and ubuntu2 containers
```
docker ps
```
The expected output is
<pre>
jegan@localhost jenkins-aug-2021]$ docker ps
CONTAINER ID   IMAGE                          COMMAND               CREATED          STATUS          PORTS                                                                          NAMES
a8a4985cf4ab   tektutor/ubuntu-ansible-node   "/usr/sbin/sshd -D"   2 seconds ago    Up 1 second     0.0.0.0:2002->22/tcp, :::2002->22/tcp, 0.0.0.0:8002->80/tcp, :::8002->80/tcp   ubuntu2
d65dfee152f4   tektutor/ubuntu-ansible-node   "/usr/sbin/sshd -D"   14 seconds ago   Up 13 seconds   0.0.0.0:2001->22/tcp, :::2001->22/tcp, 0.0.0.0:8001->80/tcp, :::8001->80/tcp   ubuntu1
</pre>

#### Let's connect to ubuntu1 container via ssh
```
ssh -p 2001 root@localhost
```
The expected output is
<pre>
jegan@localhost jenkins-aug-2021]$ ssh -p 2001 root@localhost
The authenticity of host '[localhost]:2001 ([::1]:2001)' can't be established.
ECDSA key fingerprint is SHA256:N0vrrubppNsnIjJjgOYtYMdmimP3v+O6nAFTajwiahw.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2001' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.18.0-305.12.1.el8_4.x86_64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@ubuntu1:~# exit
logout
</pre>

#### Let's connect to ubuntu2 container via ssh
```
ssh -p 2002 root@localhost
```
The expected output is
<pre>
[jegan@localhost jenkins-aug-2021]$ ssh -p 2002 root@localhost
The authenticity of host '[localhost]:2002 ([::1]:2002)' can't be established.
ECDSA key fingerprint is SHA256:N0vrrubppNsnIjJjgOYtYMdmimP3v+O6nAFTajwiahw.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2002' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.18.0-305.12.1.el8_4.x86_64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@ubuntu2:~# exit
logout
</pre>


### Ping the ansible nodes ubuntu1 and ubuntu2 using Ansible ad-hoc command
```
cd ~/Training/jenkins-aug-2021
git pull
cd Day3/Ansible
ansible -i hosts all -m ping
```
The expected output is
<pre>
[jegan@localhost Ansible]$ ansible -i hosts all -m ping
ubuntu1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
ubuntu2 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
</pre>

### What happens when we do ansible ping
1. Ansible picks the connection details of ansible nodes from the inventory file
2. Using the connections details ansible does a SSH connection to all the machines in the inventory
3. Ansible creates tmp directory on all Ansible Nodes
4. Ansible also creates a tmp directory on the Ansible Controller Machine
5. Ansible copies the ping.py from the ansible module directory and puts them in the Ansible Controller Machine's tmp folder
6. Ansible then copies all the ansible specific imports in the ping.py and pastes the code inline in the ping.py on the ACM
7. Using sftp/scp Ansible copies the transpiled ping.py from ACM and puts them on the Ansible node tmp folder
8. Ansible gives execute permission to the ping.py file on the Ansible nodes
9. Ansible execute the ping.py python script on the Ansible node using /usr/bin/python
10. Ansible records the output of the ping.py script and cleans up the tmp folder on the Ansible nodes 
11. Ansible gives a summary of output on the Ansible Controller Machine(ACM).


### Ansible Playbook Structure
1. Ansible playbook is a YAML file with extension yaml or yml
2. Each Ansible playbook may have one or more Play
3. Each Play will have a hosts section that targets one or more servers(ansible nodes)
4. Each Play may have an optional list of tasks under tasks section
5. Each Play may have an optional list of roles under roles section
6. Each Task under a Play can invoke at the most one Ansible Module(Python script in case of Unix/Linux or Powershell scripts in case of Windows Ansible Nodes)


### Running the ping-playbook
```
cd ~/Training/jenkins-aug-2021
git pull
cd Day3/Ansible
ansible-playbook -i hosts ping-playbook.yml
```
