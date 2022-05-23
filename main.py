from scrape import Scrape
from save_csv_tweets_service import CSVTweets
from generate_word_cloud_service import GenerateWordCloudService

scrape = Scrape().initialize()

INPUT_WORD = "Qual palavra você gostaria de pesquisar?\nTecle Enter para sair \n\n> "
INPUT_RESULTS = "Quantos resultados você gostaria de trazer?\n> " 
QUIT = ""

resposta = input(INPUT_WORD)
while resposta != QUIT:

    max_resultados = int(input(INPUT_RESULTS))
    # usernames = scrape.get_id_user_by_usernames(["iamjusee"])
    tweets = scrape.get_tweets_from_words(resposta, max_resultados)

    resposta_write_csv = input("Gostarai de salvar em um CSV? [S/N] ")
    if resposta_write_csv.lower() == 's':
        csv = CSVTweets(tweets)
        nome_arquivo = input('digite o nome do arquivo:\n> ')
        nome_arquivo = f'{nome_arquivo}.csv' if nome_arquivo.find('.csv') < 0 else nome_arquivo
        csv.write(nome_arquivo)
        resposta_generate_world_cloud = input("Gostaria de gerar uma nuvem de palavras? [S/N] ")
        if resposta_generate_world_cloud.lower() == 's':
            word_cloud = GenerateWordCloudService(nome_arquivo)
            word_cloud.generate()
    
    print("\n")
    resposta = input(INPUT_WORD)

