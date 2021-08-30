### Installing Docker in CentOS
```
sudo yum install -y yum-utils
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce --allowerasing
sudo systemctl enable docker && systemctl start docker
```
For other OS, you may refer the official documentation here https://docs.docker.com/engine/install/

#### Verify if docker command works
```
sudo systemctl status docker 
```

### Finding details about your docker installation
```
docker info
```

### Listing docker images in the local docker registry
```
docker images
```

### Downloading images from Docker Hub Remote Registry
```
docker pull hello-world:latest
docker pull ubuntu:16.04
```

### Deleting unwanted images from local docker registry
```
docker rmi hello-world:latest
```

### Creating containers
```
docker run hello-world:latest
```

### Listing the containers
```
docker ps -a
```

### Listing only running containers
```
docker ps
```

### Creating a ubuntu container interactively
```
docker run -it --name ubuntu1 --hostname ubuntu1 ubuntu:16.04 /bin/bash
```

### Installing ifconfig utility inside container
```
root@ubuntu1:/# apt update && apt install -y net-tools
root@ubuntu1:/# ifconfig
```
The expected output is
<pre>
root@ubuntu1:/# ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:ac:11:00:02  
          inet addr:172.17.0.2  Bcast:172.17.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2877 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2336 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:19712773 (19.7 MB)  TX bytes:130632 (130.6 KB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

root@ubuntu1:/# 
</pre>

### Listing the running containers from another terminal(tab)
```
docker ps
```

### Exiting the container from within interactive container shell
```
root@ubuntu1:/# exit
```

### At this point ubuntu1 container has exited
```
docker ps
```

### Starting the stopped container
```
docker start ubuntu1`
```

### Opening a second shell inside the already running container 
```
docker exec -it ubuntu1 /bin/bash
root@ubuntu1:/# exit
```
Exiting the second shell we launched using the above exec command will not exit the container.

### Stopping a container
```
docker stop ubuntu1
docker stop ubuntu2 ubuntu3
```

### Remove running containers graciously
```
docker stop ubuntu1 
docker rm ubuntu1
```

### Removing containers forcibly
```
docker rm -f ubuntu2
```

### Stopping and Removing multiple containers
```
docker stop $(docker ps -q)
docker rm $(docker ps -aq)
```

### Removing multiple containers abruptly
```
docker rm -f $(docker ps -aq)
```

### Restarting a container
```
docker restart ubuntu1
```
### Installing JDK 11
```
sudo yum install -y java-11-openjdk-devel
```

#### Verify if JDK is installed properly
```
java -version
javac -version
```

### Installing Maven
```
cd ~/Downloads
wget https://mirrors.estointernet.in/apache/maven/maven-3/3.8.2/binaries/apache-maven-3.8.2-bin.tar.gz
tar xvfz apache-maven-3.8.2-bin.tar.gz
```

#### Adding Maven into environment settings
```
cd ~/Downloads
cd apache-maven-3.8.2
pwd
```

### Cloning TekTutor Jenkins repository (Do it as rps user)
```
cd ~
git clone https://github.com/tektutor/jenkins-aug-2021.git
```

### Building Hello java application and run the automated test cases
```
cd jenkins-aug-2021/Day1/Hello
mvn clean test
```

### Set up JFrog artifactory using Docker
```
docker run -d --name artifactory --hostname artifactory -p 8081:8081 jfrog-docker-reg2.bintray.io/jfrog/artifactory-oss:4.1.0
```

#### See if the artifactory container runs properly
```
docker psThis time c1 will be able to ping c2
```
If you are able to see the artifactory container running, you may access the artifactory web page at
http://localhost:8081

Login Credentials
```
User - admin
Password - password
```

### Creating custom network in docker
```
docker network create my-network-1
docker network create my-network-2
```

### Listing docker networks
```
docker network ls
```

### Creating a container c1 and adding the container to our custom network
```
docker run -dit --name c1 --hostname c1 --network my-network-1 ubuntu:16.04 bash
```

### Creating a container c2 and adding the container to our custom network
```
docker run -dit --name c2 --hostname c2 --network my-network-2 ubuntu:16.04 bash
```

### Asci diagram of c1 and c2 
<pre>
+-----------------------------------------+               +-----------------------------------------+
|                                         |               |                                         |
|                                         |               |                                         |
|                                         |               |                                         |
|                                         |               |                                         |
|                                         |               |                                         |
|           +-----------------+           |               |          +-----------------+            |
|           |                 |           |               |          |                 |            |
|           |                 |           |               |          |   Container     |            |
|           |     Container   |           |               |          |      C2         |            |
|           |        C1       |           |               |          |   172.19.0.2    |            |
|           |     172.18.0.2  |           |               |          |                 |            |
|           +-----------------+           |               |          +-----------------+            |
|                                         |               |                                         |
|             172.18.0.0/16               |               |             172.19.0.0/16               |
|             my-network-1                |               |             my-network-2                |
|                                         |               |                                         |
|                                         |               |                                         |
|                                         |               |                                         |
+-----------------------------------------+               +-----------------------------------------+
</pre>

### Get inside c1 shell
```
docker exec -it c1 bash
apt update && apt install -y net-tools iputils-ping
```

### Find the ip address of c1 from within c1 shell
```
hostname -i
```

### Get inside c2 shell in another terminal
```
docker exec -it c2 bash
apt update && apt install -y net-tools iputils-ping
```

### Find the IP address of c2 from within c2
```
hostname -i
```

### Ping c1 from c2
```
ping 172.18.0.2
```
As you can notice, c1 won't be able to ping c2 as they are in two different networks.

### Ping c2 from c1
```
ping 172.19.0.2
```
As you can notice, c2 won't be able to ping c1 as they are in two different networks.

### Now let's connect c1 to my-network-2
```
docker network connect my-network-2 c1
docker inspect c1 | grep IPA
```
Now c1 container will have two IPs as it is connected to two different networks.

### Get inside c1 and verify if c1 can ping c2
```
docker exec -it c1 bash
ping 172.19.0.2
```
This time c1 will be able to ping c2

### Get inside c2 and verify if c2 can ping c1
```
docker exec -it c2 bash
ping 172.19.0.3
```
This time c2 will be able to ping c1
