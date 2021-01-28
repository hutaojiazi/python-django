import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Project
from ..serializers import ProjectSerializer


# initialize the APIClient app
client = Client()

class GetAllProjectsTest(TestCase):
    """ Test module for GET all projects API """

    def setUp(self):
        Project.objects.create(
            title='Python examples', description='Python project description', technology='Python', image='img/project1.png')
        Project.objects.create(
            title='Java examples', description='Java project description', technology='Java', image='img/project2.png')
        Project.objects.create(
            title='Angular examples', description='Angular project description', technology='Angular', image='img/project3.png')
        Project.objects.create(
            title='React examples', description='React project description', technology='React', image='img/project4.png')

    def test_get_all_projects(self):
        # get API response
        response = client.get(reverse('get_post_projects'))
        # get data from db
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleProjectTest(TestCase):
    """ Test module for GET single project API """

    def setUp(self):
        self.python = Project.objects.create(
            title='Python examples', description='Python project description', technology='Python', image='img/project1.png')
        self.java = Project.objects.create(
            title='Java examples', description='Java project description', technology='Java', image='img/project2.png')
        self.angular = Project.objects.create(
            title='Angular examples', description='Angular project description', technology='Angular', image='img/project3.png')
        self.react = Project.objects.create(
            title='React examples', description='React project description', technology='React', image='img/project4.png')

    def test_get_valid_single_project(self):
        response = client.get(
            reverse('get_delete_update_project', kwargs={'pk': self.rambo.pk}))
        project = Project.objects.get(pk=self.rambo.pk)
        serializer = ProjectSerializer(project)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_project(self):
        response = client.get(
            reverse('get_delete_update_project', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProjectTest(TestCase):
    """ Test module for inserting a new project """

    def setUp(self):
        self.valid_payload = {
            'title': 'Java project',
            'description': 'A brand new Java project',
            'technology': 'Java',
            'image': 'img/project1.png'
        }

        self.invalid_payload = {
            'title': '',
            'description': 'A invalid Java project',
            'technology': 'Java',
            'image': 'img/project1.png'
        }

    def test_create_valid_project(self):
        response = client.post(
            reverse('get_post_projects'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_project(self):
        response = client.post(
            reverse('get_post_projects'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleProjectTest(TestCase):
    """ Test module for updating an existing project record """

    def setUp(self):
        self.python = Project.objects.create(
            title='Python examples', description='Python project description', technology='Python', image='img/project1.png')
        self.java = Project.objects.create(
            title='Java examples', description='Java project description', technology='Java', image='img/project2.png')
        self.valid_payload = {
            'title': 'Java project',
            'description': 'A brand new Java project',
            'technology': 'Java',
            'image': 'img/project1.png'
        }

        self.invalid_payload = {
            'title': '',
            'description': 'A invalid Java project',
            'technology': 'Java',
            'image': 'img/project1.png'
        }

    def test_valid_update_project(self):
        response = client.put(
            reverse('get_delete_update_project', kwargs={'pk': self.python.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_project(self):
        response = client.put(
            reverse('get_delete_update_project', kwargs={'pk': self.python.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleProjectTest(TestCase):
    """ Test module for deleting an existing project record """

    def setUp(self):
        self.python = Project.objects.create(
            title='Python examples', description='Python project description', technology='Python', image='img/project1.png')
        self.java = Project.objects.create(
            title='Java examples', description='Java project description', technology='Java', image='img/project2.png')

    def test_valid_delete_project(self):
        response = client.delete(
            reverse('get_delete_update_project', kwargs={'pk': self.python.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_project(self):
        response = client.delete(
            reverse('get_delete_update_project', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
