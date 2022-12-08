import unittest
import pytest
from task_1 import filter_the_list

my_list = [
     {'visit1': ['Москва', 'Россия']}, 
     {'visit2': ['Дели', 'Индия']},
     {'visit3': ['Владимир', 'Россия']}
    ]
    
# class TestMain(unittest.TestCase):

    # def test_len_list(self):
    #     result = filter_the_list(my_list)
    #     self.assertEqual(len(result), 2) 
    #     self.assertNotEqual(len(result), 1) 
        

    # def test_isinstance_list(self):
    #     result = filter_the_list(my_list)
    #     self.assertIsInstance(result, list) 
    #     self.assertNotIsInstance(result, str)


def test_len():
    result = filter_the_list(my_list)
    assert len(result) == 2    
        

