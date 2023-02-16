from nltk.corpus import stopwords
import string


def remove_punctuation(text: str):
    """

    :param text:
    :return:
    """

    text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation))

    return text_without_punctuation


def remove_whitespace(text: str):
    """

    :param text:
    :return:
    """

    text_without_whitespace = " ".join(text.split())

    return text_without_whitespace


def change_uppercase_to_lowercase(text: str):
    """

    :param text:
    :return:
    """

    return text.lower()


def remove_stopwords(text: str, language: str = 'english'):
    """

    :param text:
    :param language:
    :return:
    """

    stopwords_english = stopwords.words(language)
    text_tokens = text.split(' ')

    text_without_stopwords = [word for word in text_tokens if word not in stopwords_english]
    join_words_to_string = " ".join(text_without_stopwords)

    return join_words_to_string
