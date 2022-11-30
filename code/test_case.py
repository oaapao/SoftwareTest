# -*- coding: utf-8 -*-
# @File  : test_case.py
# @Author: oaapao
# @Date  : 2022/11/30 11:53
# @Desc  :
# @Contact : zhiqiang.shen@zju.edu.cn
from code.main import my_op


class TestDemo:
    def test_case1(self):
        assert my_op('+', 1, 1) == 2

    def test_case2(self):
        assert my_op('+', 1, 0) == 1

    def test_case3(self):
        assert my_op('+', -1, 1) == 0
