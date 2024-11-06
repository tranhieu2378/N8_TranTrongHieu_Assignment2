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

# Testcase 1: Tìm kiếm thành công
def test_TK_001(driver):
    # Steps
    driver.get('https://elearning-app-rm1o.vercel.app/')
    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm']").send_keys('tư duy')
    driver.find_element(By.CLASS_NAME, "search_btn").click()
    # Expected result
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "timkiem_card__ZulPx"))
    )
    assert driver.find_element(By.CLASS_NAME, "timkiem_card__ZulPx")


# Testcase 2: Tìm kiếm không có khoá học
def test_TK_002(driver):
    # Steps
    driver.get('https://elearning-app-rm1o.vercel.app/')
    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm']").send_keys('abcdefgh…')
    driver.find_element(By.CLASS_NAME, "search_btn").click()
    # Expected result
    no_course_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Không có khóa học nào']"))
    )
    assert no_course_message.is_displayed()


# Testcase 3: Tìm kiếm với ký tự đặc biệt (#)
def test_TK_003(driver):
    # Steps
    driver.get('https://elearning-app-rm1o.vercel.app/')
    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm']").send_keys('#####')
    driver.find_element(By.CLASS_NAME, "search_btn").click()
    # Expected result
    no_course_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Không có khóa học nào']"))
    )
    assert no_course_message.is_displayed()

# Testcase 4: Tìm kiếm với ký tự đặc biệt (%)
def test_TK_004(driver):
    # Steps
    driver.get('https://elearning-app-rm1o.vercel.app/')
    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm']").send_keys('%')
    driver.find_element(By.CLASS_NAME, "search_btn").click()
    # Expected result
    no_course_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Không có khóa học nào']"))
    )
    assert no_course_message.is_displayed()