# Xây dựng phần mềm quản lý đại lý xe hơi

## Thành viên nhóm
- Nguyễn Văn Hiếu (Trưởng nhóm)
- Lê Minh Đạt
- Nguyễn Hữu Hải

## Cấu trúc dự án
```
Btl-Python/
├── src/                    # Mã nguồn chính
│   ├── btl_python/        # Package chính (sẽ phát triển)
│   └── demo/              # Demo giao diện PyQt6
│       ├── main_demo.py
│       ├── main_window_demo.py
│       ├── styles/
│       └── views/
├── tests/                  # Unit tests
├── docs/                   # Tài liệu hệ thống
├── diagrams/              # Sơ đồ UML
├── requirements.txt       # Danh sách thư viện
└── README.md
```

## 🚀 Hướng dẫn chạy Demo Giao Diện

### Bước 1: Clone repository
```bash
git clone https://github.com/vanhieu25/Btl-Python.git
cd Btl-Python
```

### Bước 2: Tạo virtual environment (khuyến nghị)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Bước 3: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

**Lưu ý:** File `requirements.txt` cần có:
```
PyQt6>=6.4.0
```

Nếu chưa có PyQt6, cài đặt trực tiếp:
```bash
pip install PyQt6
```

### Bước 4: Chạy Demo
```bash
cd src/demo
python main_demo.py
```

Hoặc chạy từ root:
```bash
python src/demo/main_demo.py
```

### 🎨 Các màn hình Demo

| Màn hình | Mô tả | Đường dẫn |
|----------|-------|-----------|
| **Dashboard** | Tổng quan với 4 cards, biểu đồ placeholder, HĐ gần đây | `views/dashboard_demo.py` |
| **Quản lý Xe** | Bảng xe, search/filter, dialog thêm/sửa | `views/xe_demo.py` |
| **Khách Hàng** | Tabs Cá nhân/Doanh nghiệp, dialog chi tiết + lịch sử | `views/khach_hang_demo.py` |
| **Hợp Đồng** | Stats cards, filter trạng thái, dialog tạo/xem | `views/hop_dong_demo.py` |

### 📋 Yêu cầu hệ thống
- **Python**: 3.10 trở lên
- **PyQt6**: 6.4+
- **OS**: Windows 10/11, macOS 10.14+, Ubuntu 20.04+

### 🛠️ Cấu trúc Demo
```
src/demo/
├── main_demo.py              # Entry point
├── main_window_demo.py       # MainWindow với sidebar
├── styles/
│   └── notion_theme.qss     # Stylesheet Notion-inspired
└── views/
    ├── dashboard_demo.py    # Dashboard view
    ├── xe_demo.py           # Quản lý Xe
    ├── khach_hang_demo.py   # Quản lý Khách Hàng
    └── hop_dong_demo.py     # Quản lý Hợp Đồng
```

### 📝 Tech Stack Demo
- **GUI Framework**: PyQt6
- **Design**: Notion-inspired (warm neutrals, whisper borders)
- **Database**: Chưa cần (chỉ UI)
- **Icons**: Emoji + Unicode

## 📚 Tài liệu
- [Yêu cầu chức năng](docs/YEU_CAU_CHUC_NANG.md)
- [Đặc tả kỹ thuật](docs/SPEC.md)
- [Tech Stack](docs/TECH_STACK.md)
- [Hướng dẫn tạo Demo](docs/TASKDEMO.md)

## Đóng góp
Xem hướng dẫn đóng góp chi tiết tại [CONTRIBUTORS.md](CONTRIBUTORS.md)

## Giấy phép
Xem chi tiết tại [LICENSE](LICENSE).