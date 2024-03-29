import pytest
import unittest
import random

from lotto_3 import Card, Bag

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card(['Железяка', True])

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(len(self.card.numbers), 15)
        self.assertEqual(len(self.card.positions), 3)
        self.assertEqual(len(self.card.used), 0)

    def test_decision(self):
        a = random.randint(0,90)
        self.assertEqual(self.card.decision(a, 1), a in self.card.numbers)

    def test_show(self):
        self.assertIsNone(self.card.show())

    def test_cover(self):
        a = self.card.numbers[-1]
        self.assertTrue(self.card.cover(a, True)[0])
        self.assertFalse(self.card.cover(a, False)[0])

class TestBag(unittest.TestCase):


    def setUp(self):
        self.bag = Bag()

    def test_init(self):
        self.assertEqual(len(self.bag.bag), 90)

    def test_next_barrel(self):
        self.assertNotEqual(self.bag.bag[0], self.bag.bag[-1])
        while self.bag.cur_pos < 89:
            self.assertNotEqual(self.bag.next_barrel(), self.bag.next_barrel())
        with pytest.raises(Exception, match='Мешок пуст'):
            self.bag.next_barrel()
        try:
            self.bag.next_barrel()
        except:
            self.assertRaises(Exception)
