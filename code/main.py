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


# ==========================================================================
#  测试硬币组合程序代码请注释掉下面所有代码；测试机场跑道程序是请注释掉上面代码
# ==========================================================================
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def airport(n: int, points: List[Point]):
    def quick_judge(a, b, c, d):
        # 快速排斥实验，判断线段ab和线段cd是否不相交,不相交返回False，不能判断不相交返回True
        if (max(a.x, b.x) < min(c.x, d.x) or
                max(c.x, d.x) < min(a.x, b.x) or
                max(a.y, b.y) < min(c.y, d.y) or
                max(c.y, d.y) < min(a.y, b.y)):
            return False
        else:
            return True

    # 求向量ab和向量cd的叉乘
    def xmult(a, b, c, d):
        vectorAx = b.x - a.x
        vectorAy = b.y - a.y
        vectorBx = d.x - c.x
        vectorBy = d.y - c.y
        return vectorAx * vectorBy - vectorAy * vectorBx

    def cross(a, b, c, d):
        if not quick_judge(a, b, c, d):
            return False
        xmult1 = xmult(c, d, c, a)
        xmult2 = xmult(c, d, c, b)
        xmult3 = xmult(a, b, a, c)
        xmult4 = xmult(a, b, a, d)
        if xmult1 * xmult2 < 0 and xmult3 * xmult4 < 0:
            return True
        else:
            return False

    if n != len(points):
        raise RuntimeError("Invalid Input")
    lines = []
    for i in range(n - 1):
        lines.append([points[i], points[i + 1]])
    lines.append([points[0], points[n - 1]])

    max_dist = -1
    for i in points:
        for j in points:
            if i == j:
                continue
            dist = round(pow(pow(i.x - j.x, 2) + pow(i.y - j.y, 2), 0.5), 6)
            if dist < max_dist:
                continue
            tag = True
            for line in lines:
                if cross(line[0], line[1], i, j):
                    tag = False
                    break
            if tag:
                max_dist = dist
    return max_dist


if __name__ == '__main__':
    data = [Point(0, 20), Point(40, 0), Point(40, 20), Point(70, 50), Point(50, 70), Point(30, 50), Point(0, 50)]
    print(airport(7, data))
