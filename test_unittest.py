import problem_solving as pst
import unittest

class Test_TestCensor(unittest.TestCase):
    def test_censor_1(self):
        self.assertEqual(pst.censor('The cat ate a mouse.'), "### cat ate # mouse. <n10817239>")
        
    def test_censor_2(self):
        self.assertEqual(pst.censor('I went to the store.'), 'I went to ### store. <n10817239>')

    def test_censor_3(self):
        self.assertEqual(pst.censor('A cookie is a very nice thing'), '# cookie is # very nice thing <n10817239>')

    def test_censor_4(self):
        self.assertEqual(pst.censor('THe thing over there is tHe best!'),'### thing over there is ### best! <n10817239>')

    def test_censor_5(self):
        self.assertEqual(pst.censor('aN-otter-ate-An-apple.'), '##-otter-ate-##-apple. <n10817239>')
    def test_censor_6(self):
        self.assertEqual(pst.censor("Don't change anything!"), "Don't change anything!")


class Test_TestFertiliser(unittest.TestCase):
    def test_fertiliser_1(self):
        self.assertEqual(pst.fertiliser(1.0, 0.0, 0.0, 1.0, 2.0, 2.0), (2.0,  2.0))
    
    def test_fertiliser_2(self):
        self.assertEqual(pst.fertiliser(0.3, 0.2, 0.1, 0.4, 10,  20 ), (20.0, 39.99999999999999))
    
    def test_fertiliser_3(self):
        self.assertEqual(pst.fertiliser(0.1, 0.4, 0.3, 0.2, 10,  20 ), (40.0, 20.0))
    
    def test_fertiliser_4(self):
        self.assertEqual(pst.fertiliser(0.5, 0.5, 0.5, 0.3, 10,  2  ), None)
    
    def test_fertiliser_5(self):
        self.assertEqual(pst.fertiliser(0.3, 0.3, 0.3, 0.3, 10,  20 ), None)

if __name__ == '__main__':
    unittest.main
