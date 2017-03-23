#! coding:utf-8
"""
test_app.py
"""
from datetime import datetime as dt
import unittest

from db import dal
from app import (get_chaos_all, get_chaos_all_count,
                 get_chaos_order_by_fractal, get_sum_fractal)


def preprocess_db():
    # Insert handler
    ins = dal.chaoses.insert()  # insert sql

    # Insert One
    dal.connection.execute(ins, name="dark hop", fractal=1)  # 1

    # Insert Multiple
    chaos_list = [
        {"name": "red cherry", "fractal": 2},  # 2
        {"name": "blue video", "fractal": 3},  # 3
        {"name": "green shot", "fractal": 4},  # 4
        {"name": "yellow moneys", "fractal": 5},  # 5
    ]
    dal.connection.execute(ins, chaos_list)

    # Insert DateTime
    # ColumnタイプにDateTimeを指定した場合は、Phythonのdatetime型で渡す必要がある。
    # もし文字列の場合は,datetime.strptime(str, fmt)を使ってdatetime型を生成しよう.
    chaos_list = [
        {"name": "red cherry", "fractal": 6, "modifyed_at": dt.now()},  # 6
        {"name": "red cherry", "fractal": 7, "modifyed_at": dt.strptime(
            "2017-12-02 23:24", "%Y-%m-%d %H:%M")},  # 7
    ]
    dal.connection.execute(ins, chaos_list)


class TestAppBlank(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dal.db_init('sqlite:///:memory:')

    def test_get_chaos_all_blank(self):
        results = get_chaos_all()
        self.assertEqual(results, [])

    def get_chaos_all_count_blank(self):
        count = get_chaos_all_count()
        self.assertEqual(count, 0)


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dal.db_init('sqlite:///:memory:')
        preprocess_db()

    def test_get_chaos_all_count(self):
        count = get_chaos_all_count()
        self.assertEqual(count, 7)

    def test_get_chaos_order_by_fractal(self):
        results = get_chaos_order_by_fractal()
        self.assertEqual(results[0].name, "dark hop")

    def test_get_sum_fractal(self):
        results = get_sum_fractal()
        self.assertEqual(results, 28)


if __name__ == '__main__':
    unittest.main()
