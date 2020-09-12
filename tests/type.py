import unittest

from realnet_core import Type


class TypeLifecycle(unittest.TestCase):

    def test_json(self):
        t1 = Type('1', '2', {'three': 'four'})
        t2 = Type.from_json(t1.to_json())

        self.assertEqual(t2.id, '1')
        self.assertEqual(t2.name, '2')
        self.assertEqual(t2.attributes.three, 'four')


if __name__ == '__main__':
    unittest.main()
