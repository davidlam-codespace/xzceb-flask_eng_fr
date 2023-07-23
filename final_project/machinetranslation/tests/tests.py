import unittest
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))

import translator


class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour") 

    def test2(self): 
        self.assertEqual(translator.english_to_french("Goodbye"), "Au revoir") 

    def test3(self): 
        self.assertEqual(translator.english_to_french("Flower"), "Fleur") 


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello") 

    def test2(self):         
        self.assertEqual(translator.french_to_english("Au revoir"), "Goodbye") 

    def test3(self): 
        self.assertEqual(translator.french_to_english("Fleur"), "Flower") 

unittest.main()