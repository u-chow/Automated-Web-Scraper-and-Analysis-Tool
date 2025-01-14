# visualization/visualizer.py
import matplotlib.pyplot as plt
import pandas as pd

def plot_data(file_path, column):
    data = pd.read_csv(file_path)
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data[column])
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.title(f'{column} Trend Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
