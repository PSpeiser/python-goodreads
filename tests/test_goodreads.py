#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_goodreads
----------------------------------

Tests for `goodreads` module.
"""

import unittest

from goodreads import goodreads
from config import DEVELOPER_KEY, DEVELOPER_SECRET

class TestGoodreads(unittest.TestCase):

    def setUp(self):
        self.g = goodreads.Goodreads(DEVELOPER_KEY,DEVELOPER_SECRET)


    def test_something(self):
        pass

    def test_book(self):
        book = self.g.book(123)
        assert book.title == 'The Power of One'
        assert book.isbn == 385732546

    def test_search(self):
        results = self.g.book_search("Ender's Game")
        assert results


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()