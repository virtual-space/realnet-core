import unittest

from realnet_core import DataMemStore


class DataStoreTestCase(unittest.TestCase):

    def test_create_data(self):
        return
        ds = DataMemStore()

        t1 = ds.create_data('2', attributes={'three': 'four'})
        t2 = ds.retrieve_type(t1.id)

        self.assertEqual(t2.name, '2')
        self.assertEqual(t2.attributes['three'], 'four')

    def test_create_item(self):
        return
        ds = DataMemStore()

        t1 = ds.create_type('2', attributes={'three': 'four'})
        i1 = ds.create_item(t1, '6', attributes={'seven': 'eight'})

        i2 = ds.retrieve_item(i1.id)

        self.assertEqual(i2.type.name, '2')
        self.assertEqual(i2.type.attributes['three'], 'four')
        self.assertEqual(i2.name, '6')
        self.assertEqual(i2.attributes['seven'], 'eight')



if __name__ == '__main__':
    unittest.main()
