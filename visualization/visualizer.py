from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

def plot_data(file_path):
    data = pd.read_csv(file_path)
    if 'Summary' in data.columns:
        text = ' '.join(data['Summary'])
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Most Common Keywords')
        plt.show()
    elif 'Price' in data.columns:
        plt.figure(figsize=(10, 5))
        data = data.dropna()
        plt.bar(data['Product Name'], data['Price'].apply(lambda x: float(x.replace('$', '').replace(',', ''))))
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Product Name')
        plt.ylabel('Price ($)')
        plt.title('Product Price Comparison')
        plt.tight_layout()
        plt.show()
