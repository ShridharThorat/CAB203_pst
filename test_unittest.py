import problem_solving_2 as pst
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

# import unittest

# problem_solving = __import__("problem_solving")

# class TestMethods(unittest.TestCase):

#     def test_censor(self):
#         if 'censor' not in dir(problem_solving): self.skipTest("censor doesn't exist")
#         if "studentid" not in dir(problem_solving): self.skipTest("Problem Solving File has no studentid defined, please define one")

#         censortests = [
#                         ('The cat ate a mouse.', '### cat ate # mouse.'),
#                         ('I went to the store.', 'I went to ### store.'),
#                         ('A cookie is a very nice thing', '# cookie is # very nice thing'),
#                         ('THe thing over there.is.tHe.best!', '### thing over there.is.###.best!'),
#                         ('aN-otter-ate-An-apple.', '##-otter-ate-##-apple.'),
#                         ("Don't change anything!", "Don't change anything!")
#                     ]
#         for text, result in censortests:
#             with self.subTest(text=text):
#                 sol = problem_solving.censor(text)
#                 if text != result: result = f'{result} <{problem_solving.studentid}>'
#                 self.assertEqual(sol, result, f'\n\tReturned: {sol}\n\tExpected: {result}')
            
#     def test_fertiliser(self):
#         if 'fertiliser' not in dir(problem_solving): self.skipTest("fertiliser doesn't exist")
#         fertilisertests = [
#              ((1.0, 0.0, 0.0, 1.0, 2.0, 2.0), (2.0,  2.0)),
#              ((0.3, 0.2, 0.1, 0.4, 10,  20 ), (20.0, 40.0)),
#              ((0.1, 0.4, 0.3, 0.2, 10,  20 ), (40.0, 20.0)),
#              ((0.5, 0.5, 0.5, 0.3, 10,  2  ), None),
#              ((0.3, 0.3, 0.3, 0.3, 10,  20 ), None)
#             ]
#         for args, result in fertilisertests:
#             with self.subTest(args=args):
#                 sol = problem_solving.fertiliser(*args)
#                 if result == None: self.assertIsNone(sol,f"\n\tExpected: None\n\tReturned: {sol}")
#                 else: 
#                     self.assertIsNotNone(sol, f"\n\tExpected: {sol}\n\tReturned: None")
#                     self.assertAlmostEqual(sol[0], result[0], delta=0.001)
#                     self.assertAlmostEqual(sol[1], result[1], delta=0.001)

# if __name__ == "__main__":
#     unittest.main()