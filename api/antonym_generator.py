import nltk
from nltk.corpus import wordnet as wn


class AntonymGenerator:
    def __init__(self):
        nltk.download('punkt')
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


# newGenerator = AntonymGenerator()
# paragraph1 = "Apple is looking at buying U.K. startup for $1 billion. That is a big elephant."
# paragraph2 = "You are a bad person, Delly."
# print(newGenerator.process_string(paragraph1))
# print(newGenerator.process_string(paragraph2))
