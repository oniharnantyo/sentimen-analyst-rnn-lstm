import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from collections import Counter
import json
from bhasa.spell import correction

text = "RT@oniharnantyo 06.26 wib Ada kegiatan car freeday di ruas jl.malioboro. kondisi seputaran sp km 0 lenggang. pic.twitter.com/uF5YKQNcfB"

def preprocess(teks):
    # hapus RT
    hasil = re.sub('(\\s)(RT)(\\s)', '', teks, flags=re.MULTILINE)
    print("hapus rt: ",hasil)
    # hapus url
    hasil = re.sub('(www|http|pic|https)\S+', '', hasil, flags=re.MULTILINE).lower();
    print('hapus url: ',hasil)
    # hapus username
    hasil = re.sub('@[^\s]+', '', hasil, flags=re.MULTILINE)
    print('hapus username: ', hasil)
    # hapus tanda
    hasil = re.sub('[^A-Za-z09\\s]+', '', hasil, flags=re.MULTILINE)
    print('hapus tanda: ', hasil)
    # hapus pagar
    hasil = re.sub('#[^\s]+', '', hasil, flags=re.MULTILINE)
    print('hapus pagar: ', hasil)
    # hapus angka
    hasil = re.sub('([09]+)(\\s|$)', '', hasil, flags=re.MULTILINE)
    hasil = re.sub('(^|\\s)([09]+)', '', hasil, flags=re.MULTILINE)
    print('hapus angka: ', hasil)
    # hapus stop word
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    hasil = stopword.remove(hasil)
    print('hapus stopword: ', hasil)

    out = ''
    for data in (hasil.split(" ")):
        data.replace(" ","")
        data.strip()
        print("token : ",data)
        if(data != " " and data != ""):
            kata_dasar = correction(data)
            out = out + " " + kata_dasar
    hasil = out
    print('hapus correction: ', hasil)
    stemmerFactory = StemmerFactory()
    stemmer = stemmerFactory.create_stemmer()
    hasil = stemmer.stem(hasil)
    print('stemmer: ',hasil)

    return hasil;

#
# def words(text):
#     return re.findall(r'\w+',text)
#
# WORDS = Counter(words(open('big.txt').read()))
#
# def P(word, N=sum(WORDS.values())):
#     # "Probability of `word`."
#     return WORDS[word] / N
#
# def correction(word):
#     # "Most probable spelling correction for word."
#     return max(candidates(word), key=P)
#
# def candidates(word):
#     # "Generate possible spelling corrections for word."
#     return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
#
# def known(words):
#     # "The subset of `words` that appear in the dictionary of WORDS."
#     return set(w for w in words if w in WORDS)
#
# def edits1(word):
#     # "All edits that are one edit away from `word`."
#     letters    = 'abcdefghijklmnopqrstuvwxyz'
#     splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)] # [('', 'kemarin'), ('k', 'emarin'), ('ke', 'marin'), dst]
#     deletes    = [L + R[1:]               for L, R in splits if R] # ['emarin', 'kmarin', 'kearin', dst]
#     transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1] # ['ekmarin', 'kmearin', 'keamrin', dst]
#     replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters] # ['aemarin', 'bemarin', 'cemarin', dst]
#     inserts    = [L + c + R               for L, R in splits for c in letters] # ['akemarin', 'bkemarin', 'ckemarin', dst]
#     return set(deletes + transposes + replaces + inserts)
#
# def edits2(word):
#     # "All edits that are two edits away from `word`."
#     return (e2 for e1 in edits1(word) for e2 in edits1(e1))

with open('malioboro.json',"r") as file:
    data = json.load(file)
for d in data:
    print("awal:", d['text'])
    print(preprocess(d['text']))