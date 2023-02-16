from dataclasses import dataclass
from nltk.corpus import stopwords
import pandas as pd
import string


@dataclass
class FileReader:
    """
    This class is a generic class that is able to read and transform different file formats to text.
    """

    file_name: str
    file_type: str

    def __post_init__(self) -> pd.DataFrame | str:

        if self.file_type == 'csv':

            df = pd.read_csv(self.file_name)

            return df

        if self.file_type == 'txt':
            pass


@dataclass
class Cleaner:
    """
    This class is a generic class that is able to filter text from different sources. These sources are:
    - CV files from Incentro
    - Job offers
    """

    text: str

    def __post_init__(self):

        text_without_punctuation = self.remove_punctuation(self.text)
        text_without_whitespace = self.remove_whitespace(text_without_punctuation)
        text_lowercase = self.change_uppercase_to_lowercase(text_without_whitespace)
        text_without_stopwords = self.remove_stopwords(text_lowercase)

        return text_without_stopwords

    @staticmethod
    def remove_punctuation(text: str):
        """

        :param text:
        :return:
        """

        text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation))

        return text_without_punctuation

    @staticmethod
    def remove_whitespace(text: str):
        """

        :param text:
        :return:
        """

        text_without_whitespace = " ".join(text.split())

        return text_without_whitespace

    @staticmethod
    def change_uppercase_to_lowercase(text: str):
        """

        :param text:
        :return:
        """

        return text.lower()

    @staticmethod
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
