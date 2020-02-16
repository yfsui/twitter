"""
test of preprocessor.py
"""
import unittest
import preprocessor as PreprocessorClass

class TestMyModule(unittest.TestCase):
    """
    test of class Preprocessor
    """
    text = """RT @mytsvideo: Gia Itzel.\n\n100% free shemale cams.
    Enter now:  https://t.co/qJqq3VXTxg\n\n#shemale #TS #tgirl https://t.co/GMBmcJkz1E"""
    preprocessor = PreprocessorClass.Preprocessor(text,
                                                  max_length_dictionary=100000,
                                                  max_length_tweet=10)

    def test_clean_text(self):
        """
        test of clean_text
        """
        result = self.preprocessor.clean_text()
        expected_result = 'Gia Itzel   100  free shemale cams      Enter now     TS  tgirl '
        self.assertEqual(result, expected_result)

    def test_tokenize_text(self):
        """
        test of tokenize_text
        """
        result = self.preprocessor.tokenize_text()
        expected_result = ['Gia', 'Itzel', '100', 'free', 'shemale', 'cams',
                           'Enter', 'now', 'TS', 'tgirl']
        self.assertEqual(result, expected_result)

    def test_replace_token_with_index(self):
        """
        test of replace_token_with_index
        """
        self.preprocessor.final_text = self.preprocessor.clean_text()
        self.preprocessor.tokens = self.preprocessor.tokenize_text()
        result = self.preprocessor.replace_token_with_index()
        expected_result = [25389, 425, 41559, 33797, 2494, 111, 4219]
        self.assertEqual(result, expected_result)

    def test_pad_sequence(self):
        """
        test of pad_sequence
        """
        self.preprocessor.final_text = self.preprocessor.clean_text()
        self.preprocessor.tokens = self.preprocessor.tokenize_text()
        self.preprocessor.indexes = self.preprocessor.replace_token_with_index()
        result = self.preprocessor.pad_sequence()
        expected_result = [25389, 425, 41559, 33797, 2494, 111, 4219, 0, 0, 0]
        self.assertEqual(result, expected_result)
        