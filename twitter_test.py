import unittest  # library for unit testing
import twitter as TwitterClass

class TestMyModule(unittest.TestCase):
    text = 'RT @mytsvideo: Gia Itzel.\n\n100% free shemale cams. Enter now:  https://t.co/qJqq3VXTxg\n\n#shemale #TS #tgirl https://t.co/GMBmcJkz1E'
    twitter = TwitterClass.Twitter(text)

    def test_clean_text(self):
        result = self.twitter.clean_text()
        expected_result = 'Gia Itzel   100  free shemale cams  Enter now     TS  tgirl '
        self.assertEqual(result,expected_result)

    def test_tokenize_text(self):
        result = self.twitter.tokenize_text()
        expected_result = ['Gia', 'Itzel','100','free','shemale','cams','Enter','now','TS','tgirl']
        self.assertEqual(result,expected_result)

    def test_replace_token_with_index(self):
        self.twitter.tokens = ['Gia','Itzel','100','free','shemale','cams','Enter','now','TS','tgirl']
        result = self.twitter.replace_token_with_index()
        expected_result = [24477, 122718, 338, 40136, 32649, 2289, 71, 3931, 176800]
        self.assertEqual(result,expected_result)

    def test_pad_sequence(self):
        self.twitter.indexes = [24477, 122718, 338, 40136, 32649, 2289, 71, 3931, 176800]
        result = self.twitter.pad_sequence()
        expected_result = [24477, 122718, 338, 40136, 32649, 2289, 71, 3931, 176800]
        self.assertEqual(result,expected_result)