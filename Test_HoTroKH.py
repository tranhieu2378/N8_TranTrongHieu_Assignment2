import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Testcase 1: Kiểm tra chức năng đăng ký tư vấn
def test_HT_001(driver):
    # Steps
    driver.get('https://elearning-app-rm1o.vercel.app/')
    driver.find_element(By.ID, "TuVan_name").send_keys("Trần Trọng Hiếu")
    driver.find_element(By.ID, "TuVan_email").send_keys("tranhieu4345@gmail.com")
    driver.find_element(By.ID, "TuVan_phone").send_keys("098763733")
    # Click
    phone_element = driver.find_element(By.ID, "btnTuVan")
    driver.execute_script("arguments[0].scrollIntoView(true);", phone_element)
    time.sleep(1) 
    phone_element.click()
    time.sleep(2)
    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    message_text = message_element.text
    assert "Đăng ký tư vấn thành công" in message_text


# Testcase 2: Kiểm tra chức năng nhận tin khuyến mãi
def test_HT_002(driver):
    # Steps
    driver.get('https://elearning-app-rm1o.vercel.app/')
    driver.find_element(By.XPATH, "//input[@placeholder='Email nhận khuyến mãi']").send_keys('tranhieu4345@gmail.com')
    # Click
    phone_element = driver.find_element(By.ID, "btnKhuyenMai")
    driver.execute_script("arguments[0].scrollIntoView(true);", phone_element)
    time.sleep(1) 
    phone_element.click()
    time.sleep(2)
    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    message_text = message_element.text
    assert "Đăng ký nhận khuyến mãi thành công" in message_text