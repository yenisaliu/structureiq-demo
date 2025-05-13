import unittest
from modules import bridge

class TestBridgeProcessing(unittest.TestCase):
    def test_filter(self):
        sample = [(1, 'bridge', 80), (2, 'bridge', 70)]
        result = bridge.process(sample)
        self.assertEqual(result, [(1, 'bridge', 80)])

if __name__ == '__main__':
    unittest.main()