import nltk
import domain.tags as tags
from collections import namedtuple, Counter

class TratarTweeterService:

    def __init__(self, dados_tweeter = None) -> None:
        self.dados_tweeter = dados_tweeter

    def tokenizar_dados_tweeter(self):
        # nltk.download('punkt')
        self.tokens = nltk.word_tokenize(self.dados_tweeter.tweet, language='portuguese')
        return self

    def posicionar_tags(self):
        # nltk.download('averaged_perceptron_tagger')
        self.tagged = nltk.pos_tag(self.tokens)
        return self

    def remover_preposicoes_adverbios_dois_pontos_virgula(self):
        tweet, tweet_tagged = "", []
        for tag in self.tagged:
            word, item = tag
            if item != tags.PREPOSITION_OR_SUBORDINATING_CONJUNCETION and item != tags.ADVERB and item != tags.TWO_POINTS and word not in tags.PONTUATIONS and item != tags.CARDINAL_NUMBER and item != tags.NOUN_PROPER_SINGULAR and item != tags.ADJECTIVE and item != tags.VERB_PRESENT_TENSE_NOT_3RD_PERSON_SINGULAR and word not in tags.CONJUNCOES and word not in tags.PREPOSICOES and word not in tags.ARTIGOS and word not in tags.LINGUAGEM_INTERNET:
                if word.find("//") < 0 and word != "https":
                    tweet += f"{word} "
                    tweet_tagged.append(word)

        
        return [tweet, tweet_tagged]

    def count_words_bank(self, words):
        Analise = namedtuple("Analise", ["count_word_pix", "count_word_nubank", "count_word_inter", "count_word_safra", "count_word_c6", "count_word_santander"])
        count_word_pix = 0
        count_word_nubank = 0
        count_word_inter = 0
        count_word_safra = 0
        count_word_c6 = 0
        count_word_santander = 0
        for word in words:
            word = word.lower()
            if word == "nubank":
                count_word_nubank += 1
            if word == "inter":
                count_word_inter += 1
            if word == "safra":
                count_word_safra += 1
            if word == "c6":
                count_word_c6 += 1
            if word == "santander":
                count_word_santander += 1
            if word == "pix":
                count_word_pix += 1

        return Analise(count_word_pix, count_word_nubank, count_word_inter, count_word_safra, count_word_c6, count_word_santander)

    def count_words(self, words):
        words_ = []
        for word in words:
            for w in word:
                words_.append(w)
        return Counter(words_).most_common(20)





    



