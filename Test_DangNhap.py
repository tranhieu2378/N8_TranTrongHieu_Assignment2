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

# Testcase 1: Kiểm tra đăng nhập thành công
def test_DN_001(driver):
    # Steps
    driver.get("https://elearning-app-rm1o.vercel.app/users/dangnhap")
    driver.find_element(By.ID, "login-form_taiKhoan").send_keys("newuser")
    driver.find_element(By.ID, "login-form_matKhau").send_keys("password123")
    driver.find_element(By.ID, "login-button").click()
    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Đăng nhập thành công" in message_element.text
    assert "https://elearning-app-rm1o.vercel.app/" in driver.current_url
    assert driver.find_element(By.ID, "userDropdown")


# Testcase 2: Kiẻm tra đăng nhập sai tài khoản hoặc mật khẩu
def test_DN_002(driver):
    # Steps
    driver.get("https://elearning-app-rm1o.vercel.app/users/dangnhap")
    driver.find_element(By.ID, "login-form_taiKhoan").send_keys("bbb111")
    driver.find_element(By.ID, "login-form_matKhau").send_keys("123123")
    driver.find_element(By.ID, "login-button").click()
    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    message_text = message_element.text
    assert "Tài khoản hoặc mật khẩu không đúng" in message_text

# Testcase 3 kiểm tra đăng nhập với form rỗng
def test_DN_003(driver):
    # Streps
    driver.get("https://elearning-app-rm1o.vercel.app/users/dangnhap")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Expected result
    error_taiKhoan = driver.find_element(By.ID, "login-form_taiKhoan_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Không được để trống tài khoản" in error_taiKhoan

    error_matKhau = driver.find_element(By.ID, "login-form_matKhau_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Không được để trống mật khẩu" in error_matKhau

# Testcase 4: Kiểm tra login với admin
def test_DN_004(driver):
    # Steps
    driver.get("https://elearning-app-rm1o.vercel.app/users/dangnhap")
    driver.find_element(By.ID, "login-form_taiKhoan").send_keys("bbb111")
    driver.find_element(By.ID, "login-form_matKhau").send_keys("123456")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Đăng nhập thành công" in message_element.text

    assert "https://elearning-app-rm1o.vercel.app/" in driver.current_url
    time.sleep(2)
    driver.find_element(By.ID, "userDropdown").click()
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//a[text()='Trang quản trị']")