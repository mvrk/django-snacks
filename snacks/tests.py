from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class SnacksTest(simple_test):
    def tests_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def tests_about_page_status(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_not_found(self):
        url = 'rui/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')
