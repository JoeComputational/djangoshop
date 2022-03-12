import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('hey'.upper(), 'HEY')

    def test_isupper(self):
        self.assertTrue('HEY'.isupper())
        self.assertFalse('HEY'.isupper())

    def test_split(self):
        s = 'hey jeremy'
        self.assertEqual(s.split(), ['hey', 'jeremy'])
        with self.assertRaises(TypeError):
            s.split(2)
            #This can help check if its split or not

if __name__ == '__main__':
    unittest.main()
