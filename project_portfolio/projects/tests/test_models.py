from django.test import TestCase
from ..models import Project


class ProjectTest(TestCase):
    """ Test module for Project model """

    def setUp(self):
        Project.objects.create(
            title='Python examples', description='Python project description', technology='Python', image='project1.png')
        Project.objects.create(
            title='Java examples', description='Java project description', technology='Java', image='project2.png')

    def test_project_description(self):
        project_python = Project.objects.get(name='Python examples')
        project_java = Project.objects.get(name='Java examples')
        self.assertEqual(
            project_python.get_description(), "Python examples is a projects: Python project description.")
        self.assertEqual(
            project_java.get_description(), "Java examples is a projects: Java project description.")
