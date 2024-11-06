import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Test_DangNhap import test_DN_001, test_DN_004

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Testcase 1: Điều hướng đến trang thông tin tài khoản khi chưa đăng nhập
def test_DH_001(driver):
    # Steps
    driver.get('https://elearning-app-rm1o.vercel.app/thongtintaikhoan')
    time.sleep(2)
    # Expected result
    assert "https://elearning-app-rm1o.vercel.app/not-found" in driver.current_url

# Testcase 2: Điều hướng đến trang admin khi chưa đăng nhập
def test_DH_002(driver):
    # Steps
    driver.get('https://elearning-app-rm1o.vercel.app/admin/quanlynguoidung')
    time.sleep(2)
    # Expected result
    assert "https://elearning-app-rm1o.vercel.app/not-found" in driver.current_url

# Testcase 3: Điều hướng đến trang admin khi đăng nhập dưới quyền user 
def test_DH_003(driver):
    # Steps
    test_DN_001(driver)
    time.sleep(2)

    driver.get('https://elearning-app-rm1o.vercel.app/admin/quanlynguoidung')
    time.sleep(2)

    # Expect result
    assert "https://elearning-app-rm1o.vercel.app/not-found" in driver.current_url

# Testcase 4: kiểm tra liên kết đến trang khoá học
def test_DH_004(driver):
    # Steps
    driver.get('https://elearning-app-rm1o.vercel.app/')
    driver.find_element(By.XPATH, "//a[text()='Khoá học']").click()
    time.sleep(2)
    
    # Expected result
    assert driver.find_element(By.CLASS_NAME, "title_title_content__0p8XV").text == 'KHOÁ HỌC'

# Testcase 5: Kiểm tra liên kết giữa các danh mục khoá học
def test_DH_005(driver):
    # Steps
    driver.get('https://elearning-app-rm1o.vercel.app/')
    element = driver.find_element(By.XPATH, "//a[text()='Danh mục khoá học']")
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[text()='Lập trình Backend']").click()
    time.sleep(5)
    # Expected result
    assert driver.find_element(By.CLASS_NAME, "title_title_content__0p8XV").text == 'Lập trình Backend'

# 
def test_DH_ChiTiet(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    element = driver.find_element(By.CLASS_NAME, "card_cardContent__UzyxP")
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()
    time.sleep(2)
    element.click()
    time.sleep(6)
    assert driver.find_element(By.CLASS_NAME, "title_title_content__0p8XV").text == 'Thông tin khoá học'

def test_DH_ThongTinTK(driver):
    driver.get('https://elearning-app-rm1o.vercel.app/')
    test_DN_001(driver)
    driver.find_element(By.CLASS_NAME, "userDropdown_dropdownTrigger__TO32H").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "userDropdown_dropdownMenu__6DtQw"))
    )
    driver.find_element(By.XPATH, "//a[text()='Thông tin']").click()

    titleProfile = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "thongtintaikhoan_profTitle__Y4ntt"))
    )

    assert EC.visibility_of_all_elements_located((By.CLASS_NAME, "thongtintaikhoan_profTitle__Y4ntt"))

# def test_DH_QLKH(driver):
#     test_DN_004(driver)
#     time.sleep(2)

#     driver.find_element(By.XPATH, "//a[text()='Trang quản trị']").click()
#     time.sleep(2)

#     WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "title_title_content__0p8XV"))
#     )

#     assert driver.find_element(By.CLASS_NAME, "title_title_content__0p8XV").text == "Quản lý khoá học"

# def test_DH_QLND(driver):
#     test_DN_004(driver)
#     time.sleep(2)
    
#     driver.find_element(By.XPATH, "//a[text()='Trang quản trị']").click()
#     time.sleep(2)

#     driver.find_element(By.XPATH, "//a[span[text()='Quản lý người dùng']]").click()
#     time.sleep(2)

#     WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "title_title_content__0p8XV"))
#     )

#     assert driver.find_element(By.CLASS_NAME, "title_title_content__0p8XV").text == "Quản lý người dùng"