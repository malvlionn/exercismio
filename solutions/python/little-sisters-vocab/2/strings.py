"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    awalan = vocab_words[0]
    hasil = [awalan]
    for words in (vocab_words[1:]):
        ditambah = awalan + words
        hasil += [ditambah]
    return " :: ".join(hasil)

def remove_suffix_ness(word):
    katabaru = word[:-4]
    if katabaru[-1] == "i":
        katabaru = katabaru[:-1] + "y"
    return katabaru

def adjective_to_verb(sentence, index):
    listkalimat = sentence.split()
    diamau = listkalimat[index]
    if diamau[-1].isalpha():
        return diamau + "en"
    return diamau[:-1] + "en"
