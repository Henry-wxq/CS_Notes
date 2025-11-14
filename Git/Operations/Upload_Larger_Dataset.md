To upload a dataset larger than **100 MB** to a GitHub repository, you **cannot** push it directly because GitHub blocks files >100 MB.
Instead, you have **three correct options**:

---

# **Option 1 — Use Git LFS (Large File Storage) (Most Common)**

Git LFS is the standard solution for large files.

### **Step 1: Install Git LFS**

Mac:

```bash
brew install git-lfs
```

Windows:

```bash
git lfs install
```

Then initialize it:

```bash
git lfs install
```

---

### **Step 2: Track your large dataset file**

Example: your file is `dataset.csv`

```bash
git lfs track "*.csv"
```

This creates a `.gitattributes` file automatically.

Commit it:

```bash
git add .gitattributes
git commit -m "Track large CSV using Git LFS"
```

---

### **Step 3: Add and push your dataset**

```bash
git add dataset.csv
git commit -m "Add dataset via Git LFS"
git push
```

Files **larger than 100MB** are now stored in LFS, not regular Git.
Free Git LFS storage = **1 GB**, bandwidth = **1 GB/month**.



