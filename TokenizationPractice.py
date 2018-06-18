import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import replacers
from replacers import RegexpReplacer
from replacers import RepeatReplacer
import re
import string

#open hate speech file and read into one big string, ignoring new line characters; include extra space so words don't get concatenated
s = ""
f = open('/home/R18cmansueti/hateSpeech/meinKampfVolI.txt', 'rU')
for line in f:
    s+=" " +line.strip()

#different tokenizations
#word tokenization of using whitespaces
tokenizer=RegexpTokenizer('\s+',gaps=True)
tokens=tokenizer.tokenize(s)    
  
#tokenzation of words that begin with capital letters
capt = RegexpTokenizer(' [A-Z]\w+')
capitalWords=capt.tokenize(s)
print("\nThe first 200 words that begin with capital letters are:")
print(capitalWords[:200])
print("Number of elements in capital words ")
print(len(capitalWords))


#capitalWords but without duplicate words counted
capitalWordsNoDups=list(set(capt.tokenize(s)))
print("\n\n")
print(capitalWordsNoDups[:200])
print("Number of elements in capital words no duplicats: ")
print(len(capitalWordsNoDups))
  
#sentence tokenzation
sent=sent_tokenize(s)
print("\nThe first 10 sentences are:")
print(sent[:10])
  

#turn list of tokens into NLTK Text
text = nltk.Text(tokens)

#print out collocations
print("\nThe collocations are: ")
text.collocations()






#NORMALIZATION SECTION

#hanve't gotten this section to work #remove punctuation 
#tokenized_words_by_sentence=[word_tokenize(doc) for doc in sent_tokenize(s)]
#x=re.compile('[%s]' % re.escape(string.punctuation))
#tokenized_words_by_sentence_no_punc = []
#for review in tokenized_words_by_sentence:
#    new_review = []
#    for token in review:
#        new_token = x.sub(u'', token)
#        if not new_token    == u'':
#            new_review.append(new_token)
#        tokenized_words_by_sentence.append(new_review)
#print(tokenized_words_by_sentence_no_punc[:10])

#remove stop words from the word tokenization
stops=set(stopwords.words('english'))
tokens_no_stop_words=[w for w in tokens if w not in stops]
print(tokens[:100])
print("\nTokenized words with stop words removed:")
print(tokens_no_stop_words[:100])

#remove stops from sentence tokenization
print("\nFirst 20 entences after stops have been removed:")
sentences_no_stops=[None] * len(sent)

for i in range(0, len(sent)):
    temp = sent[i]
    newTemp = tokenizer.tokenize(temp)
    newTemp=[w for w in newTemp if w not in stops]
    newTemp=' '.join(newTemp)
    sentences_no_stops.insert(i, newTemp)
    
print(sentences_no_stops[:20]) 
    


#convert sentences to all lowercase
lowercase_sentences=[None] * len(sent)

for i in range(0, len(sent)):
    lowercase_sentences[i]=sent[i].lower()
    
#convert tokenized words to all lowercase
lowercase_words=[None] * len(tokens)

for i in range(0, len(tokens)):
    lowercase_words[i]=tokens[i].lower()
    
#replacing words with regular expressiong, i.e., 'won't' with 'will not'
#start with s, the untokenized text
replacer=RegexpReplacer()
replacedText=replacer.replace(s)
print(replacedText[:1000])

a="I'm art won't bar can't he isn't you won't and they've but would've and she's while you're good and i'd here I'd"
a=replacer.replace(a)
print(a)

#edit words with repeating characters and then tokenize a test sentence
#will probably use on forum posts
forumPost='I just looooooove it. It is ooooooh so fun aaah oooookaaay whateverrrrr'
repReplacer=RepeatReplacer()
forumPostTokenized=word_tokenize(forumPost)

for i in range(0, len(forumPostTokenized)):
    forumPostTokenized[i]=repReplacer.replace(forumPostTokenized[i])
    

forumPostTokenized=' '.join(forumPostTokenized)
print("\n\nBefore: ")
print(forumPost)
print("After: ")
print(forumPostTokenized)





#normalization in a different order. Normalize all text before it is tokenized
#first expand contractions
str1=''.join(s)
str1=replacer.replace(str1)

#convert to lowercase
str1=str1.lower()

#tokenize into sentences
str1Sentences=sent_tokenize(str1)

#remove punctuation by breaking down sentences into words
#then go through each token in sentence list a see if it punctuation

strToWords=[]
for x in range(0, len(str1Sentences)):
    strToWords.append(word_tokenize(str1Sentences[x]))

wordsNoPunc=[]
x=re.compile('[%s]' % re.escape(string.punctuation))

for i in range(0, len(strToWords)):
    new_list = []
    for token in strToWords[i]:
        new_token = x.sub(u' ', token)
        if not new_token == u' ':
            new_list.append(new_token)
    wordsNoPunc.append(new_list)

print(len(wordsNoPunc))
print(len(sent))      


