# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: oaapao
# @Date  : 2022/11/30 11:42
# @Desc  :
# @Contact : zhiqiang.shen@zju.edu.cn
from typing import List


def coin_comb(n: int, m: int, nums: List[int]) -> int:
    """
    给你一个非负整数n，再给你一个整数数组nums表示不同面值的硬币。
    请你计算并返回可以凑成总金额n的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
    :param n:表示总金额数
    :param m:表示数组的元素个数
    :param nums:互不相同的m个整数表示不同面值的硬币
    :return:可以凑成总金额的硬币组合数
    """
    # input check
    N = 99999999
    if not (isinstance(n, int) and isinstance(m, int) and isinstance(nums, List)):
        raise RuntimeError("Invalid Input")
    if n >= N:
        raise RuntimeError("Invalid Input, n is too big")
    if len(nums) != m:
        raise RuntimeError("Invalid Input")
    if len(nums) != len(list(set(nums))):
        raise RuntimeError("Invalid Input")
    for i in nums:
        if not isinstance(i, int):
            raise RuntimeError("Invalid Input")

    a = [0] * N  # 权重为i的组合数
    a[0] = 1
    for coin in nums:
        b = [0] * N
        j = 0
        while True:
            if j * coin > n:
                break
            k = 0
            while True:
                if k + j * coin > n:
                    break
                b[k + j * coin] += a[k]
                k += 1
            j += 1
        a = b.copy()
    return a[n]


if __name__ == '__main__':
    print(coin_comb(10, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
