## Git Commands

### Creating an empty Git Repository in your local system
```
git init
```

### Configuring git in local scope
```
git config --local --user.name "Jeganathan Swaminathan"
git config --local --user.email "mail2jegan@gmail.com"
```
The config file will be saved in the .git folder on the current git repo. The config details are only applied for the local git repo.

### Configuring git in global scope
```
git config --global --user.name "Jeganathan Swaminathan"
git config --global --user.email "mail2jegan@gmail.com"
```
The config file will be saved in the home directory of the user and config details are available for all the Git repos created by the user.

### Configuring git in system scope
```
sudo git config --system --user.name "Jeganathan Swaminathan"
sudo git config --system --user.email "mail2jegan@gmail.com"
```
The config file will be saved in the /etc directory, hence config details are available for all the Git repos created by all users in the system.
