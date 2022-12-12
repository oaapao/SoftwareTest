# -*- coding: utf-8 -*-
# @File  : test_case.py
# @Author: oaapao
# @Date  : 2022/11/30 11:53
# @Desc  :
# @Contact : zhiqiang.shen@zju.edu.cn
from code.main import coin_comb


class TestDemo:
    def test_case1(self):
        assert coin_comb(5, 3, [1, 2, 5]) == 4

    def test_case2(self):
        try:
            coin_comb(500, 5, [1, 2, 4, 5])
        except RuntimeError as err:
            assert err.__str__() == 'Invalid Input'
        else:
            assert False

    def test_case3(self):
        try:
            coin_comb(3, 1, [1, 5])
        except RuntimeError as err:
            assert err.__str__() == 'Invalid Input'
        else:
            assert False

    def test_case4(self):
        assert coin_comb(0, 1, [1]) == 1

    def test_case5(self):
        assert coin_comb(1000, 5, [1, 7, 8, 11, 12]) == 6088313

    def test_case6(self):
        assert coin_comb(200, 2, [2, 5]) == 21

    def test_case7(self):
        assert coin_comb(2000, 2, [1, 2]) == 1001

    def test_case8(self):
        try:
            coin_comb('a', 3, [1, 2, 5])
        except RuntimeError as err:
            assert err.__str__() == 'Invalid Input'
        else:
            assert False

    def test_case9(self):
        try:
            coin_comb(5, 3, ['a', 2, 5])
        except RuntimeError as err:
            assert err.__str__() == 'Invalid Input'
        else:
            assert False

    def test_case10(self):
        try:
            coin_comb(5, 3, [1.2, 2, 5])
        except RuntimeError as err:
            assert err.__str__() == 'Invalid Input'
        else:
            assert False

    def test_case11(self):
        assert coin_comb(10, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 42

    def test_case12(self):
        try:
            coin_comb(-1, 3, [1, 2, 5])
        except RuntimeError as err:
            assert err.__str__() == 'Invalid Input'
        else:
            assert False

    def test_case13(self):
        try:
            coin_comb(5, -1, [0])
        except RuntimeError as err:
            assert err.__str__() == 'Invalid Input'
        else:
            assert False

    def test_case14(self):
        assert coin_comb(5, 0, []) == 0
