from unittest import TestCase
from models.item import ItemModel

class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 29.99)
        self.assertEqual(item.name, 'test',
                         "The name of the item does not equal to the constructor")

        self.assertEqual(item.price, 29.99,
                         "The price of the item does not equal to the constructor")

    def test_item_json(self):
        item = ItemModel('test', 29.99)
        expected = {'name': 'test',
                    'price': 29.99
                    }
        self.assertEqual(item.json(), expected, msg="The json export is incorrect. Received {}, expectted {}".format(item.json(), expected))