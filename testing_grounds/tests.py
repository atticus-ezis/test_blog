from django.test import TestCase, Client
from django.urls import reverse 
from django.contrib.auth.models import User 
from models import Blog

class AuthorizedUserDelete(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='AugaHolic101')
        self.user1 = User.objects.create_user(username='user2', password='AugaHolic102')

        self.blog = Blog.objects.create(title='Test Post', content='Test Content', author = self.user1)

        self.client = Client()

    def test_user_can_delete_own_blog_post(self):
        # Log in as the blog post author (user1)
        self.client.login(username='user1', password='AugaHolic101')
        
        # Attempt to delete the blog post
        response = self.client.post(reverse('delete', args=[self.blog.id, 'blog']))
        
        # Check that the blog post was deleted
        self.assertEqual(response.status_code, 302)  # Assuming redirect after deletion
        self.assertFalse(Blog.objects.filter(id=self.blog.id).exists())




