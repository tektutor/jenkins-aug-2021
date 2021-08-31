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

### Staging a new file
```
cd /home/rps
mkdir GitDemo
cd GitDemo
echo "Apple" > fruits.txt

git add fruits.txt
```

### Commiting the staged files 
```
git commit -m "Initial commit."
```

### Modifying the files in the Git repo
```
echo "Grapes" >> fruits.txt
git add --all
git commit -m "Added Grapes."
```

### Ammending last commit
```
git commit --amend
```
This will let you modify the last commit message or let's modify the file and commit without creating additional commits.


### Listing all the branches in your local git repo
```
git branch
```
Shows all the branches in the repo.  The * represents the active branch.

### Creating a new branch from master branch
```
git checkout -b dev-1.0
```
This will create a new branch by name dev-1.0 and switch to it.

### Switching between branches
```
git checkout master
```
