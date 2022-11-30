# -*- coding: utf-8 -*-
# @File  : run_cover.py
# @Author: oaapao
# @Date  : 2022/11/30 11:55
# @Desc  :
# @Contact : zhiqiang.shen@zju.edu.cn

import pytest

if __name__ == '__main__':
    pytest.main(["--cov=./code/", "--cov-report=html", "--cov-config=./code/.coveragerc"])  # 执行某个目录下case
