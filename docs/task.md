# PLAN CHI TIẾT - PHẦN MỀM QUẢN LÝ ĐẠI LÝ XE HƠI

## MỤC TIÊU TỔNG THỂ
Xây dựng hệ thống quản lý đại lý xe hơi console-based bằng Python, tuân thủ kiến trúc MVC, hỗ trợ đầy đủ 7 chức năng nghiệp vụ với hiệu năng và bảo mật theo yêu cầu.

## GIAI ĐOẠN 1: THIẾT LẬP CƠ SỞ (Tuần 1)

### 1.1 Thiết lập database
- [ ] Tạo schema SQLite với 6 bảng chính:
  - `cars` (mã_xe, hãng, dòng_xe, năm_sx, màu_sắc, giá_bán, tồn_kho)
  - `customers` (id, họ_tên, sđt, email, phân_loại)
  - `employees` (id, họ_tên, vai_trò, sđt, email)
  - `contracts` (id, mã_xe, khách_hàng_id, nhân_viên_id, giá_trị, trạng_thái)
  - `inventory` (id, mã_xe, số_lượng, ngày_cập_nhật)
  - `audit_logs` (id, người_dùng, hành_động, thời_gian)

### 1.2 Xây dựng cấu trúc project
- [ ] Tạo thư mục `src/btl_python/database/` với connection manager
- [ ] Implement CRUD cơ bản cho database
- [ ] Viết unit test đầu tiên cho database connection

## GIAI ĐOẠN 2: TRIỂN KHAI MODULE CỐT LÕI (Tuần 2-4)

### 2.1 Module quản lý xe (feature/car-management)
- [ ] Model `Car` với validation dữ liệu
- [ ] Controller xử lý: thêm/sửa/xóa/tìm kiếm xe
- [ ] View console cho quản lý xe
- [ ] Unit test toàn bộ chức năng

### 2.2 Module quản lý khách hàng (feature/customer-management)  
- [ ] Model `Customer` với logic phân loại tự động
- [ ] Controller quản lý thông tin và lịch sử giao dịch
- [ ] View console tương ứng
- [ ] Unit test

### 2.3 Module quản lý hợp đồng (feature/contract-management)
- [ ] Model `Contract` với tính toán giá trị tự động
- [ ] Controller tạo/quản lý hợp đồng
- [ ] View console + export PDF (dùng thư viện reportlab)
- [ ] Unit test

## GIAI ĐOẠN 3: MODULE NÂNG CAO (Tuần 5-6)

### 3.1 Module quản lý nhân viên & phân quyền
- [ ] Model `Employee` với hệ thống vai trò
- [ ] Controller phân quyền truy cập
- [ ] View console với menu theo quyền

### 3.2 Module quản lý kho
- [ ] Model `Inventory` với cảnh báo tồn kho
- [ ] Controller cập nhật tồn kho tự động từ hợp đồng
- [ ] View hiển thị tồn kho và cảnh báo

### 3.3 Module báo cáo thống kê
- [ ] Controller tổng hợp dữ liệu doanh thu, top xe, KPI
- [ ] View hiển thị báo cáo dạng bảng

## GIAI ĐOẠN 4: HỆ THỐNG & BẢO MẬT (Tuần 7)

### 4.1 Hệ thống đăng nhập & bảo mật
- [ ] Model `User` với mã hóa bcrypt
- [ ] Controller xử lý đăng nhập/đăng xuất
- [ ] Session management với timeout 30 phút
- [ ] Audit trail logging

### 4.2 Giao diện console hoàn chỉnh
- [ ] Menu chính thống nhất
- [ ] Xử lý lỗi và validation input
- [ ] Hướng dẫn sử dụng tích hợp

## GIAI ĐOẠN 5: TEST & TRIỂN KHAI (Tuần 8)

### 5.1 Testing toàn diện
- [ ] Unit test cho tất cả module (>90% coverage)
- [ ] Integration test cho luồng nghiệp vụ chính
- [ ] Performance test theo yêu cầu phi chức năng

### 5.2 Documentation hoàn chỉnh
- [ ] Cập nhật tài liệu kỹ thuật
- [ ] Viết hướng dẫn sử dụng chi tiết
- [ ] Chuẩn bị demo

### 5.3 Triển khai production
- [ ] Build final version
- [ ] Test trên multi-platform (Windows/Linux/macOS)
- [ ] Release v1.0

## CÔNG CỤ & CÔNG NGHỆ
- **Database**: SQLite → PostgreSQL (nếu cần mở rộng)
- **Testing**: pytest + coverage
- **PDF Export**: reportlab
- **Security**: bcrypt cho mật khẩu
- **Code Style**: PEP 8 + comment tiếng Việt

## PHÂN CÔNG NHÓM
- **Nguyễn Văn Hiếu (Trưởng nhóm)**: Tổng thể + Database + Security
- **Lê Minh Đạt**: Module xe + khách hàng + kho  
- **Nguyễn Hữu Hải**: Module hợp đồng + báo cáo + giao diện

## KPI THÀNH CÔNG
✅ Đáp ứng 100% yêu cầu chức năng  
✅ Hiệu năng ≤ 2s cho tìm kiếm xe (10k records)  
✅ Bảo mật theo nguyên tắc least privilege  
✅ Code coverage > 90%  
✅ Tài liệu đầy đủ tiếng Việt