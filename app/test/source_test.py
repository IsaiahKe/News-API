from app.models import Source
import unittest

class TestSource(unittest.TestCase):
    
    def setUp(self):
        self.new_source=Source('id','name','description','url','category','language','country')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
        
        
if __name__=='__main__':
    unittest.main()