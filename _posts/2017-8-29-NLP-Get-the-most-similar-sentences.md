---
layout: post
title: NLP - Get the most semantically similar texts
---

There are two types of data - with and without labels. In this post I will focus on the unlabeled text, which should simulate <a href="http://www.cs.cornell.edu/~cristian//Cornell_Movie-Dialogs_Corpus.html">human dialog</a> or <a href="https://www.cs.cmu.edu/~./enron/">a email communication</a>. There are a lot of stuff you can do with these texts, one of them is <a href="https://en.wikipedia.org/wiki/Cluster_analysis">clustering</a>.

You can use already implemented algorithms like <a href="http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html">KMeans</a>, but you will struggle with text representation, because in the human genereted text is a lot of misplelling and abbreavations. This makes tf-idf very sparse and uneffective to catch similarties in the text. For example, "cat" and "kitten" would be as far as "cat" and "house". Because tf-idf does not catch the semantic.

To solve this we can use <a href="https://en.wikipedia.org/wiki/Word2vec">the work</a> of Tomas Mikolov. He created neural network model which can "catch" the semantic of text into low-dimension space (usually 300 dim). I want to talk about it in future post. We will use FastText because it is character-based. We will base our aproach on this <a href="https://arxiv.org/pdf/1607.00570">paper</a>. So we use coordinate-wise mean, because it is simple to implement and provide not bad results.

My data looks like this:

{% highlight python %}

msg_raw || from || to || msg_init || msg_reply || subject || cluster (set to -1 at initializion)

{% endhighlight %}

Here is a part where I will take care of embeddings. I have already impleted version where I can use tf-idf weight to adjust embeddings:

{% highlight python %}

def get_embedding_for_doc(document_order, embedding_model, dim, tfidf_matrix, not_weight = True):
    embeddings = []
    number_of_examples = 0.0
    for w, s in [(terms[i], s) for (i, s) in get_scores_for_doc(document_order, tfidf_matrix)]:
        try:
            if not_weight:
                embeddings.append(embedding_model[w]) # normal
            else:
                embeddings.append((s * embedding_model[w])) # weighted
        except KeyError as e:
#             print (w , " not in dictionary (writing to file ./stopwords.txt)")
            with open("./stop_words.txt" , "aw") as f:
                f.write(w + "\n")
    embeddings = np.array(embeddings)
    if len(embeddings) > 0:
        return np.mean(embeddings, axis=0)
    else:
        return np.zeros(dim)

{% endhighlight %}

To get scored for ith document. We have to know index of the document:

{% highlight python %}

def get_scores_for_doc(document_order, tfidf_matrix):
    feature_index = tfidf_matrix[document_order,:].nonzero()[1]
    return zip(feature_index, [tfidf_matrix[document_order, x] for x in feature_index])

{% endhighlight %}


Loading of FastText (using <a href="https://radimrehurek.com/gensim/models/wrappers/fasttext.html">gensim</a>) model:

{% highlight python %}

from gensim.models.wrappers import FastText
import gensim
model_fast = FastText.load_fasttext_format("./embedings/wiki.cs")

{% endhighlight %}

{% highlight python %}

def find_most_close_dist(distance_matrix, search_index = -1, distance_limit = 0.1):
    indexes = []
    for index in distance_matrix[search_index].argsort()[1:]:
        indexes.append(index)
        if distance_matrix[search_index][index] > distance_limit:
            return indexes

{% endhighlight %}


These are our helper functions. How I will show you one iteration of clustering by taking the most similar sentences to my "seed" text and labeled them with some number/tag/whatever. Then I will choose another "seed" and do the same again.

{% highlight python %}

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(max_features=200000, encoding="utf8", decode_error="ignore", 
                                 min_df=2, stop_words=stop_words, analyzer = "word", lowercase = True,
                                 use_idf=True, tokenizer=word_tokenize, ngram_range=(1,1))

data = [str(msg).decode("utf8", "ignore") for msg, cluster in zip(df_small["msg_reply"], df_small["cluster"]) if cluster == -1]
data.append("This is beautiful.") # adding seed

%time tfidf_matrix = tfidf_vectorizer.fit_transform(data)

sentence_embedings = np.array([get_embedding_for_doc(x, model_fast, 300, tfidf_matrix) for x in range(0, len(data))])

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances

# dist = abs(1 - cosine_similarity(sentence_embedings))
# dist_e = euclidean_distances(sentence_embedings)
dist_pow = pow(np.array(1 - cosine_similarity(sentence_embedings)), 2)

tag_new_cluster = 6
indexes_to_change = find_most_close_dist(dist_pow, -1, 0.1)
for index in indexes_to_change:
    df_small.set_value(df_small.index[index], "cluster" , tag_new_cluster)
print(len(indexes_to_change) , "items was changed.")

{% endhighlight %}












