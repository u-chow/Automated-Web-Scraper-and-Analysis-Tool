import pandas as pd
from collections import Counter

def analyze_data(file_path):
    data = pd.read_csv(file_path)
    if 'Summary' in data.columns:
        text = ' '.join(data['Summary'])
        words = text.split()
        common_words = Counter(words).most_common(20)
        print("Top 20 Keywords:")
        for word, count in common_words:
            print(f"{word}: {count}")
    elif 'Price' in data.columns:
        print(data[['Product Name', 'Price']])
    else:
        print("No valid data to analyze.")
