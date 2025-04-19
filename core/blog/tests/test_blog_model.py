"""
SimpleTestCase without database
TransactionTestCase with database (about a model) on main db and remove after data
TestCase with dumy database
"""


from django.test import TestCase
from datetime import datetime

from ..models import Post, Category
from accounts.models import User, Profile


class TestPostModel(TestCase):
    
    def test_create_test_with_valid_data(self):
        post_obj = Post.objects.create(
            title='test',
            content='description',
            status=True,
            category=None,
            published_date=datetime.now(),
        )
        self.assertEqual(post_obj.title, 'test')
    
    def test_create_test_with_valid_data_and_user(self):
        user_obj = User.objects.create_user(email='test@gmail.co', password='@Pp123456')
        profile_obj, created  = Profile.objects.get_or_create(user=user_obj)
        """
        profile_obj.first_name = 'updated_first_name'
        profile_obj.last_name = 'updated_last_name'
        profile_obj.description = 'updated_description'
        profile_obj.save()
        """
        post_obj = Post.objects.create(
            author= profile_obj,
            title='test',
            content='description',
            status=True,
            category=None,
            published_date=datetime.now(),
        )
        self.assertEqual(post_obj.title, 'test')