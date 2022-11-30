# -*- coding: utf-8 -*-
# @File  : run_case.py
# @Author: oaapao
# @Date  : 2022/11/30 12:34
# @Desc  :
# @Contact : zhiqiang.shen@zju.edu.cn
import pytest

if __name__ == '__main__':
    pytest.main(["--html=./unit_result.html", "./code/test_case.py"])
