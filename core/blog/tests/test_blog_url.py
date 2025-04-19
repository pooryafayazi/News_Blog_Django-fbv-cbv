"""
SimpleTestCase without database
TransactionTestCase with database (about a model) on main db and remove after data
TestCase with dumy database
"""

from django.test import TestCase
from django.urls import reverse, resolve #dynamic resolver

from ..views import Indexview, PostListView, PostDetailView


class TestUrl(TestCase):
    
    def test_blog_index_url_resolve(self):
        url = reverse('blog:index')
        self.assertEqual(resolve(url).func.view_class, Indexview)
    
    def test_blog_post_list_url_resolve(self):
        url = reverse('blog:post-list')
        self.assertEqual(resolve(url).func.view_class, PostListView)
    def test_post_detail_with_arg_input_url(self):
        url = reverse('blog:post-detail', kwargs={'pk' : 1})
        self.assertEqual(resolve(url).func.view_class, PostDetailView)