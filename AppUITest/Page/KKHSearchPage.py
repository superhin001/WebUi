from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By
from AppUITest.Page.basepage import AppUI
from Lib.Logger import Logger


class KKHSearchPage(AppUI):

    search_inputbox_id_loc1 = (By.ID, "com.dangdang.buy2:id/index_search")
    search_inputbox_id_loc = (By.ID, "com.dangdang.buy2:id/search_edit_input")
    search_button_loc = (By.ID, "com.dangdang.buy2:id/search_btn_search")

    search_result_item1_loc = (By.ID, "com.albot.kkh:id/tv_rank_by_composite")
    search_result_item2_loc = (By.ID, "com.albot.kkh:id/tv_rank_by_time")
    search_result_item3_loc = (By.ID, "com.albot.kkh:id/rl_rand_by_price")
    search_result_item4_loc = (By.ID, "com.albot.kkh:id/tv_screen")


    def click_search_input_box(self, searchkey):
        print("----------click_search_input_box-------")
        self.wait()
        self.find_element(*self.search_inputbox_id_loc1).click()
        self.wait()
        input_ele = self.find_element(*self.search_inputbox_id_loc)
        input_ele.send_keys(searchkey)
        # subprocess.call("adb shell input text "+searchkey)
        butt_ele = self.find_element(*self.search_button_loc)
        butt_ele.click()


    def switch_items(self):
        self.wait()
        self.find_element(*self.search_result_item1_loc)
        self.wait()
        self.find_element(*self.search_result_item2_loc)
        self.wait()
        self.find_element(*self.search_result_item3_loc)
        self.wait()
        self.find_element(*self.search_result_item4_loc)


def search_some(self, searchkey):
    self.click_search_input_box(searchkey)
    self.switch_items()
