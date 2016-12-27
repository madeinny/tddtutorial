from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.

class HomePageViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('<title>To-Do lists</title>', response.content.decode('utf8'))
        self.assertTrue(response.content.decode('utf8').startswith('<html>'))
        self.assertTrue(response.content.decode('utf8').strip().endswith('</html>'))
        
        expected_content = render_to_string('home.html')
        self.assertEqual(
            response.content.decode('utf8'),
            expected_content
        )