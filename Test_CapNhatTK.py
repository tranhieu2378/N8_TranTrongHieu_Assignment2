import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_DieuHuong import test_DH_ThongTinTK
from selenium.webdriver.common.keys import Keys
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def clear_field(element):
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.BACKSPACE)

# Testcase 1: Cập nhật thông tin tài khoản thành công
def test_UTK_001(driver):
    # Steps
    test_DH_ThongTinTK(driver)
    time.sleep(2)
    ho_ten_element = driver.find_element(By.ID, "nest-messages_hoTen")
    email_element = driver.find_element(By.ID, "nest-messages_email")
    soDT_element = driver.find_element(By.ID, "nest-messages_soDT")
    matKhau_element = driver.find_element(By.ID, "nest-messages_matKhau")

    clear_field(ho_ten_element)
    clear_field(email_element)
    clear_field(soDT_element)
    clear_field(matKhau_element)

    ho_ten_element.send_keys("Trần Trọng Hiếu")
    email_element.send_keys("tranhieu123@gmail.com")
    soDT_element.send_keys("098767123")
    matKhau_element.send_keys("password123")

    driver.find_element(By.XPATH, "//button[span[text() = 'Cập nhật thông tin']]").click()
    time.sleep(2)

    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Cập nhật thành công" in message_element.text


# Testcase 2: Cập nhật thông tin tài khoản với các trường không hợp lệ
def test_UTK_002(driver):
    # Steps
    test_DH_ThongTinTK(driver)
    time.sleep(2)
    email_element = driver.find_element(By.ID, "nest-messages_email")
    soDT_element = driver.find_element(By.ID, "nest-messages_soDT")
    matKhau_element = driver.find_element(By.ID, "nest-messages_matKhau")

    clear_field(email_element)
    clear_field(soDT_element)
    clear_field(matKhau_element)

    email_element.send_keys("tranhieu123@")
    soDT_element.send_keys("098edcca")
    matKhau_element.send_keys("pas")

    driver.find_element(By.XPATH, "//button[span[text() = 'Cập nhật thông tin']]").click()
    time.sleep(2)

    # Expected result
    error_email = driver.find_element(By.ID, "nest-messages_email_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Email không hợp lệ!" in error_email

    error_soDT = driver.find_element(By.ID, "nest-messages_soDT_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Số điện thoại không hợp lệ!" in error_soDT

    error_pwd = driver.find_element(By.ID, "nest-messages_matKhau_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Mật khẩu phải từ 6 đến 20 ký tự!" in error_pwd


# Testcase 3: Cập nhật thông tin tài khoản với form rỗng
def test_UTK_003(driver):
    # Steps
    test_DH_ThongTinTK(driver)
    time.sleep(2)
    ho_ten_element = driver.find_element(By.ID, "nest-messages_hoTen")
    email_element = driver.find_element(By.ID, "nest-messages_email")
    soDT_element = driver.find_element(By.ID, "nest-messages_soDT")
    matKhau_element = driver.find_element(By.ID, "nest-messages_matKhau")

    clear_field(ho_ten_element)
    clear_field(email_element)
    clear_field(soDT_element)
    clear_field(matKhau_element)

    driver.find_element(By.XPATH, "//button[span[text() = 'Cập nhật thông tin']]").click()
    time.sleep(2)

    # Expected result
    error_name = driver.find_element(By.ID, "nest-messages_hoTen_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Họ tên không được để trống!" in error_name

    error_email = driver.find_element(By.ID, "nest-messages_email_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Email không được để trống!" in error_email

    error_soDT = driver.find_element(By.ID, "nest-messages_soDT_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Số điện thoại không được để trống!" in error_soDT

    error_pwd = driver.find_element(By.ID, "nest-messages_matKhau_help").find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
    assert "Mật khẩu không được để trống!" in error_pwd