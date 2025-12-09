# Hate Speech & Offensive Language Classification

This project implements a transformer-based classifier (BERT) to detect hate speech, offensive language, and neutral content in tweets. It supports both multiclass and binary classification modes.

## Requirements

- Python 3.8+
- pip

### Python Packages
- torch
- transformers
- datasets
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- tqdm

You can install all requirements with:

```bash
pip install torch transformers datasets scikit-learn pandas numpy matplotlib seaborn tqdm
```

## Data
- Place your dataset as `data/labeled_data.csv` (should have columns: `class`, `tweet`)

## How to Run

1. **Open the notebook**
   - Open `FINAL_Hate_MultiClass_GentleNLP.ipynb` in Jupyter or VS Code.

2. **Run all cells**
   - The notebook will:
     - Load and preprocess the data
     - Train a BERT classifier (multiclass and binary)
     - Evaluate and print metrics
     - Show error analysis and sample predictions

## Project Structure

- `FINAL_Hate_MultiClass_GentleNLP.ipynb` — Main notebook with all code and analysis
- `data/labeled_data.csv` — Input data (not included)
- `README.md` — This file

## Notes
- GPU is recommended for faster training, but the code will run on CPU as well.
- The notebook includes both multiclass (hate speech, offensive, neither) and binary (harmful vs not harmful) classification.
- Results and error analysis are printed at the end of the notebook.

## Authors
- Claire Lynch
- Jose Santiago Campa Morales