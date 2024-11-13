import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Test_DieuHuong import test_DH_QLND
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def clear_field(element):
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.BACKSPACE)

# Testcase 1: Thêm người dùng
def test_QLND_001(driver):
    # Steps
    test_DH_QLND(driver)
    
    driver.find_element(By.XPATH, "//a[contains(text(), 'Thêm người dùng')]").click()
    time.sleep(2)
    
    driver.find_element(By.ID, "nest-messages_taiKhoan").send_keys("tester100")
    driver.find_element(By.ID, "nest-messages_matKhau").send_keys("123456")
    driver.find_element(By.ID, "nest-messages_hoTen").send_keys("Tester 100")
    driver.find_element(By.ID, "nest-messages_email").send_keys("tester100@gmail.com")
    driver.find_element(By.ID, "nest-messages_soDT").send_keys("0987674725")
    # Select
    select_element = driver.find_element(By.CLASS_NAME, "ant-select-selector")
    select_element.click()
    
    wait = WebDriverWait(driver, 10)
    dropdown_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@title='Học viên']"))
    )
    
    dropdown_option.click()
    time.sleep(2)

    # Thêm người dùng
    driver.find_element(By.XPATH, "//button[span[text()='Thêm người dùng']]").click()
    time.sleep(2)

    # Expected result 1
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Thêm thành công" in message_element.text

    # Step 5
    driver.find_element(By.XPATH, "//a[contains(text(), 'Quay lại trang trước')]").click()
    time.sleep(2)

    # Step 6
    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm tài khoản hoặc họ tên']").send_keys("tester100")
    driver.find_element(By.CLASS_NAME, "button_buttonSearchAdmin__xdlis").click()
    time.sleep(2)

    # Expected result 2
    assert driver.find_element(By.XPATH, "//td[text()='tester001']")


# Testcase 2: Cập nhật người dùng
def test_QLND_002(driver):
    # Steps
    test_DH_QLND(driver)
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm tài khoản hoặc họ tên']").send_keys("test01")
    driver.find_element(By.CLASS_NAME, "button_buttonSearchAdmin__xdlis").click()
    time.sleep(2)

    WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'btn-warning')]")) 
    ).click()
    time.sleep(2)

    # Cập nhật form
    ho_ten_element = driver.find_element(By.ID, "nest-messages_hoTen")
    email_element = driver.find_element(By.ID, "nest-messages_email")
    soDT_element = driver.find_element(By.ID, "nest-messages_soDT")

    clear_field(ho_ten_element)
    clear_field(email_element)
    clear_field(soDT_element)

    ho_ten_element.send_keys("tester100 updated")
    email_element.send_keys("test100updated@gmail.com")
    soDT_element.send_keys("0987678732")

    select_element = driver.find_element(By.CLASS_NAME, "ant-select-selector")
    select_element.click()

    dropdown_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@title='Giáo vụ']"))
    )
    dropdown_option.click()
    time.sleep(2)
    
    # Nhấn nút lưu
    driver.find_element(By.XPATH, "//button[span[text()='Lưu']]").click()

    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Cập nhật thành công" in message_element.text

    assert "https://elearning-app-rm1o.vercel.app/admin/quanlynguoidung" in driver.current_url


# Testcase 3: Xoá người dùng khi người đó chưa đăng ký khoá học nào
def test_QLND_003(driver):
    # Steps
    # test_QLND_009(driver)
    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm tài khoản hoặc họ tên']").send_keys("tester100")
    driver.find_element(By.CLASS_NAME, "button_buttonSearchAdmin__xdlis").click()
    time.sleep(2)
    # Xoá
    WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-danger')]/i[contains(@class, 'fa-trash')]")) 
    ).click()
    time.sleep(2)

    driver.switch_to.alert.accept()
    time.sleep(2)

    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Xoá thành công" in message_element.text


