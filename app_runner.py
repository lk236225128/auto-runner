# -*- coding: utf-8 -*-
# @Time : 2022/3/19 8:45 上午
# @Author : Kevin
# @File : app_runner.py
# @Software: PyCharm

import pytest

if __name__ == '__main__':
    pytest.main(["auto_app/baidu_demo/testcases/",
                 "--clean-alluredir",
                 "--html=auto_web/reports/report.html"])
