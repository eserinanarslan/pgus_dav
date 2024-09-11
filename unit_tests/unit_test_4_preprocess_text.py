import unittest
import pandas as pd
import string
import re

# Define the stop words for the test (replace this with your actual stop words list)
stop_words = set(['a', 'an', 'the', 'is', 'in', 'and', 'of', 'to', 'with', 'for'])

# Text preprocessing function
def preprocess_text(text):
    if pd.isnull(text):
        return ""

    # 1. Lowercase the text
    text = text.lower()

    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 3. Remove numbers
    text = re.sub(r'\d+', '', text)

    # 4. Remove extra whitespaces
    text = ' '.join(text.split())

    # 5. Remove stopwords
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]

    # 6. Join the filtered words back into a string
    filtered_text = ' '.join(filtered_words)

    return filtered_text

class TestPreprocessText(unittest.TestCase):
    def test_lowercase_conversion(self):
        self.assertEqual(preprocess_text("HELLO WORLD!"), "hello world")

    def test_remove_punctuation(self):
        self.assertEqual(preprocess_text("Hello, world! How's it going?"), "hello world hows it going")

    def test_remove_numbers(self):
        self.assertEqual(preprocess_text("There are 2 apples and 3 oranges."), "there are apples and oranges")

    def test_remove_extra_whitespaces(self):
        self.assertEqual(preprocess_text("This   is    a   test."), "this is a test")

    def test_clean_text(self):
        self.assertEqual(preprocess_text("Special characters: @#$$%^&*()"), "special characters")

    def test_remove_stopwords(self):
        self.assertEqual(preprocess_text("The quick brown fox jumps over the lazy dog"), "quick brown fox jumps lazy dog")

    def test_handle_null(self):
        self.assertEqual(preprocess_text(None), "")

    def test_empty_string(self):
        self.assertEqual(preprocess_text(""), "")

    def test_combined_steps(self):
        self.assertEqual(preprocess_text("123 Hello!   This is a Test."), "hello this test")

if __name__ == '__main__':
    unittest.main()
