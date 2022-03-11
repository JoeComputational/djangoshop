from django.test import TestCase
from store.models import Category, Product

def beans_for_your(bean_list):
    if len(bean_list) > 1:
        raise ValueError("A maximum of 1 bean can be brought")
    return {"the_beans": bean_list}

class TestBeans(unittest.TestCase):
    def do_beans_buy(self):
        actual = beans_for_your(bean_list=["kidney", "black_bean"])
        expected = {"the_beans": ["kidney", "black_bean"]}
        self.assertEqual(actual, expected)