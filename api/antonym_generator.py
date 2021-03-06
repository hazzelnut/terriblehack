import nltk
from nltk.corpus import wordnet as wn


class AntonymGenerator:
    def __init__(self):
        self.punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
                            '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    def process_string(self, paragraph):
        output = []
        split_string = nltk.word_tokenize(paragraph)
        for word in split_string:
            antonym_found = False
            if word not in self.punctuation:
                syns = wn.synsets(word)

                if syns and syns[0].pos() in ['a', 's', 'n']:
                    for synset in syns:
                        if antonym_found:
                            break
                        for lemma in synset.lemmas():
                            # print(word, lemma)
                            if lemma.antonyms():
                                output.append(lemma.antonyms()[0].name())
                                antonym_found = True
                                break
                if antonym_found:
                    continue
            output.append(word)

        return " ".join(output)

