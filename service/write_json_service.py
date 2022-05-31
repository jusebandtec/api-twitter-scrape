import json
import datetime

class CreateJsonService:

    def __init__(self, tweets = None, analise = None) -> None:
        self.mytweets = tweets
        self.analise = analise

    
    def write(self, nome_arquivo):
        tweets_dict = [tweet._asdict() for tweet in self.mytweets]
        with open(nome_arquivo, 'w') as j:
            json.dump(tweets_dict, j, ensure_ascii=False, cls=DateTimeEncoder)
    
    def write_analise(self):
        with open("analise.json", 'w') as j:
            json.dump(self.analise, j, ensure_ascii = False)
    
class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)