from django.test import TestCase, Client
from django.urls import reverse, resolve

from .models import Blog
from .views import BlogListView, BlogDetailView

class BlogPageTest(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(
            title = 'A new blog',
            body = 'I love creating, designing and bringing to live website!',
            pub_date = '2020-10-17 14:24',
            image = '/media/images/fire-wallpaper-207353_QyNbcms.jpg'
        )
        self.response = self.client.get('/blog/')
        self.no_response = self.client.get('/bobo/')
        self.resp = self.client.get(self.blog.get_absolute_url())
        self.no_resp = self.client.get('/blog/ywgjhiqhajhiasojabc/')

    def test_blog_listing(self):
        self.assertEqual(self.blog.title, 'A new blog')
        self.assertNotEqual(self.blog.title, 'Tweak, I hate programming')
        self.assertEqual(self.blog.pub_date, '2020-10-17 14:24')
        self.assertNotEqual(self.blog.pub_date, '2019-08-28 14:32')
        self.assertEqual(self.blog.image, '/media/images/fire-wallpaper-207353_QyNbcms.jpg')
        self.assertNotEqual(self.blog.pub_date, '/media/images/fire-wallpaper-53_QyNbcms.jpg')

    def test_blog_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.no_response.status_code, 404)

    def test_bloglist_url_resolves_bloglistview(self):
        views = resolve('/blog/')
        self.assertEqual(
            views.func.__name__,
            BlogListView.as_view().__name__
        )
    
    def test_blog_template_used(self):
        self.assertTemplateUsed(self.response, 'allblogs.html')
        self.assertTemplateNotUsed(self.response, 'notblog.html')

    def test_blog_detail_status_code(self):
        self.assertEqual(self.resp.status_code, 200)
        self.assertEqual(self.no_resp.status_code, 404)
    
    def test_blog_detail_contains_correct_html(self):
        self.assertContains(self.resp, 'I love creating, designing and bringing to live website!')
        self.assertNotContains(self.resp, 'lalalallallalalallalalalal')
    
    def test_blog_detail_template_used(self):
        self.assertTemplateUsed(self.resp, 'blogdetail.html')
        self.assertTemplateNotUsed(self.resp, 'noblogdetail,html')

    def test_blogdetail_url_resolves_blogdetailview(self):
        views = resolve(self.blog.get_absolute_url())
        self.assertEqual(
            views.func.__name__,
            BlogDetailView.as_view().__name__
        )




    