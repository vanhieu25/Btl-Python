# ĐẶC TẢ KỸ THUẬT  
**Phần mềm quản lý đại lý xe hơi**

## 1. TỔNG QUAN HỆ THỐNG

### 1.1 Mục tiêu
Xây dựng hệ thống quản lý toàn diện cho đại lý xe hơi bao gồm: quản lý xe, khách hàng, nhân viên, hợp đồng, kho bãi và báo cáo kinh doanh.

### 1.2 Phạm vi
- Quản lý thông tin xe và tồn kho
- Quản lý thông tin khách hàng và lịch sử giao dịch  
- Quản lý nhân viên và phân quyền
- Tạo và quản lý hợp đồng bán xe
- Báo cáo thống kê kinh doanh
- Hệ thống bảo mật và audit trail

### 1.3 Người dùng mục tiêu
- Quản trị viên đại lý
- Nhân viên bán hàng
- Nhân viên kho
- Khách hàng (chế độ xem công khai)

## 2. KIẾN TRÚC PHẦN MỀM

### 2.1 Kiến trúc tổng thể
- **Mô hình**: MVC (Model-View-Controller)
- **Kiểu ứng dụng**: Ứng dụng desktop console (Python + SQLite ban đầu)
- **Mở rộng**: Có thể phát triển thành web app sau này

### 2.2 Các module chính
```
src/btl_python/
├── models/          # Các model dữ liệu
├── controllers/     # Logic nghiệp vụ
├── views/           # Giao diện console
├── utils/           # Các hàm tiện ích
├── database/        # Quản lý kết nối database
└── main.py          # Entry point
```

### 2.3 Luồng dữ liệu
1. Người dùng nhập liệu qua console
2. Controller xử lý logic nghiệp vụ
3. Model tương tác với database
4. View hiển thị kết quả cho người dùng

## 3. THIẾT KẾ DATABASE

### 3.1 Các bảng chính
- **cars**: Thông tin xe
- **customers**: Thông tin khách hàng  
- **employees**: Thông tin nhân viên
- **contracts**: Hợp đồng bán xe
- **inventory**: Quản lý tồn kho
- **audit_logs**: Nhật ký hệ thống

### 3.2 Mối quan hệ
- Một khách hàng có nhiều hợp đồng
- Một nhân viên tạo nhiều hợp đồng
- Một hợp đồng liên kết một xe và một khách hàng
- Mỗi xe có nhiều bản ghi tồn kho theo thời gian

## 4. CÔNG NGHỆ SỬ DỤNG

### 4.1 Backend
- **Ngôn ngữ**: Python 3.8+
- **Database**: SQLite (ban đầu), có thể mở rộng sang PostgreSQL
- **ORM**: SQLAlchemy (nếu cần)

### 4.2 Frontend  
- **Giao diện**: Console-based (cmd/terminal)
- **Thư viện**: Built-in Python libraries

### 4.3 Công cụ hỗ trợ
- **Version control**: Git + GitHub
- **Testing**: pytest
- **Documentation**: Markdown

## 5. YÊU CẦU TRIỂN KHAI

### 5.1 Môi trường phát triển
- Hệ điều hành: Windows/Linux/macOS
- Python 3.8+
- pip package manager

### 5.2 Cài đặt
```bash
# Clone repository
git clone https://github.com/vanhieu25/Btl-Python.git

# Cài dependencies  
pip install -r requirements.txt

# Chạy ứng dụng
python src/btl_python/main.py
```

### 5.3 Cấu trúc thư mục dự án
```
Btl-Python/
├── docs/                # Tài liệu
├── src/btl_python/      # Mã nguồn chính
├── tests/               # Unit tests
├── requirements.txt     # Dependencies
├── README.md            # Hướng dẫn tổng quan
└── LICENSE              # Giấy phép
```