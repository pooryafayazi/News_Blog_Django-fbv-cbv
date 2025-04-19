"""
SimpleTestCase without database
TransactionTestCase with database (about a model) on main db and remove after data
TestCase with dumy database
"""

""" two types
1st. the form doesn't need DB and just needs input data
2nd. the form needs DB data 
"""

from django.test import SimpleTestCase, TestCase
from datetime import datetime

from ..forms import PostForm
from ..models import Category


"""
class TestPostForm(SimpleTestCase): # without DB & without category
    
    def test_post_form_with_valid_data(self):
        form = PostForm(data={
            'title':'test',
            'content':'description',
            'status':True,
            'published_date':datetime.now(),
        })
        self.assertTrue(form.is_valid())
"""       

class TestPostForm(TestCase): # with DB for create category object
    
    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(name='for test')
        form = PostForm(data={
            'title':'test',
            'content':'description',
            'status':True,
            'category':category_obj,
            'published_date':datetime.now(),
        })
        self.assertTrue(form.is_valid())
        
    def test_post_form_with_no_data(self):
        form = PostForm(data={            
        })
        self.assertFalse(form.is_valid())