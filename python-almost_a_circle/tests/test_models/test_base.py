from models.base import Base
from models.rectangle import Rectangle
import unittest

class TestBase(unittest.TestCase):
    """Testing"""
    def setUp(self):
        """Set up for test cases"""
        Base._Base__nb_objects = 0 
    
    def test_id(self):
        tst_obj = Base()
        self.assertEqual(tst_obj.id, 1)
        tst_obj1 = Base()
        self.assertEqual(tst_obj1.id, 2)
        tst_obj2 = Base(111)
        self.assertEqual(tst_obj2.id, 111)

    """ Testing to json string """
    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dic = r1.to_dictionary()
        json = Base.to_json_string([dic])
        self.assertEqual(json, '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]')

    def test_to_json_empty(self):
        json = Base.to_json_string([])
        self.assertEqual(json, '[]')

    def test_to_json_none(self):
        json = Base.to_json_string(None)
        self.assertEqual(json, '[]')

    """ Testing from json to string """
    def test_json_srting(self):
        json = Base.from_json_string(None)
        self.assertEqual(json, [])

    def test_json_str(self):
        json = Base.from_json_string("[]")
        self.assertEqual(json, [])

    def test_json_str_good(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_li_input = Base.to_json_string(list_input)
        json_output = Base.from_json_string(json_li_input)
        self.assertIsInstance(json_output, list)

    def test_json_str_empty(self):
        json = Base.from_json_string(None)
        self.assertEqual(json, [])

    def test_json_str_empty_2(self):
        json = Base.from_json_string("[]")
        self.assertEqual(json, [])

if __name__ == '__main__':
    unittest.main()