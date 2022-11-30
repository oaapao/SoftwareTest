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
