from django.test import TestCase
from .templates import home
# Create your tests here.

class HomeTest(TestCase):
    def test_home(self):
        self.assertEqual(2+2,4);
        self.assertTrue(5>1);
        self.assertFalse(3==4);
        self.assertContains(response,"Welcome")
        self.assertTemplateUsed(response,"home.html")


class HomeTemplateTest(TestCase):
    def test_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response,"Welcome Students")

