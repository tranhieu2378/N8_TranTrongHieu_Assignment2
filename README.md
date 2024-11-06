# README - Kiểm Thử Tự Động Cho Web E-Learning

## Giới Thiệu
Kiểm thử tự động web E-learning là quá trình phát triển và thực hiện các kịch bản kiểm thử tự 
động sử dụng Selenium để kiểm tra và đảm bảo rằng các tính năng trên nền tảng học trực tuyến 
hoạt động đúng như mong đợi và mang lại trải nghiệm người dùng mượt mà. Quá trình này bao 
gồm việc kiểm tra các chức năng chính như đăng ký tài khoản, đăng nhập, đăng ký khóa học, quản 
lý thông tin cá nhân và tham gia các khóa học. Để đảm bảo tất cả các tác vụ quản trị đều hoạt 
động ổn định. Các kịch bản kiểm thử tự động sẽ được thực thi và tạo ra các báo cáo kiểm thử toàn 
diện. 

## Đường dẫn trang web

url(https://elearning-app-rm1o.vercel.app)

## Công Nghệ Sử Dụng
- **Ngôn ngữ**: Python
- **Thư viện kiểm thử**: Selenium WebDriver
- **Framework**: Pytest
- **Công cụ khác**: ChromeDriver

## Cấu Trúc Dự Án
```plaintext
├── README.md
├── __pycache__
├── test_CapNhatTK.py
├── test_DangKy.py
├── test_DangNhap.py
├── test_DangXuat.py
├── test_DieuHuong.py
├── test_DK_KhoaHoc.py
├── test_HoTroKH.py
├── test_HuyDangKy.py
└── test_TimKiem.py
```

## Các TestCase bao gồm

1. **Đăng Nhập**: `test_DangNhap.py`
   - test_TK_001: Kiểm tra đăng nhập với tài khoản và mật khẩu chính xác
   - test_DN_002: Kiểm tra đăng nhập với tài khoản hoặc mật khẩu không chính xác
   - test_DN_003: Kiểm tra đăng nhập với tài khoản hoặc mật khẩu để trống
   - test_DN_004: Kiểm tra đăng nhập bằng tài khoản admin
   
2. **Đăng Ký**: `test_DangKy.py`
   - test_DK_001: Kiểm tra đăng ký thành công 
   - test_DK_002: Kiểm tra đăng ký khi trùng tài khoản 
   - test_DK_003: Kiểm tra đăng ký trùng email 
   - test_DK_004: Kiểm tra đăng ký khi để form rỗng
   - test_DK_005: Kiểm tra đăng ký khi nhập sai định dạng 

3. **Đăng Xuất**: `test_DangXuat.py`
   - test_DX_001: Kiểm tra đăng xuất 

4. **Kiểm Tra Điều Hướng và Liên Kết**: `test_DieuHuong.py`
   - test_DH_001: Kiểm tra điều hướng đến trang thông tin tài khoản khi chưa đăng nhập 
   - test_DH_002: Kiểm tra điều hướng đến trang admin khi chưa đăng nhập 
   - test_DH_003: Kiểm tra điều hướng đến trang admin khi đăng nhập tài khoản dưới quyền user 
   - test_DH_004: Kiểm tra liên kết đến trang khoá học
   - test_DH_005: Kiểm tra liên kết giữa các danh mục khoá học 

5. **Đăng Ký Khóa Học**: `test_DK_KhoaHoc.py`
   - test_DKkh_001: Kiểm tra đăng ký khoá học khi chưa đăng nhập
   - test_DKkh_002: Kiểm tra đăng ký khoá học thành công
   - test_DKkh_003: Kiểm tra đăng ký khoá học khi đã đăng ký 

6. **Hủy Đăng Ký Khóa Học**: `test_HuyDangKy.py`
   - test_CDK_001 : Kiểm tra huỷ đăng ký khoá học 

7. **Tìm Kiếm**: `test_TimKiem.py`
   - test_TK_001: Kiểm tra tìm kiếm khoá học có trong dữ liệu 
   - test_TK_002: Kiểm tra tìm kiếm khoá học không có trong dữ liệu
   - test_TK_003: Kiểm tra tìm kiếm khoá học với ký tự đặc biệt (Ký tự #) 
   - test_TK_004: Kiểm tra tìm kiếm khoá học với ký tự đặc biệt (Ký tự %) 

8. **Cập Nhật Thông Tin Tài Khoản**: `test_CapNhatTK.py`
   - test_UTK_001: Kiểm tra chức năng cập nhật thông tin tài khoản thành công
   - test_UTK_002: Kiểm tra chức năng cập nhật thông tin tài khoản khi nhập sai định dạng  
   - test_UTK_003: Kiểm tra chức năng cập nhật không tin tài khoản khi để trống thông tin 

9. **Hỗ Trợ Khách Hàng**: `test_HoTroKH.py`
   - test_HT_001: Kiểm tra chức năng đăng ký tư vấn 
   - test_HT_002: Kiểm tra chức năng nhận tin tức khuyến mãi   
