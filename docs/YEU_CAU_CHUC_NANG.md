# YÊU CẦU HỆ THỐNG  
**Phần mềm quản lý đại lý xe hơi**

## 1. PHÂN TÍCH CHỨC NĂNG

### 1.1 Quản lý thông tin xe
- **Mô tả**: Hệ thống cho phép quản lý toàn bộ thông tin về các dòng xe có trong đại lý
- **Chi tiết**:
  - Thêm mới xe với thông tin: mã xe, hãng, dòng xe, năm sản xuất, màu sắc, giá bán, số lượng tồn kho
  - Chỉnh sửa thông tin xe (trừ mã xe)
  - Xóa xe chỉ khi chưa có hợp đồng liên quan
  - Tìm kiếm nâng cao theo nhiều tiêu chí kết hợp
  - Lọc xe theo trạng thái: còn hàng / đã bán / sắp về

### 1.2 Quản lý khách hàng
- **Mô tả**: Lưu trữ và quản lý thông tin khách hàng mua xe tại đại lý
- **Chi tiết**:
  - Thêm mới khách hàng với thông tin bắt buộc: họ tên, SĐT, email
  - Cập nhật thông tin khách hàng
  - Xem lịch sử giao dịch đầy đủ của từng khách hàng
  - Phân loại tự động dựa trên số lần mua và tổng giá trị

### 1.3 Quản lý nhân viên
- **Mô tả**: Quản lý thông tin và phân quyền cho nhân viên trong đại lý
- **Chi tiết**:
  - Quản trị viên có thể thêm/xóa/sửa mọi nhân viên
  - Nhân viên bán hàng chỉ xem được thông tin của mình
  - Theo dõi KPI: số xe bán được, doanh thu tạo ra

### 1.4 Quản lý hợp đồng bán xe
- **Mô tả**: Tạo và quản lý hợp đồng bán xe giữa đại lý và khách hàng
- **Chi tiết**:
  - Tự động tính toán giá trị hợp đồng
  - Hỗ trợ thêm phụ kiện và khuyến mãi
  - Trạng thái hợp đồng: mới tạo / đã thanh toán / đã giao xe
  - In hợp đồng dưới dạng PDF chuyên nghiệp

### 1.5 Quản lý kho xe
- **Mô tả**: Theo dõi số lượng tồn kho và cảnh báo khi cần nhập hàng
- **Chi tiết**:
  - Cập nhật tồn kho tự động khi có hợp đồng mới
  - Cảnh báo khi tồn kho dưới mức tối thiểu
  - Lịch sử nhập kho từ nhà cung cấp

### 1.6 Báo cáo thống kê
- **Mô tả**: Cung cấp các báo cáo kinh doanh theo nhiều chiều dữ liệu
- **Chi tiết**:
  - Doanh thu theo thời gian (ngày/tháng/năm)
  - Top 10 xe bán chạy nhất
  - Hiệu suất nhân viên theo KPI
  - Khách hàng VIP theo tổng giá trị mua hàng

### 1.7 Hệ thống bảo mật
- **Mô tả**: Đảm bảo an toàn thông tin và phân quyền truy cập
- **Chi tiết**:
  - Đăng nhập bằng tài khoản/mật khẩu
  - Mã hóa mật khẩu theo chuẩn bcrypt
  - Ghi log mọi hoạt động quan trọng
  - Session timeout sau 30 phút không hoạt động

## 2. YÊU CẦU PHI CHỨC NĂNG

### 2.1 Hiệu năng
- Thời gian phản hồi tìm kiếm xe: ≤ 2 giây với cơ sở dữ liệu 10.000 bản ghi
- Thời gian tải danh sách khách hàng: ≤ 1 giây
- Hỗ trợ đồng thời 50 người dùng

### 2.2 Độ tin cậy
- Tỷ lệ lỗi hệ thống: < 0.1%
- Dữ liệu được backup tự động hàng ngày
- Khả năng phục hồi sau sự cố: ≤ 15 phút

### 2.3 Bảo mật
- Tuân thủ nguyên tắc least privilege (phân quyền tối thiểu)
- Mã hóa dữ liệu nhạy cảm khi lưu trữ
- Không lưu trữ mật khẩu dưới dạng plain text
- Audit trail cho mọi thay đổi dữ liệu quan trọng

### 2.4 Khả năng sử dụng
- Giao diện thân thiện, dễ sử dụng cho người không rành công nghệ
- Hỗ trợ thao tác bằng bàn phím và chuột
- Có hướng dẫn sử dụng tích hợp trong hệ thống
- Thời gian đào tạo nhân viên mới: ≤ 2 giờ

### 2.5 Khả năng bảo trì
- Mã nguồn được comment đầy đủ bằng tiếng Việt
- Kiến trúc module, dễ mở rộng tính năng
- Có unit test cho các hàm nghiệp vụ chính
- Tài liệu kỹ thuật đầy đủ

### 2.6 Tính khả chuyển
- Chạy được trên Windows, Linux, macOS
- Không phụ thuộc vào phiên bản hệ điều hành cụ thể
- Dễ dàng di chuyển cơ sở dữ liệu sang hệ thống khác