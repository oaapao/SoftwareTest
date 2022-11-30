# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: oaapao
# @Date  : 2022/11/30 11:42
# @Desc  :
# @Contact : zhiqiang.shen@zju.edu.cn


def my_op(type: str, a: int, b: int) -> int:
    if type == "+":
        return a + b
    elif type == "-":
        return a - b
    elif type == "*":
        return a * b
