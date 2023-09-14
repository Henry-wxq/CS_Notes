# Move a git repository to subdirectory of another repository
Assume we have two repositories on git, repoA, and repoB, and we want to make repoB a subdirectory of repoA while maintaining its full history after deleting it.

****
## Clone **repoA** and **repoB** on machine
```
$ git clone repoA
$ git clone repoA
```

## Copy the content of repoB to a new subfolder in repoB except the .git folder
### cd to folder **repoB** and create a subfolder called **repoB/**

