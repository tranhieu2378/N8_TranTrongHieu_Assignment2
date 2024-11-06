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

# Kiểm tra đăng ký thành công
def test_DK_001(driver):
    # Steps
    driver.get("https://elearning-app-rm1o.vercel.app/users/dangky")
    driver.find_element(By.ID, "register_taiKhoan").send_keys("newuser2")
    driver.find_element(By.ID, "register_matKhau").send_keys("123456")
    driver.find_element(By.ID, "register_xacNhanMatKhau").send_keys("123456")
    driver.find_element(By.ID, "register_hoTen").send_keys("tester2")
    driver.find_element(By.ID, "register_email").send_keys("tester2@gmail.com")
    driver.find_element(By.ID, "register_soDT").send_keys("0987652389")
    driver.find_element(By.CLASS_NAME, "ant-btn").click()
    
    # Expected result
    message_success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Đăng ký thành công" in message_success.text

    assert "https://elearning-app-rm1o.vercel.app/users/dangnhap" in driver.current_url

# Kiểm tra đăng ký trùng tài khoản
def test_DK_002(driver):
    driver.get("https://elearning-app-rm1o.vercel.app/users/dangky")
    driver.find_element(By.ID, "register_taiKhoan").send_keys("newuser")
    driver.find_element(By.ID, "register_matKhau").send_keys("123456")
    driver.find_element(By.ID, "register_xacNhanMatKhau").send_keys("123456")
    driver.find_element(By.ID, "register_hoTen").send_keys("tester")
    driver.find_element(By.ID, "register_email").send_keys("tester99@gmail.com")
    driver.find_element(By.ID, "register_soDT").send_keys("0987656789")
    driver.find_element(By.CLASS_NAME, "ant-btn").click()
    time.sleep(2)

    message_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content")))

    assert "Tài khoản đã tồn tại" in message_element.text

# Kiểm tra đăng ký khi Email đã được tạo ở tài khoản khác
def test_DK_003(driver):
    # Steps
    driver.get("https://elearning-app-rm1o.vercel.app/users/dangky")
    driver.find_element(By.ID, "register_taiKhoan").send_keys("newuser4")
    driver.find_element(By.ID, "register_matKhau").send_keys("123456")
    driver.find_element(By.ID, "register_xacNhanMatKhau").send_keys("123456")
    driver.find_element(By.ID, "register_hoTen").send_keys("tester")
    driver.find_element(By.ID, "register_email").send_keys("newuser@example.com")
    driver.find_element(By.ID, "register_soDT").send_keys("0987656789")
    driver.find_element(By.CLASS_NAME, "ant-btn").click()
    time.sleep(2)

    # Expect result
    message_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content")))

    assert "Email đã tồn tại" in message_element.text

# Kiểm tra form rỗng
def test_DK_004(driver):
    # Steps
    driver.get("https://elearning-app-rm1o.vercel.app/users/dangky")
    driver.find_element(By.CLASS_NAME, "ant-btn").click()
    time.sleep(2)

    # Expect Result
    error_taiKhoan = driver.find_element(By.ID, "register_taiKhoan_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Không được để trống tài khoản" in error_taiKhoan

    error_matKhau = driver.find_element(By.ID, "register_matKhau_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Không được để trống mật khẩu" in error_matKhau

    error_xacNhanMatKhau = driver.find_element(By.ID, "register_xacNhanMatKhau_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Không được để trống mật khẩu" in error_xacNhanMatKhau

    error_hoTen = driver.find_element(By.ID, "register_hoTen_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Không được để trống họ tên" in error_hoTen

    error_email = driver.find_element(By.ID, "register_email_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Email không được để trống" in error_email

    error_soDT = driver.find_element(By.ID, "register_soDT_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Số điện thoại không được để trống" in error_soDT


# Kiểm tra khi nhập sai định dạng
def test_DK_005(driver):
    # Steps
    driver.get("https://elearning-app-rm1o.vercel.app/users/dangky")
    driver.find_element(By.ID, "register_email").send_keys("bbb111")
    driver.find_element(By.ID, "register_soDT").send_keys("aa123123")
    driver.find_element(By.ID, "register_matKhau").send_keys("123456")
    driver.find_element(By.ID, "register_xacNhanMatKhau").send_keys("123321")
    driver.find_element(By.CLASS_NAME, "ant-btn").click()
    time.sleep(2)

    # Expect result
    error_email = driver.find_element(By.ID, "register_email_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Email không chính xác" in error_email

    error_soDT = driver.find_element(By.ID, "register_soDT_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Số điện thoại không hợp lệ" in error_soDT

    error_xacNhanMatKhau = driver.find_element(By.ID, "register_xacNhanMatKhau_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Mật khẩu không trùng khớp" in error_xacNhanMatKhau

