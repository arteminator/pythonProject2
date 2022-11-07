from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_case_blog(self):
        b = Blog('Test', 'Test author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test author', b.author)
        self.assertListEqual([], b.posts)
    def test_repr(self):
        b = Blog('Test', 'Test author')
        b2 = Blog('Mark', 'Twain')
        self.assertEqual(b.__repr__(), 'Test by Test author (0 posts)')
        self.assertEqual(b2.__repr__(), 'Mark by Twain (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test author')
        b.posts = ['Yellow']
        b2 = Blog('Mark', 'Twain')
        b2.posts = ['Red', 'Green']

        self.assertEqual(b.__repr__(), 'Test by Test author (1 post)')
        self.assertEqual(b2.__repr__(), 'Mark by Twain (2 posts)')

    def test_json(self):
        b = Blog('Test', 'Test author')
        b.create_post('Test post', 'Test content')
        expected = {
            'title': 'Test',
            'author': 'Test author',
            'post': [
                {'title': 'Test post',
                 'content': 'Test content'}
            ]
        }

        self.assertDictEqual(expected, b.json())