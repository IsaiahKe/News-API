from app.models import Article
import unittest

class Article_test(unittest.TestCase):
    
    def setUp(self):
        self. new_article=Article('source','author','title','description','url','imageurl','content','published at')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
if __name__=='__main__':
    unittest.main()