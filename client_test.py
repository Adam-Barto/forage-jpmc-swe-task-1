import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        expected = [
            ('ABC', 120.48, 121.2, 120.84),
            ('DEF', 117.87, 121.68, 119.775)
        ]
        """ ------------ Add the assertion below ------------ """
        for i in range(len(quotes)):
            self.assertEqual(getDataPoint(quotes[i]), expected[i])

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        expected = [
            ('ABC', 120.48, 119.2, 119.84),
            ('DEF', 117.87, 121.68, 119.775)
        ]
        """ ------------ Add the assertion below ------------ """
        for i in range(len(quotes)):
            self.assertEqual(getDataPoint(quotes[i]), expected[i])

    """ ------------ Add more unit tests ------------ """
    def test_getratio_calculate(self):
        # price_a, price_b, expected
        price_test = [
            [120.48, 32.2, 3.741614906832298],
            [132.48, 42.2, 3.139336492890995],
            [240.48, 123.2, 1.9519480519480519],
            [150.48, 0, None] # The 0 Test
        ]
        for i in range(len(price_test)):
            self.assertEqual(getRatio(price_test[i][0],price_test[i][1]),price_test[i][2])



if __name__ == '__main__':
    unittest.main()
