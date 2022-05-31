import csv
from distutils.log import error

class CSVTweets:

    def __init__(self, tweets) -> None:
        self.tweets = tweets

    def write(self, name_file):
        
        with open(f"{name_file}.csv", 'w') as f:
            try:
                w = csv.writer(f)
                w.writerow(("name", "tweet", "source", "criado_em", "likes", "retweets"))
                for tweet in self.tweets:
                    w.writerow((tweet.name, tweet.tweet, tweet.source, tweet.criado_em, tweet.likes, tweet.retweets))
                print("Arquivo salvo com sucesso")
            except Exception as ex:
                raise error("Erro ao salvar arquivo.", ex)
