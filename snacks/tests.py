from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from snacks.models import Snack

# Create your tests here.


class SnacksModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="tester", email="tester@gmail.com", password="pass")
        self.snack = Snack.objects.create(name="Cheetos", purchaser=self.user, description="cheesy and delicious")

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Cheetos")

    def test_snack_name(self):
        self.assertEqual(self.snack.name, "Cheetos")

    def test_snack_description(self):
        self.assertEqual(f'{self.snack.description}', 'cheesy and delicious')


class SnackListViewTest(TestCase):
    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")
