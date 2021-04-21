# %%
import lab1
import json
import importlib
import nltk

# %%
with open("./freqs.json", "r") as f:
    freqs_true = json.load(f)

# %%
importlib.reload(lab1)
puncts = ['.','!','?',',',';',':','[', ']', '{', '}', '(', ')', '\'', '\"']

raw_corpus = nltk.corpus.reuters.raw()
freqs = lab1.get_freqs(raw_corpus, puncts)

# %%
print(len(freqs))
print(len(freqs_true))

# %%
diff = []
for word in freqs:
    if word not in freqs_true:
        diff.append(word)
print(diff)

# %%
