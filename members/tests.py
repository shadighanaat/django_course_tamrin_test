from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Members


class TestMembers(TestCase):
    @classmethod
    def setUp(cls):

        cls.user = User.objects.create(username='user1')
        cls.members1 = Members.objects.create(
            title='members1',
            text='this is car',
            status=Members.STATUS_CHOICES[0][0],
            author=cls.user,
        )
        cls.members2 = Members.objects.create(
            title='members2',
            text='this is car',
            status=Members.STATUS_CHOICES[1][0],
            author=cls.user,
        )

    def test_members_model_str(self):
        members = self.members1
        self.assertEqual(str(members), members.title)

    def test_members_detail(self):
        self.assertEqual(self.members1.title, 'members1')
        self.assertEqual(self.members1.text, 'this is car')

    def test_members_list_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_members_list_url_by_name(self):
        response = self.client.get(reverse('members_list'))
        self.assertEqual(response.status_code, 200)

    def test_members_title_on_page_list(self):
        response = self.client.get(reverse('members_list'))
        self.assertContains(response, self.members1.title)

    def test_members_detail_on_page_list(self):
        response = self.client.get(f'//{self.members1.id}/')
        self.assertContains(response, self.members1.text)

    def test_members_create_view(self):
        response = self.client.post(reverse('create'), {
            'title': 'members1',
            'text': 'this is car',
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Members.objects.last().title, 'members1')
        self.assertEqual(Members.objects.last().text, 'this is car')

    def test_members_update_view(self):
        response = self.client.post(reverse('update', args=[self.members2.id]), {
            'title': 'members2 updated',
            'text': 'this is car updated',
            'status': 'pup',
            'author': self.members2.author.id,

        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Members.objects.last().title, 'members2 updated')
        self.assertEqual(Members.objects.last().text, 'this is car updated')

    def test_members_delete_view(self):
        response = self.client.post(reverse('delete', args=[self.members1.id]))

        self.assertEqual(response.status_code, 302)
