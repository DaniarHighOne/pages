
from django.test import TestCase
from .models import Posts
from django.urls import reverse

# Create your tests here.
class HomePage(TestCase):
    def setUp(self):
        Posts.objects.create(text ='just a test')#create a simple text by this comman

#by this we expected equality btw two variables
    def test_text_content(self):
        post = Posts.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')

class HomePageView(TestCase):
    
    def setUp(self):#these are not tests btw

        Posts.objects.create(text ='this is a another test')

    def test_View_url_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def  test_view_uses_corr_html(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')



