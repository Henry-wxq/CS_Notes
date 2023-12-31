# Move a git repository to subdirectory of another repository
Assume we have two repositories on git, repoA, and repoB, and we want to make repoB a subdirectory of repoA while maintaining its full history after deleting it.

****
## Steps
- [ ] Clone repoA** and **repoB on machine
- [ ] Copy the content of repoB to a new subfolder in repoB except the .git folder
- [ ] Merge repoA and repoB
- [ ] Check whether all histories are kept
- [x] References 

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
[Difference Between 'git commit -am' and 'git commit -m'](./2_Advanced_Notes.md)
```
git commit -am '[repoB] Move content to a subfolder'
git push origin master
```

## Merge repoA and repoB
1. Add a remote branch with the content of repoB
[Note for 'git remote add'](../Notes/1_Basic_Notes.md)
```
$ git remote add (create_a_branch_name) (path_to_repoB)
```
 * For Example:
```
git remote add repoB_origin git@github.com:Henry-wxq/Git_Study.git
```

2. Pull the **repoA** maintaining its history
[Note for --allow-unrelated-histories](../Notes/2_Advanced_Notes.md)
```
git pull (created_branch_name) (merged_to_branch_name) --allow-unrelated-histories
```
  * For Example:
```
git pull repoB_origin master --allow-unrelated-histories
```

4. Exit the vim

  * Directly type :wq

3. Delete the remote **repoB_origin**
```
git remote rm (created_branch_name)
```
  * For Example:
```
git remote rm repoB_origin
```

4. Check whether successfully remove the branch
```
git remote -vv
```

5. Push the changes to the server
```
git push origin master
```

## Check whether all histories are kept
![Check](https://github.com/Henry-wxq/Pictures/blob/main/Coding_Pic/git-log.png)

## References
* [Merge Unrelated Histories](https://stackoverflow.com/questions/45272492/git-is-refusing-to-merge-unrelated-histories-what-are-unrelated-histories)
* [Moving Repo](https://ahmadatwi.me/2016/04/07/how-to-move-a-git-repository-to-subdirectory-of-another-repository/comment-page-1/)



