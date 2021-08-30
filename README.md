### Installing Docker
```
sudo yum install -y yum-utils
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce --allowerasing
sudo systemctl enable docker && systemctl start docker

```

#### Verify if docker command works
```
sudo systemctl status docker 

```
