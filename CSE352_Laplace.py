from random import randint
import string

sentence_file = open("eng_news_2016_10K-sentences.txt", "r", encoding='utf8')

each_sentence_list = []
selected_sentence = []
k = [0.5, 1.0, 2.0]
uni_counts = dict()
bi_counts = dict()

# open text file
if sentence_file.mode == "r":
    sentences = sentence_file.readlines()

for i in range(len(sentences)):
    each_sentence_list.append(sentences[i])

#erases the punctuations and spaces
each_sentence_list = [''.join(c for c in s if c not in string.punctuation) for s in each_sentence_list]
each_sentence_list = [s for s in each_sentence_list if s]
print(each_sentence_list[i].split())
#Create dictionary for UNIGRAM:
for i in range(len(each_sentence_list)):
    for each_word in each_sentence_list[i].split():
        if each_word in uni_counts:
            uni_counts[each_word] += 1
        else:
            uni_counts[each_word] = 1


#Create dictionary for BIGRAM:
for i in range(len(each_sentence_list)):
    for j in range(1, len(each_sentence_list[i].split())):
        each_word = ((each_sentence_list[i].split())[j-1], (each_sentence_list[i].split())[j])
        if each_word in bi_counts:
            bi_counts[each_word] += 1
        else:
            bi_counts[each_word] = 1


#store the sentences with length of 20 
for j in range(len(each_sentence_list)):
    if len(each_sentence_list[j].split()) == 20:
        selected_sentence.append(each_sentence_list[j])


#erases the punctuations and spaces from selected sentences
selected_sentence = [''.join(c for c in s if c not in string.punctuation) for s in selected_sentence]
selected_sentence = [s for s in selected_sentence if s]

# Test if the data is clearly set.
# for key, value in bi_counts.items():
#     if value == 5 :
#         print(key)

#10 random sentences for each test
#Store the 10 selected sentences.

for i in range(10):
    randNum = randint(0,len(selected_sentence))
    
    # Unigram method
    pr_word_unigram = 0
    pr_sentence_unigram = 1
    N_unigram = len(uni_counts)

    each_word = ""
    for each in selected_sentence[randNum].split():
        each_word = each
    for each_k in k:
        pr_word_unigram = (uni_counts[each_word]) / (N_unigram)
        pr_sentence_unigram = pr_sentence_unigram * pr_word_unigram
        print("When K = ", each_k,":", selected_sentence[randNum],"UNIGRAM: ",pr_sentence_unigram)
    
    # Bigram method
    pr_word_bigram = 0
    pr_sentence_bigram = 1
    N_bigram = len(bi_counts)
    
    for i in range(1, len(selected_sentence[randNum].split())):
        bi_words = ((selected_sentence[randNum].split())[i-1], (selected_sentence[randNum].split())[i])
        # print(bi_words)
    for each_k in k:
        pr_word_bigram = (bi_counts[bi_words] + each_k) / (uni_counts[bi_words[0]] + (each_k * N_bigram))
        pr_sentence_bigram = pr_sentence_bigram * pr_word_bigram
        print("When K = ", each_k,":", selected_sentence[randNum],"BIGRAM: ",pr_sentence_bigram)

        

    