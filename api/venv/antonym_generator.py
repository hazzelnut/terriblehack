import nltk
from nltk.corpus import wordnet as wn


class AntonymGenerator:
    def __init__(self):
        nltk.download('punkt')
        self.punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
                            '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    def process_string(self, paragraph):
        output = []
        split_string = nltk.word_tokenize(m)
        for word in split_string:
            if word not in self.punctuation:
                syns = wn.synsets("program")
                antonym_found = False
                if syns[0].pos() == 'a':
                    for synset in syns:
                        if not antonym_found:
                            break
                        for lemma in synset.lemmas():
                            if lemma.antonyms():
                                output.append(lemma.antonyms()[0].name())
                                antonym_found = True
                                break
                if not antonym_found:
                    break
            output.append(word)
        return output


newGenerator = AntonymGenerator()
paragraph1 = "Apple is looking at buying U.K. startup for $1 billion. Is that tiny Rick?"
paragraph1 = "Apple is looking at buying U.K. startup for $1 billion. \n Is that tiny Rick?"
print(newGenerator.process_string())