from models.item import ItemModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_contex():
            item = ItemModel('test', 29.99)
            self.assertIsNone(ItemModel.find_by_name('test'),
                              msg="Found an item with name{}, but expected no to.".format(item.name))

            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'))