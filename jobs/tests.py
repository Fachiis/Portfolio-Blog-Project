from django.test import TestCase, Client
from django.urls import reverse, resolve

from .models import Job
from .views import homepage


class HomePageTest(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
        self.no_response = self.client.get('homiii')

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.no_response.status_code, 404)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertTemplateNotUsed(self.response, 'nohome.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Fachiis')
        self.assertNotContains(self.response, 'Am not there')

    def test_homepage_url_resolves_homepage_view(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            homepage.__name__
        )


class JobModelTest(TestCase):
    def setUp(self):
        self.job = Job.objects.create(
            image = '/media/images/python_wp6_LpWvTsQ.jpg',
            summary = 'My job model is working'
        )
        self.response = self.client.get('/')
        self.no_response = self.client.get('/hhjeiuyujh/')

    def test_job_listing(self):
        self.assertEqual(self.job.summary, 'My job model is working')
        self.assertNotEqual(self.job.summary, 'Am not in the job summary model')
    
    def test_job_status_code_template_used(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.no_response.status_code, 404)
    
    def test_job_template_used(self):
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertTemplateNotUsed(self.response, 'nothome.html')
    
    def test_job_contains_correct_html(self):
        self.assertContains(self.response, 'job model is')
        self.assertNotContains(self.response, 'Hahahaha, I am not there')


