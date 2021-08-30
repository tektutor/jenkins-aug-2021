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

### Listing the running containers 
```
docker ps
```
