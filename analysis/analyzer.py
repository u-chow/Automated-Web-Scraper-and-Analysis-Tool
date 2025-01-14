# analysis/analyzer.py
import pandas as pd

def analyze_data(file_path):
    data = pd.read_csv(file_path)
    summary = data.describe()
    print(summary)
    return summary
