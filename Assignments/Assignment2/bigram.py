from collections import defaultdict
from languageModel import LanguageModel
import random
import bisect

'''
Tuan Do
'''
class Bigram (LanguageModel):
    def __init__(self):
        self.unigramCounter = defaultdict(float)
        self.bigramCounter = defaultdict(float)
        self.prob = defaultdict(float)
        self.rand = random.Random()
    
    def train(self, trainingSentences):
        self.accu = defaultdict(list)
        
        for sentence in trainingSentences:
            for i, word in enumerate(sentence):
                self.unigramCounter[word] += 1
                if i < len(sentence) - 1:
                    self.bigramCounter[(word, sentence[i+1])] += 1
                else:
                    self.bigramCounter[(word, LanguageModel.STOP)] += 1

            if len(sentence) > 0:
                self.bigramCounter[(LanguageModel.START, sentence[0])] += 1

            self.unigramCounter[LanguageModel.START] += 1
            self.unigramCounter[LanguageModel.STOP] += 1

        self.unigramCounter[LanguageModel.UNK] += 1

        print 'Size of vocabulary %d' % len(self.getVocabulary())

        self.vocab_size = len(self.getVocabulary())

        print 'Size of bigram %d' % len(self.bigramCounter.keys())

        for prev_word, next_word in self.bigramCounter:
            self.prob[(prev_word, next_word)] = (self.bigramCounter[(prev_word, next_word)] + 0.01) / (self.unigramCounter[prev_word] + 0.01 * self.vocab_size)
            self.accu[prev_word].append(self.prob[(prev_word, next_word)] if len(self.accu[prev_word]) == 0 else 
                self.accu[prev_word][-1] + self.prob[(prev_word, next_word)] )

        print 'Done training'

    def getProp(self, prev_word, word):
        if (prev_word, word) in self.prob:
            return self.prob[(prev_word, word)]

        return 0.01 / (self.unigramCounter[prev_word] + 0.01 * self.vocab_size)


    def getWordProbability(self, sentence, index):
        if index == 0:
            return self.getProp(LanguageModel.START, sentence[0])
        if index == len(sentence):
            return self.getProp(sentence[-1], LanguageModel.STOP)
        
        prev_word = sentence[index - 1]
        word = sentence[index]
        return self.getProp(prev_word, word)
        
    def getVocabulary(self):
        return self.unigramCounter.keys()

    def generateWord(self, prev_word):
        x = self.rand.random()

        if prev_word in self.accu:
            # Random word
            if x > self.accu[prev_word][-1]:
                y = self.rand.randint(0, self.vocab_size - 1)
                return self.unigramCounter.keys()[y]
            index = bisect.bisect_left( self.accu[prev_word], x )
        else:
            index = bisect.bisect_left( self.accu[LanguageModel.START], x )

        return self.unigramCounter.keys()[index]
        
    def generateSentence(self):
        result = []
        prev_word = LanguageModel.START
        for i in xrange(1000):
            word = self.generateWord(prev_word)
            result.append(word)
            prev_word = word
            if word == LanguageModel.STOP:
                break
        return result