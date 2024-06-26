from django.test import TestCase, Client
from django.urls import reverse 
from django.contrib.auth.models import User 
from .models import Blog, Comment

class AuthorizedUserDelete(TestCase):
    def setUp(self):
        # create users
        self.user1 = User.objects.create_user(username='user1', password='AugaHolic101')
        self.user1 = User.objects.create_user(username='user2', password='AugaHolic102')

        # create blog
        self.blog = Blog.objects.create(title = 'Test Post', text_content = 'Test Content', user = self.user1)
        self.comment = Comment.objects.create(text_content= 'TEST content', blog = self.blog, user = self.user1)

        # create client 
        self.client = Client()

    def test_user_can_delete_own_blog_post(self):
        # Log in as the blog post author (user1)
        self.client.login(username='user1', password='AugaHolic101')
        
        # Attempt to delete the blog post
        response = self.client.post(reverse('delete', args=[self.blog.id, 'blog']))
        
        # Check that the blog post was deleted
        self.assertEqual(response.status_code, 302)  # Assuming redirect after deletion
        self.assertFalse(Blog.objects.filter(id=self.blog.id).exists())

    def test_user_cant_delete_others_blog_post(self):

        # login as wrong user
        self.client.login(username='user2', password='AguaHolic102')

        response = self.client.post(reverse('delete', args=[self.blog.id, 'blog']))

        self.assertEqual(response.status_code, 302)  # Assuming redirect after deletion
        self.assertTrue(Blog.objects.filter(id=self.blog.id).exists())

    def test_author_can_delete_comment(self):

        self.client.login(username='user1', password='AugaHolic101')
        response = self.client.post(reverse('delete', args=[self.comment.id, 'comment']))
        self.assertEqual(response.status_code, 302)  # Assuming redirect after deletion
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())

    def test_user_cant_delete_others_blog_post(self):

        self.client.login(username='user2', password='AguaHolic102')
        response = self.client.post(reverse('delete',args=[self.comment.id, 'blog']))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())







