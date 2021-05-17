import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def remove_punctuation(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text


def remove_stopword(text):
    stop_words = set(stopwords.words('english'))
    words_tokens = word_tokenize(text)
    text = [w for w in words_tokens if w not in stop_words]
    text = ' '.join(text)
    return text


def lemmatize(text):
    lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(text)
    lemmatized_text = [lemmatizer.lemmatize(word) for word in word_tokens]
    text = ' '.join(lemmatized_text)
    return text


def print_topics(model, vectorizer):
    '''Print topics found by LDA model and words associated'''
    for idx, topic in enumerate(model.components_):
        print("Topic %d:" % (idx))
        print([(vectorizer.get_feature_names()[i], topic[i])
                        for i in topic.argsort()[:-10 - 1:-1]])
