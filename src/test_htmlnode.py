import unittest

from htmlnode import HTMLnode


class TestHTMLnode(unittest.TestCase):
    def test_eq1(self):
        node = HTMLnode()
        node2 = HTMLnode()
        self.assertEqual(node.props_to_html(), node2.props_to_html())

if __name__ == "__main__":
    unittest.main()