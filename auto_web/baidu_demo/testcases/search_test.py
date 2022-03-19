# -*- coding: utf-8 -*-
# @Time : 2022/3/19 8:17 上午
# @Author : Kevin
# @File : search_test.py
# @Software: PyCharm

from selenium import webdriver
import pytest
import time

key_words = ["Hogwarts"]


class TestSearch:
    def setup(self):
        self.start_time = time.time()
        chromedriver = "auto_web/driver/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromedriver)

    @pytest.mark.parametrize("search_key", key_words, ids=[f"搜寻_{i}" for i in key_words])
    def test_search(self, search_key):
        self.driver.get("https:www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        result = self.driver.page_source
        assert search_key in result

    def teardown(self):
        print("本次case的使用时间:", time.time() - self.start_time)
        self.driver.quit()
