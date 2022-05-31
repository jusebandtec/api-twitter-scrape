from domain.scrape import Scrape
from service.save_csv_tweets_service import CSVTweets
from service.generate_word_cloud_service import GenerateWordCloudService
from service.tratar_tweeter_service import TratarTweeterService
from service.write_json_service import CreateJsonService
from collections import namedtuple

scrape = Scrape().initialize()

print("Resgatando todos os tweets que contém PIX")
tweets = scrape.get_tweets_from_words()
tweets_tratados = []
palavras = []
tratar_tweet_service = TratarTweeterService()
tweets_tagged = []


for tweet in tweets:
    tweeter_tratado, tweeter_tagged = TratarTweeterService(dados_tweeter = tweet).tokenizar_dados_tweeter().posicionar_tags().remover_preposicoes_adverbios_dois_pontos_virgula()
    tweets_tagged.append(tweeter_tagged)
    tweets_tratados.append(tweet._replace(tweet = tweeter_tratado))
    count_bancos = tratar_tweet_service.count_words_bank(tweeter_tagged)
    palavras.append(count_bancos)



analise = {
    "count_words_pix": 0,
    "count_words_c6": 0,
    "count_words_nubank": 0,
    "count_words_safra": 0,
    "count_words_santander": 0,
    "count_words_inter": 0,
}

for analisado in palavras:
    analise["count_words_pix"] += analisado.count_word_pix 
    analise["count_words_c6"] += analisado.count_word_c6 
    analise["count_words_nubank"] += analisado.count_word_nubank 
    analise["count_words_safra"] += analisado.count_word_safra 
    analise["count_words_inter"] += analisado.count_word_inter 
    analise["count_words_santander"] += analisado.count_word_santander 

json_write_analise = CreateJsonService(analise = [analise, tratar_tweet_service.count_words(tweets_tagged)])
json_write_analise.write_analise()

resposta_write_csv = input("Gostarai de salvar em um arquivo JSON? [S/N] ")
if resposta_write_csv.lower() == 's':
    nome_arquivo = input('digite o nome do arquivo:\n> ')
    nome_arquivo = f'{nome_arquivo}.json' if nome_arquivo.find('.json') < 0 else nome_arquivo
    json_write = CreateJsonService(tweets_tratados)
    json_write.write(nome_arquivo)
    csv = CSVTweets(tweets = tweets_tratados)
    csv.write(nome_arquivo)
    resposta_generate_world_cloud = input("Gostaria de gerar uma nuvem de palavras? [S/N] ")
    if resposta_generate_world_cloud.lower() == 's':
        word_cloud = GenerateWordCloudService(nome_arquivo)
        word_cloud.generate()