# Testcase 4: Xoá người dùng khi người đó đã đăng ký khoá học
def test_QLND_004(driver):
    # Steps
    test_DH_QLND(driver)
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm tài khoản hoặc họ tên']").send_keys("newuser")
    driver.find_element(By.CLASS_NAME, "button_buttonSearchAdmin__xdlis").click()
    time.sleep(2)
    # Xoá
    WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-danger')]/i[contains(@class, 'fa-trash')]")) 
    ).click()
    time.sleep(2)

    driver.switch_to.alert.accept()
    time.sleep(2)

    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Người dùng đã được ghi danh không thể xóa!" in message_element.text


# Testcase 5: Kiểm tra chức năng xét duyệt khoá học mà người dùng đã đăng ký
def test_QLND_005(driver):
    # Steps
    test_DH_QLND(driver)
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm tài khoản hoặc họ tên']").send_keys("newuser")
    driver.find_element(By.CLASS_NAME, "button_buttonSearchAdmin__xdlis").click()
    time.sleep(2)

    # Ghi danh
    driver.find_element(By.XPATH, "//a[text()='Ghi danh']").click()
    time.sleep(2)

    driver.find_element(By.ID, "btn_XT_KH").click()
    time.sleep(2)

    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Ghi danh thành công" in message_element.text

    khoa_hoc_element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//tr[@data-row-key='Javascript nâng cao']")) ) 
    assert "Javascript nâng cao" in khoa_hoc_element.text


# Testcase 6: Kiểm tra chức năng huỷ đăng ký khoá học
def test_QLND_006(driver):
    # Steps
    test_DH_QLND(driver)
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm tài khoản hoặc họ tên']").send_keys("newuser")
    driver.find_element(By.CLASS_NAME, "button_buttonSearchAdmin__xdlis").click()
    time.sleep(2)

    # Ghi danh
    driver.find_element(By.XPATH, "//a[text()='Ghi danh']").click()
    time.sleep(2)

    driver.find_element(By.ID, "btn_Huy_XT_KH").click()
    time.sleep(2)

    driver.switch_to.alert.accept()
    time.sleep(2)

    # Expected result
    # 1
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Huỷ ghi danh thành công" in message_element.text
    # 2


# Testcase 7: Kiểm tra chức năng huỷ khoá học người dùng đã tham gia
def test_QLND_007(driver):
    # Steps
    test_DH_QLND(driver)
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm tài khoản hoặc họ tên']").send_keys("newuser")
    driver.find_element(By.CLASS_NAME, "button_buttonSearchAdmin__xdlis").click()
    time.sleep(2)

    # Ghi danh
    driver.find_element(By.XPATH, "//a[text()='Ghi danh']").click()
    time.sleep(2)

    driver.find_element(By.ID, "btn_Huy_GD_KH").click()
    time.sleep(2)

    driver.switch_to.alert.accept()
    time.sleep(2)

    # Expected result
    # 1
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Huỷ ghi danh thành công" in message_element.text
    # 2


# Testcase 8: Chọn khoá học để đăng ký cho người dùng
def test_QLND_008(driver):
    # Steps
    test_DH_QLND(driver)
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm tài khoản hoặc họ tên']").send_keys("newuser")
    driver.find_element(By.CLASS_NAME, "button_buttonSearchAdmin__xdlis").click()
    time.sleep(2)

    # Ghi danh
    driver.find_element(By.XPATH, "//a[text()='Ghi danh']").click()
    time.sleep(2)

    select_element = driver.find_element(By.CLASS_NAME, "ant-select-selection-search")
    select_element.click()   
    dropdown_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@title='Javascript nâng cao']"))
    )
    dropdown_option.click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[span[text()='Ghi danh']]").click()
    time.sleep(2)

    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Ghi danh thành công" in message_element.text

    khoa_hoc_element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//tr[@data-row-key='Javascript nâng cao']")) ) 
    assert "Javascript nâng cao" in khoa_hoc_element.text


# Testcase 9: Tìm kiếm người dùng
def test_QLND_009(driver):
    test_DH_QLND(driver)
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm tài khoản hoặc họ tên']").send_keys("tester001")
    driver.find_element(By.CLASS_NAME, "button_buttonSearchAdmin__xdlis").click()
    time.sleep(2)

    assert driver.find_element(By.XPATH, "//td[text()='tester001']")
