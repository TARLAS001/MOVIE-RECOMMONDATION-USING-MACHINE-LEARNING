# Complete Git Workflow Setup Guide
## Movie Recommender System Using Machine Learning

### Prerequisites
- Git Bash installed on Windows
- GitHub account
- Repository URL ready (you'll provide this)

---

## PHASE 1: CHECK & INITIALIZE GIT

### Step 1.1: Navigate to Project Directory
```bash
cd /c/path/to/MOVIE-RECOMMONDATION-USING-MACHINE-LEARNING
# Example: cd /c/Users/TARLAS001/Documents/projects/MOVIE-RECOMMONDATION-USING-MACHINE-LEARNING
```
**What it does:** Changes directory to your project folder

---

### Step 1.2: Check if Git is Initialized
```bash
git status
```
**What it does:** 
- If repo exists: Shows current branch and status
- If not initialized: Shows "fatal: not a git repository" error

---

### Step 1.3: Initialize Git (Only if NOT Already Initialized)
```bash
git init
```
**What it does:** Creates a `.git` folder in your project directory. This makes it a Git repository.

**WARNING:** Only run this if `git status` returned an error in Step 1.2

---

## PHASE 2: CONFIGURE GIT USER

### Step 2.1: Set Your Git User Name
```bash
git config user.name "TARLAS001"
```
**What it does:** Configures the name to be used in commits

---

### Step 2.2: Set Your Git Email
```bash
git config user.email "your-email@example.com"
```
**What it does:** Configures the email to be used in commits
**Replace:** `your-email@example.com` with your actual GitHub email

---

## PHASE 3: VERIFY & UPDATE .gitignore

### Step 3.1: Check Current .gitignore
```bash
cat .gitignore
```
**What it does:** Displays the current contents of .gitignore

---

### Step 3.2: Verify These Entries Exist (Should Already Be There)
The .gitignore should contain:
```
# Python
__pycache__/
*.py[cod]
*.egg-info/
.Python
build/
dist/
*.egg

# Jupyter
.ipynb_checkpoints/

# Environment
.env
.venv
venv/

# IDE
.vscode/
.idea/

# Project Specific
artifacts/
data/
configs/secrets.yaml
```

---

## PHASE 4: CHECK WHAT WILL BE COMMITTED

### Step 4.1: See All Untracked and Modified Files
```bash
git status
```
**What it does:** Shows which files are staged, unstaged, and untracked

---

### Step 4.2: See Detailed Changes
```bash
git diff --name-only
```
**What it does:** Shows files with changes (not staged yet)

---

## PHASE 5: STAGE FILES

### Step 5.1: Stage All Required Files
```bash
git add app.py README.md requirements.txt setup.py setup.sh "Movie Recommender System Data Analysis.ipynb"
```
**What it does:** Stages specific files for commit
**Files included:**
- ✅ app.py (Streamlit application)
- ✅ README.md (Documentation)
- ✅ requirements.txt (Dependencies)
- ✅ setup.py (Package setup)
- ✅ setup.sh (Shell script)
- ✅ Jupyter notebook (Data analysis)

**Files excluded (staying in git):**
- ❌ artifacts/ (Generated model files)
- ❌ data/ (Raw data files)
- ❌ configs/secrets.yaml (Secrets)

---

### Step 5.2: Verify Staged Files
```bash
git status
```
**What it does:** Shows which files are staged and ready to commit

---

## PHASE 6: CREATE COMMIT

### Step 6.1: Commit with Professional Message
```bash
git commit -m "feat: Initialize Movie Recommender System project with core files

- Add Streamlit web application (app.py) with movie recommendation engine
- Add data processing notebook for model training using cosine similarity
- Add requirements.txt with dependencies (streamlit, scikit-learn, nltk, pandas)
- Add setup.py and setup.sh for project configuration
- Add comprehensive README with project details, workflow, and setup instructions
- Initialize project structure for content-based movie recommendation system

Technologies: Python 3.7+, Streamlit, scikit-learn, TMDB API
Dataset: TMDB 5000 Movies & Credits from Kaggle
Recommendation Method: Cosine Similarity"
```

**What it does:** Creates a commit with a detailed, professional message explaining all changes

---

## PHASE 7: CONNECT TO GITHUB

### Step 7.1: Add Remote Repository
```bash
git remote add origin https://github.com/TARLAS001/MOVIE-RECOMMONDATION-USING-MACHINE-LEARNING.git
```
**What it does:** Connects your local repo to the GitHub repository
**Replace:** The URL with your actual GitHub repository URL

---

### Step 7.2: Verify Remote Connection
```bash
git remote -v
```
**What it does:** Shows the remote repository URLs configured

---

## PHASE 8: PUSH TO GITHUB

### Step 8.1: Push to Main Branch
```bash
git branch -M main
git push -u origin main
```
**What it does:** 
- Renames current branch to "main" (if needed)
- Pushes commits to GitHub main branch
- `-u` flag sets this as the default upstream branch

---

### Step 8.2: Verify Push Success
```bash
git log --oneline -5
```
**What it does:** Shows the last 5 commits to verify push worked

---

## PHASE 9: TROUBLESHOOTING

### Issue: Authentication Failed
**Solution:** Set up SSH or Personal Access Token (PAT)

**For HTTPS with PAT:**
```bash
# Update remote URL
git remote set-url origin https://YOUR_USERNAME:YOUR_PAT@github.com/TARLAS001/MOVIE-RECOMMONDATION-USING-MACHINE-LEARNING.git
```

**For SSH:**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your-email@example.com"

# Update remote URL
git remote set-url origin git@github.com:TARLAS001/MOVIE-RECOMMONDATION-USING-MACHINE-LEARNING.git
```

---

### Issue: Branch Conflicts
**Solution:**
```bash
git pull origin main --rebase
git push -u origin main
```

---

### Issue: Changes Already on Remote
**Solution:**
```bash
git pull origin main
git push origin main
```

---

## PHASE 10: BEST PRACTICES FOR FUTURE DEVELOPMENT

### 1. Create Feature Branches
```bash
git checkout -b feature/new-feature-name
# Do your work
git add .
git commit -m "feat: add new feature"
git push origin feature/new-feature-name
```

### 2. Pull Before Starting Work
```bash
git pull origin main
```

### 3. Keep Commits Atomic
Each commit should represent one logical change

### 4. Write Descriptive Commit Messages
```
feat: Add new feature
fix: Fix bug in X
docs: Update README
refactor: Refactor Y
```

### 5. Review Changes Before Committing
```bash
git diff
git diff --cached
```

### 6. Protect Main Branch
- Set branch protection rules on GitHub
- Require pull requests for changes
- Require code reviews

### 7. Use .gitignore Effectively
```bash
# Never commit:
- API keys / secrets
- Large model files (> 100MB)
- Generated cache files
- Personal configuration files
- Data files (use DVC instead for large data)
```

---

## QUICK REFERENCE COMMANDS

```bash
# Status and logs
git status                    # See current status
git log --oneline             # See commit history
git diff                      # See unstaged changes
git diff --cached             # See staged changes

# Staging and committing
git add <file>               # Stage specific file
git add .                    # Stage all changes
git commit -m "message"      # Commit with message
git reset <file>             # Unstage file

# Branching
git branch                   # List branches
git checkout -b <branch>     # Create and switch to branch
git checkout <branch>        # Switch to branch
git merge <branch>           # Merge branch into current

# Remote operations
git push origin <branch>     # Push to remote
git pull origin <branch>     # Pull from remote
git fetch origin             # Fetch updates without merging

# Undo changes
git restore <file>           # Discard changes in file
git restore --staged <file>  # Unstage file
git reset --hard HEAD~1      # Undo last commit (⚠️ DESTRUCTIVE)
```

---

## NEXT STEPS

1. Copy and execute the commands in order (PHASE 1 through PHASE 8)
2. Provide your GitHub repository URL when prompted
3. Monitor each step for errors
4. Contact support if issues arise during authentication or push

**Good luck! 🚀**
