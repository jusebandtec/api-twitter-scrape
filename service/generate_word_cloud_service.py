from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import csv

class GenerateWordCloudService:

    def __init__(self, file_name_csv) -> None:
        self.file_name_csv = file_name_csv
        pass

    def generate(self):
        data = pd.read_csv(self.file_name_csv)
        stopwords = set(STOPWORDS)
        wordcloud = WordCloud(background_color='white', stopwords=stopwords, max_words=200, max_font_size=40, random_state=42).generate(str(data['tweet']))
        
        fig = plt.figure(1)
        plt.imshow(wordcloud)
        plt.axis('off')
        fig.savefig("word_cloud.png", dpi=900)
