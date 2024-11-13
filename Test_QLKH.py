import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Test_DieuHuong import test_DH_QLKH
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Testcase 1: Thêm khoá học
def test_QLKH_001(driver):
    # Steps
    test_DH_QLKH(driver)
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[contains(text(), 'Thêm khoá học')]").click()
    time.sleep(2)

    driver.find_element(By.ID, "maKhoaHoc").send_keys("LTDDFT_002")
    driver.find_element(By.ID, "tenKhoaHoc").send_keys("Lập trình di động với Flutter")
    driver.find_element(By.ID, "ngayTao").send_keys("2024-11-04")
    driver.find_element(By.ID, "danhGia").send_keys("5")
    driver.find_element(By.ID, "luotXem").send_keys("100")
    driver.find_element(By.ID, "moTa").send_keys("Khoá học Lập trình di động với Flutter được thiết kế để cung cấp cho người học những kiến thức từ cơ bản đến nâng cao trong việc phát triển ứng dụng di động đa nền tảng bằng Flutter, một framework hiện đại của Google. Flutter cho phép các lập trình viên viết mã một lần và triển khai trên cả Android và iOS, giúp tiết kiệm thời gian, công sức và tăng tính nhất quán cho ứng dụng trên nhiều nền tảng khác nhau.")   
    # Select
    select_element = driver.find_element(By.ID, "danhMucKhoaHoc")
    select_element.click()
    wait = WebDriverWait(driver, 10)
    dropdown_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@title='Lập trình di động']"))
    ) 
    dropdown_option.click()
    time.sleep(2)
    # 
    driver.find_element(By.ID, "nguoiTao").click()
    dropdown_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@title='Trần Văn B']"))
    ) 
    dropdown_option.click()
    time.sleep(2)
    # Upload
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, 'img', 'flutter.png') 
    file_input = driver.find_element(By.ID, "upload")
    file_input.send_keys(path)
    time.sleep(2)

    # 
    driver.find_element(By.XPATH, "//button[span[text()='Thêm']]").click()
    time.sleep(2)

    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Thêm khóa học thành công" in message_element.text

    # Step 5
    driver.find_element(By.XPATH, "//a[contains(text(), 'Quay lại trang trước')]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm mã hoặc tên khoá học']").send_keys("LTDD_001")
    driver.find_element(By.XPATH, "//button[text()='Tìm kiếm']").click()
    time.sleep(2)

    # Expected result 2
    assert driver.find_element(By.XPATH, "//td[text()='LTDD_001']")




# Testcase 2: Cập nhật khoá học



# Testcase 3: Xoá khoá học khi chưa có học viên đăng ký
def test_QLKH_003(driver):
    # Steps
    test_DH_QLKH(driver)
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm mã hoặc tên khoá học']").send_keys("Mã khoá học chưa có hv đki")
    driver.find_element(By.XPATH, "//button[text()='Tìm kiếm']").click()
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
    assert "Xoá thành công" in message_element.text


# Testcase 4: Xoá khoá học khi đã có học viên đăng ký
def test_QLKH_004(driver):
    test_QLKH_009(driver)
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
    assert "Khóa học đã ghi danh học viên không thể xóa!" in message_element.text


# Testcase 5: Kiểm tra chức năng xét duyệt người dùng đã đăng ký khoá học
def test_QLKH_005(driver):
    test_QLKH_009(driver)
    time.sleep(2)

    # Ghi danh
    WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Ghi danh']")) 
    ).click()
    time.sleep(2)

    driver.find_element(By.ID, "btn_XT_HV").click()

    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Ghi danh thành công" in message_element.text

    # khoa_hoc_element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//tr[@data-row-key='Javascript nâng cao']")) ) 
    # assert "Javascript nâng cao" in khoa_hoc_element.text


# Testcase 6: Kiểm tra chức năng từ chối học viên đăng ký khoá học
def test_QLKH_006(driver):
    # Steps
    test_QLKH_009(driver)
    time.sleep(2)

    WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Ghi danh']")) 
    ).click()
    time.sleep(2)

    driver.find_element(By.ID, "btn_Huy_XT_HV").click()

    driver.switch_to.alert.accept()
    time.sleep(2)

    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Huỷ ghi danh thành công" in message_element.text


# Testcase 7: Kiểm tra chức năng xoá học viên khỏi khoá học
def test_QLKH_007(driver):
    test_QLKH_009(driver)
    time.sleep(2)

    WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Ghi danh']")) 
    ).click()
    time.sleep(2)

    # Huỷ
    driver.find_element(By.ID, "btn_Huy_GD_HV").click()

    driver.switch_to.alert.accept()
    time.sleep(2)

    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Huỷ ghi danh thành công" in message_element.text


# Testcase 8: Kiểm tra chức năng đăng ký người dùng vào khoá học đã chọn
def test_QLKH_008(driver):
    test_QLKH_009(driver)
    time.sleep(2)

    # Ghi danh
    WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Ghi danh']")) 
    ).click()
    time.sleep(2)

    driver.find_element(By.ID, "formKhChuaDk_taiKhoan").send_keys("Trần Trọng Hiếu")
 
    dropdown_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@title='Trần Trọng Hiếu']"))
    )
    dropdown_option.click()
    time.sleep(2)
    # Click
    driver.find_element(By.XPATH, "//button[span[text()='Ghi danh']]").click()
    time.sleep(2)

    # Expected result
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ant-message-notice-content"))
    )
    assert "Ghi danh thành công" in message_element.text



# Testcase 9: Tìm kiếm khoá học
def test_QLKH_009(driver):
    test_DH_QLKH(driver)
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm mã hoặc tên khoá học']").send_keys("FT002")
    driver.find_element(By.XPATH, "//button[text()='Tìm kiếm']").click()
    time.sleep(2)

    assert driver.find_element(By.XPATH, "//td[text()='FT002']")


# Testcase 10: Tìm kiếm Học viên chờ xác thực



# Testcase 11: Tìm kiếm học viên đã ghi danh