# Installation Guide - Movie Recommender System

## Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Step 1: Clone the Repository

```bash
git clone https://github.com/TARLAS001/MOVIE-RECOMMONDATION-USING-MACHINE-LEARNING.git
cd MOVIE-RECOMMONDATION-USING-MACHINE-LEARNING
```

## Step 2: Create Virtual Environment

### On Windows (Git Bash)
```bash
python -m venv venv
source venv/Scripts/activate
```

### On macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Download Required Data

The TMDB 5000 dataset is required to generate model files:
- Download from: https://www.kaggle.com/tmdb/tmdb-movie-metadata
- Extract to `data/` folder

## Step 5: Generate Model Files

Run the Jupyter notebook to generate artifacts:
```bash
jupyter notebook "Movie Recommender System Data Analysis.ipynb"
```

This will create:
- `artifacts/movie_dict.pkl`
- `artifacts/similarity.pkl`

## Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

## Troubleshooting

### Issue: Module not found
**Solution:** Ensure virtual environment is activated
```bash
which python  # Should show path inside venv folder
```

### Issue: Data files missing
**Solution:** Download TMDB dataset and extract to `data/` folder

### Issue: TMDB API errors
**Solution:** Verify internet connection and API key in `app.py`

## Next Steps

- Explore movie recommendations
- Modify the recommendation algorithm
- Deploy to cloud platform (Heroku, AWS, etc.)
