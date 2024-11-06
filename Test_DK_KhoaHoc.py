import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from Test_DieuHuong import test_DH_ChiTiet
from Test_DangNhap import test_DN_001

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Testcase 1: Kiểm tra đăng ký khoá học khi chưa đăng nhập
def test_DKKH_001(driver):
    # Steps
    test_DH_ChiTiet(driver)
    driver.find_element(By.ID, "btn_DangKy_KH").click()
    time.sleep(2)
    
    # Expected result
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Vui lòng đăng nhập để đăng ký khoá học" in message.text
    assert "https://elearning-app-rm1o.vercel.app/users/dangnhap" in driver.current_url


# Testcase 2: Kiểm tra đăng ký khoá học thành công
def test_DKKH_002(driver):
    # Steps
    test_DN_001(driver)
    time.sleep(2)
    test_DH_ChiTiet(driver)
    driver.find_element(By.ID, "btn_DangKy_KH").click()
    time.sleep(2)
    
    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    message_text = message_element.text
    assert "Đăng ký thành công" in message_text


def test_DKKH_003(driver):
    # Steps
    test_DN_001(driver)
    time.sleep(2)
    test_DH_ChiTiet(driver)
    driver.find_element(By.ID, "btn_DangKy_KH").click()
    time.sleep(2)
    
    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    message_text = message_element.text
    assert "Đã đăng ký khóa học này rồi!" in message_text