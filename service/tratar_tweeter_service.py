import nltk
import domain.tags as tags

class TratarTweeterService:

    def __init__(self, dados_tweeter) -> None:
        self.dados_tweeter = dados_tweeter

    def tokenizar_dados_tweeter(self):
        # nltk.download('punkt')
        self.tokens = nltk.word_tokenize(self.dados_tweeter.tweet)
        return self

    def posicionar_tags(self):
        # nltk.download('averaged_perceptron_tagger')
        self.tagged = nltk.pos_tag(self.tokens)
        return self

    def remover_preposicoes_adverbios_dois_pontos_virgula(self):
        self.tagged_removed = []
        for tag in self.tagged:
            word, item = tag
            if item is not tags.PREPOSITION_OR_SUBORDINATING_CONJUNCETION and item is not tags.ADVERB and item is not tags.TWO_POINTS and item is not tags.COMMA:
                self.tagged_removed.append((word, item))

        print(self.tagged_removed)



