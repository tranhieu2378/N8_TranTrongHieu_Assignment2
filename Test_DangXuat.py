import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_DangNhap import test_DN_001

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Testcase Đăng xuất
def test_DX_001(driver):
    # Steps
    driver.get("https://elearning-app-rm1o.vercel.app/users/dangnhap")
    test_DN_001(driver)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "ant-dropdown-trigger").click()
    time.sleep(2)
    driver.find_element(By.ID, "button-logout").click()
    
    # Expect result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "đăng xuất thành công" in message_element.text
    
    assert "https://elearning-app-rm1o.vercel.app/" in driver.current_url

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Đăng nhập']"))
    )
    assert driver.find_element(By.XPATH, "//a[text()='Đăng nhập']")
