from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from nltk.corpus import udhr

def get_freqs(corpus: str, puncts):
    freqs = {}
    ### BEGIN SOLUTION
    for punct in puncts:
        corpus = corpus.replace(punct, ' ')
    for digit in range(0, 10):
        corpus = corpus.replace(str(digit), ' ')
    for token in corpus.lower().split():
        token = token.strip()
        if token == '':
            continue
        if token in freqs:
            freqs[token] += 1
        else:
            freqs[token] = 1
    ### END SOLUTION
    return freqs

def get_top_10(freqs):
    top_10 = []
    ### BEGIN SOLUTION
    res = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    top_10 = [res[i][0] for i in range(10)]
    ### END SOLUTION
    return top_10

def get_bottom_10(freqs):
    bottom_10 = []
    ### BEGIN SOLUTION
    res = sorted(freqs.items(), key=lambda x: x[1], reverse=False)
    bottom_10 = [res[i][0] for i in range(10)]
    ### END SOLUTION
    return bottom_10

def get_percentage_singletons(freqs):
    ### BEGIN SOLUTION
    cnt = 0
    for token in freqs:
        if freqs[token] == 1:
            cnt += 1
    return cnt / len(freqs) * 100
    ### END SOLUTION

def get_freqs_stemming(corpus, puncts):
    ### BEGIN SOLUTION
    porter = PorterStemmer()
    freqs = {}
    for punct in puncts:
        corpus = corpus.replace(punct, ' ')
    for digit in range(0, 10):
        corpus = corpus.replace(str(digit), ' ')
    for token in corpus.lower().split():
        token = token.strip()
        if token == '':
            continue
        token = porter.stem(token)
        if token in freqs:
            freqs[token] += 1
        else:
            freqs[token] = 1
    return freqs
    ### END SOLUTION

def get_freqs_lemmatized(corpus, puncts):
    ### BEGIN SOLUTION
    wordnet_lemmatizer = WordNetLemmatizer()
    freqs = {}
    for punct in puncts:
        corpus = corpus.replace(punct, ' ')
    for digit in range(0, 10):
        corpus = corpus.replace(str(digit), ' ')
    for token in corpus.lower().split():
        token = token.strip()
        if token == '':
            continue
        token = wordnet_lemmatizer.lemmatize(token, pos="v")
        if token in freqs:
            freqs[token] += 1
        else:
            freqs[token] = 1
    return freqs
    ### END SOLUTION

def size_of_raw_corpus(freqs):
    ### BEGIN SOLUTION
    return len(freqs)
    ### END SOLUTION

def size_of_stemmed_raw_corpus(freqs_stemming):
    ### BEGIN SOLUTION
    return len(freqs_stemming)
    ### END SOLUTION

def size_of_lemmatized_raw_corpus(freqs_lemmatized):
    ### BEGIN SOLUTION
    return len(freqs_lemmatized)
    ### END SOLUTION

def percentage_of_unseen_vocab(a, b, length_i):
    ### BEGIN SOLUTION
    return len(set(a) - set(b)) / length_i
    ### END SOLUTION

def frac_80_perc(freqs):
    ### BEGIN SOLUTION
    total = sum([freqs[token] for token in freqs])
    freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    cnt = 0
    frac = 0
    for freq in freqs:
        if frac >= 0.8 * total:
            break
        frac += freq[1]
        cnt += 1
    return cnt / len(freqs)
    ### END SOLUTION

def plot_zipf(freqs):
    ### BEGIN SOLUTION
    freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    plt.plot(range(1, len(freqs)+1), [freq[1] for freq in freqs])
    ### END SOLUTION
    plt.show()  # put this line at the end to display the figure.

def get_TTRs(languages):
    TTRs = {}
    for lang in languages:
        words = udhr.words(lang)
        ### BEGIN SOLUTION
        TTRs[lang] = []
        for num in range(100, 1301, 100):
            seen = set()
            n_type = 0
            for i in range(num):
                word = words[i].lower()
                if word not in seen:
                    seen.add(word)
                    n_type += 1
            TTRs[lang].append(n_type)
        ### END SOLUTION
    return TTRs

def plot_TTRs(TTRs):
    ### BEGIN SOLUTION
    for lang in TTRs:
        plt.plot(range(100, 1301, 100), TTRs[lang], label=lang)
    plt.legend()
    ### END SOLUTION
    plt.show()  # put this line at the end to display the figure.
