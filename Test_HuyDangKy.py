import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Test_DangNhap import test_DN_001

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_CDK_001(driver):
    test_DN_001(driver)

    driver.find_element(By.CLASS_NAME, "userDropdown_dropdownTrigger__TO32H").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "userDropdown_dropdownMenu__6DtQw"))
    )
    driver.find_element(By.XPATH, "//a[text()='Thông tin']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "thongtintaikhoan_profTitle__Y4ntt"))
    )

    driver.find_element(By.ID, 'course-tab').click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='Huỷ']").click()
    time.sleep(2)

    driver.switch_to.alert.accept()
    time.sleep(2)

    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    message_text = message_element.text
    assert "Huỷ ghi danh thành công" in message_text