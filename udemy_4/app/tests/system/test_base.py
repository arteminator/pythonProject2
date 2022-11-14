from unittest import TestCase
from app.app import app
import json

class TestBase(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()