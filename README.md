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

