# Move a git repository to subdirectory of another repository
Assume we have two repositories on git, repoA, and repoB, and we want to make repoB a subdirectory of repoA while maintaining its full history after deleting it.

****
## Clone repoA** and **repoB on machine
```
$ git clone repoA
$ git clone repoB
```

## Copy the content of repoB to a new subfolder in repoB except the .git folder
1. cd to folder **repoB** and create a subfolder called **repoB**
```
$ mkdir repoB
```

2. Move everything from the parent **repoB** to the child **repoB**(except the .git folder)
```
$ git stage repoB/
$ git stage README.md
```

3. Commit and push those changes to git
[Difference Between 'git commit -am' and 'git commit -m'](./Advanced_Notes.md)
```
git commit -am '[repoB] Move content to a subfolder'
git push origin master
```

## Merge repoA and repoB
1. Add a remote branch with the content of repoB
```
$ git remote add (create_a_branch_name) (path_to_repoB)
```

2. 

