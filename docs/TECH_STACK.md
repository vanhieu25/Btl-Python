# Tech Stack - Phần Mềm Quản Lý Đại Lý Xe Hơi

## 1. TỔNG QUAN CÔNG NGHỆ

| Thành phần | Công nghệ | Phiên bản | Lý do lựa chọn |
|------------|-----------|-----------|----------------|
| Ngôn ngữ lập trình | Python | 3.10+ | Dễ học, thư viện phong phú, cộng đồng lớn |
| GUI Framework | PyQt6 | 6.4+ | Hiện đại, đa nền tảng, giao diện chuyên nghiệp |
| Database | SQLite | 3.x | Nhẹ nhất, nhúng trong ứng dụng, không cần server |
| ORM | SQLAlchemy | 2.0+ | Trừu tượng hóa database, dễ bảo trì |
| Báo cáo PDF | ReportLab | 3.6+ | Xuất hợp đồng, hóa đơn PDF chuyên nghiệp |
| Bảo mật | bcrypt | 4.0+ | Mã hóa mật khẩu chuẩn industry |
| Testing | pytest | 7.x+ | Framework test mạnh mẽ, dễ sử dụng |

## 2. CHI TIẾT CÔNG NGHỆ

### 2.1 Python 3.10+
- **Vai trò**: Ngôn ngữ lập trình chính
- **Tính năng sử dụng**:
  - Type hints (gợi ý kiểu dữ liệu cho clean code)
  - Dataclasses (định nghĩa model nhanh chóng)
  - f-strings (xuất chuỗi tiện lợi)
  - Match/case (Python 3.10+, thay thế if-elif dài)
  - Walrus operator `:=` (gán trong expression)
- **Yêu cầu cài đặt**: Python 3.10 hoặc cao hơn

### 2.2 PyQt6 6.4+ ⭐ GUI FRAMEWORK
- **Vai trò**: Xây dựng giao diện người dùng đồ họa (GUI)
- **Ưu điểm vượt trội**:
  - Hiện đại, kế thừa và cải tiến từ PyQt5
  - Hỗ trợ đầy đủ Windows, macOS, Linux
  - Widgets phong phú: bảng, form, dialog, biểu đồ
  - StyleSheet tương tự CSS cho giao diện đẹp
  - Signals/Slots cho xử lý sự kiện mạnh mẽ
  - Hiệu suất cao, phản hồi nhanh
  - Hỗ trợ đa ngôn ngữ (tiếng Việt)
- **Thành phần chính sử dụng**:
  - `QMainWindow`: Cửa sổ chính ứng dụng
  - `QTableWidget`: Hiển thị danh sách xe, khách hàng, hợp đồng
  - `QFormLayout`: Form nhập liệu thông tin
  - `QDialog`: Cửa sổ dialog (thêm, sửa, xóa)
  - `QMessageBox`: Thông báo, cảnh báo, xác nhận
  - `QComboBox`, `QLineEdit`, `QDateEdit`: Input controls
  - `QPushButton`, `QToolBar`, `QMenuBar`: Tương tác người dùng
  - `QStackedWidget`: Chuyển đổi giữa các màn hình chức năng
  - `QTabWidget`: Tab cho nhiều chức năng
  - `QChart` (PyQt6-Charts): Biểu đồ báo cáo doanh thu

### 2.3 SQLite 3.x ⭐ DATABASE NHẸ NHẤT
- **Vai trò**: Cơ sở dữ liệu nhúng cho ứng dụng desktop
- **Tại sao chọn SQLite (tối ưu & nhẹ)**:
  - **Zero-configuration**: Không cần cài đặt, cấu hình server
  - **Serverless**: Database là file đơn giản (`quanlyxedaily.db`)
  - **Portable**: Copy file là chuyển được toàn bộ dữ liệu
  - **Nhẹ**: Chỉ ~500KB thư viện
  - **Nhanh**: Đủ nhanh cho ứng dụng desktop đơn lẻ
  - **Tích hợp Python**: Hỗ trợ native qua `sqlite3` module
  - **Transaction ACID**: Đảm bảo toàn vẹn dữ liệu
  - **Cross-platform**: Chạy trên mọi OS Python hỗ trợ
- **Khi nào cần nâng cấp**: Nếu cần đa người dùng remote hoặc web app → chuyển PostgreSQL
- **So sánh với lựa chọn khác**:
  | Database | Kích thước | Cài đặt | Server | Phù hợp |
  |----------|-----------|---------|--------|---------|
  | **SQLite** | ~500KB | Không cần | Không | ✅ **Desktop app** |
  | PostgreSQL | ~100MB | Cần cài | Cần | Web app, multi-user |
  | MySQL | ~200MB | Cần cài | Cần | Web app |
  | MongoDB | ~300MB | Cần cài | Cần | NoSQL, document |

### 2.4 SQLAlchemy 2.0+
- **Vai trò**: Object-Relational Mapping (ORM)
- **Chức năng**:
  - Ánh xạ Python classes ↔ Database tables
  - Truy vấn database bằng Python syntax thay vì SQL thuần
  - Quản lý transactions tự động
  - Migration database (kết hợp Alembic)
- **Lợi ích**:
  - Không viết SQL thủ công → giảm lỗi, tăng năng suất
  - Dễ bảo trì, refactor code
  - Hỗ trợ nhiều database (SQLite, PostgreSQL, MySQL)
  - Connection pooling tối ưu

### 2.5 ReportLab 3.6+
- **Vai trò**: Tạo file PDF báo cáo, hợp đồng, hóa đơn
- **Ứng dụng trong project**:
  - Xuất hợp đồng bán xe (mẫu chuẩn đại lý)
  - Hóa đơn thanh toán PDF
  - Báo cáo doanh thu, thống kê PDF
  - Phiếu xuất kho, nhập kho

### 2.6 bcrypt 4.0+
- **Vai trò**: Mã hóa mật khẩu người dùng
- **Tại sao cần**:
  - Bảo mật đăng nhập hệ thống
  - Tuân thủ tiêu chuẩn bảo mật
  - Chống rainbow table attacks
- **Cách dùng**: `bcrypt.hashpw(password, bcrypt.gensalt())`

### 2.7 pytest 7.x+
- **Vai trò**: Framework kiểm thử đơn vị (unit testing)
- **Tính năng**:
  - Fixtures cho setup/teardown
  - Parametrize cho test nhiều case
  - Coverage reporting (kết hợp pytest-cov)
  - Mocking (kết hợp unittest.mock)

## 3. CẤU TRÚC PROJECT VỚI PYQT6

```
Btl-Python/
├── main.py                    # Entry point - khởi động QApplication
├── requirements.txt           # Danh sách dependencies
├── README.md                  # Hướng dẫn
├── .gitignore                 # Loại trừ file
│
├── src/                       # Mã nguồn chính
│   ├── __init__.py
│   ├── main_window.py         # QMainWindow chính
│   ├── app.py                 # QApplication configuration
│   │
│   ├── gui/                   # Giao diện PyQt6
│   │   ├── __init__.py
│   │   ├── widgets/           # Custom widgets (bảng tùy chỉnh, v.v.)
│   │   ├── dialogs/           # QDialog (thêm, sửa, xóa, xác nhận)
│   │   ├── forms/             # Form nhập liệu
│   │   │   ├── xe_form.py
│   │   │   ├── khach_hang_form.py
│   │   │   ├── hop_dong_form.py
│   │   │   └── ...
│   │   ├── views/             # Các màn hình chính (QWidget/QStackedWidget)
│   │   │   ├── xe_view.py         # Quản lý xe
│   │   │   ├── khach_hang_view.py # Quản lý khách hàng
│   │   │   ├── hop_dong_view.py   # Quản lý hợp đồng
│   │   │   ├── nhan_vien_view.py  # Quản lý nhân viên
│   │   │   ├── kho_view.py        # Quản lý kho
│   │   │   ├── baocao_view.py     # Báo cáo thống kê
│   │   │   └── dashboard.py       # Màn hình chính
│   │   └── styles/            # StyleSheet (QSS files)
│   │       └── main_style.qss
│   │
│   ├── models/                # Database models (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── base.py            # Base model, engine
│   │   ├── xe.py              # Model Xe
│   │   ├── khach_hang.py      # Model KhachHang
│   │   ├── nhan_vien.py       # Model NhanVien
│   │   ├── hop_dong.py        # Model HopDong
│   │   ├── kho.py             # Model Kho, TonKho
│   │   └── audit_log.py       # Model AuditLog
│   │
│   ├── services/              # Business logic
│   │   ├── __init__.py
│   │   ├── xe_service.py
│   │   ├── khach_hang_service.py
│   │   ├── hop_dong_service.py
│   │   ├── kho_service.py
│   │   └── auth_service.py    # Xác thực đăng nhập
│   │
│   ├── database/              # Database connection
│   │   ├── __init__.py
│   │   ├── connection.py      # SQLAlchemy engine/session
│   │   ├── init_db.py         # Khởi tạo database & tables
│   │   └── migrations/        # Alembic migrations
│   │
│   └── utils/                 # Tiện ích
│       ├── __init__.py
│       ├── validators.py      # Validate dữ liệu input
│       ├── formatters.py      # Format số tiền, ngày tháng
│       ├── pdf_generator.py   # Tạo PDF (ReportLab)
│       └── constants.py       # Hằng số (vai trò, trạng thái)
│
├── data/                      # Dữ liệu ứng dụng
│   ├── quanlyxedaily.db       # File SQLite database
│   ├── backups/               # Backup database định kỳ
│   └── exports/               # File PDF xuất ra
│
├── docs/                      # Tài liệu
│   ├── YEU_CAU_CHUC_NANG.md
│   ├── SPEC.md
│   ├── TECH_STACK.md          # File này
│   ├── PHAN_TICH_THIET_KE_HE_THONG.md
│   └── giaodien/              # Screenshot thiết kế UI
│
├── tests/                     # Unit tests
│   ├── __init__.py
│   ├── conftest.py            # pytest fixtures
│   ├── test_models/
│   ├── test_services/
│   └── test_gui/              # GUI tests (pytest-qt)
│
└── resources/                 # Icons, images, fonts
    ├── icons/
    ├── images/
    └── fonts/
```

## 4. CÀI ĐẶT MÔI TRƯỜNG

### 4.1 Yêu cầu hệ thống
- **OS**: Windows 10/11, macOS 10.14+, Ubuntu 20.04+
- **Python**: 3.10 trở lên
- **RAM**: Tối thiểu 4GB (8GB khuyến nghị)
- **Disk**: 500MB trống
- **Màn hình**: 1366x768 trở lên

### 4.2 Cài đặt dependencies

```bash
# 1. Tạo virtual environment (khuyến nghị)
python -m venv venv

# 2. Kích hoạt environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Nâng cấp pip
python -m pip install --upgrade pip

# 4. Cài đặt packages
pip install -r requirements.txt
```

### 4.3 File requirements.txt

```
# Core - PyQt6 GUI Framework
PyQt6>=6.4.0
PyQt6-Qt6>=6.4.0

# Database
SQLAlchemy>=2.0.0

# PDF Generation
reportlab>=3.6.0

# Security
bcrypt>=4.0.0

# Utilities
python-dateutil>=2.8.0

# Development & Testing
pytest>=7.0.0
pytest-cov>=4.0.0
pytest-qt>=4.0.0      # Testing PyQt6
black>=23.0.0         # Code formatter
pylint>=2.15.0        # Linter
```

### 4.4 Cấu hình PyQt6 cơ bản

```python
# src/app.py
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
import sys

def create_app():
    app = QApplication(sys.argv)
    app.setApplicationName("Quản Lý Đại Lý Xe Hơi")
    app.setApplicationVersion("1.0.0")
    
    # Cấu hình font mặc định tiếng Việt
    font = app.font()
    font.setPointSize(10)
    app.setFont(font)
    
    return app

if __name__ == "__main__":
    app = create_app()
    # ... start main window
    sys.exit(app.exec())
```

## 5. WORKFLOW PHÁT TRIỂN

### 5.1 Quy trình làm việc
1. **Khởi tạo database**: `python -m src.database.init_db`
2. **Chạy ứng dụng**: `python main.py`
3. **Test**: `pytest tests/`
4. **Format code**: `black src/`

### 5.2 Pattern thiết kế
- **MVC (Model-View-Controller)**: Tách Model (data), View (GUI), Controller (logic)
- **Repository Pattern**: Tách database access ra khỏi business logic
- **Service Layer**: Xử lý nghiệp vụ phức tạp
- **Observer Pattern**: Signals/Slots của PyQt6

### 5.3 Ví dụ triển khai PyQt6

```python
# src/gui/views/xe_view.py
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem,
    QPushButton, QLabel, QLineEdit,
    QMessageBox
)
from PyQt6.QtCore import Qt

class XeView(QWidget):
    def __init__(self, service, parent=None):
        super().__init__(parent)
        self.service = service
        self.init_ui()
        self.load_data()
    
    def init_ui(self):
        # Layout chính
        layout = QVBoxLayout(self)
        
        # Tiêu đề
        title = QLabel("📋 Quản Lý Xe")
        title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            color: #2196F3;
            padding: 10px;
        """)
        layout.addWidget(title)
        
        # Search bar
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Tìm kiếm xe theo hãng, dòng xe...")
        self.btn_search = QPushButton("Tìm")
        self.btn_search.clicked.connect(self.search_xe)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.btn_search)
        layout.addLayout(search_layout)
        
        # Bảng dữ liệu
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Mã Xe", "Hãng", "Dòng Xe", "Năm SX", "Giá Bán", "Tồn Kho"
        ])
        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #f5f5f5;
                alternate-background-color: #e0e0e0;
                gridline-color: #bdbdbd;
            }
            QHeaderView::section {
                background-color: #2196F3;
                color: white;
                padding: 5px;
                font-weight: bold;
            }
        """)
        layout.addWidget(self.table)
        
        # Nút chức năng
        btn_layout = QHBoxLayout()
        self.btn_them = QPushButton("➕ Thêm Xe")
        self.btn_sua = QPushButton("✏️ Sửa")
        self.btn_xoa = QPushButton("🗑️ Xóa")
        self.btn_refresh = QPushButton("🔄 Làm mới")
        
        self.btn_them.clicked.connect(self.add_xe)
        self.btn_sua.clicked.connect(self.edit_xe)
        self.btn_xoa.clicked.connect(self.delete_xe)
        self.btn_refresh.clicked.connect(self.load_data)
        
        btn_layout.addWidget(self.btn_them)
        btn_layout.addWidget(self.btn_sua)
        btn_layout.addWidget(self.btn_xoa)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_refresh)
        layout.addLayout(btn_layout)
    
    def load_data(self):
        """Load danh sách xe từ database"""
        xe_list = self.service.get_all_xe()
        self.table.setRowCount(len(xe_list))
        for row, xe in enumerate(xe_list):
            self.table.setItem(row, 0, QTableWidgetItem(xe.ma_xe))
            self.table.setItem(row, 1, QTableWidgetItem(xe.hang))
            self.table.setItem(row, 2, QTableWidgetItem(xe.dong_xe))
            self.table.setItem(row, 3, QTableWidgetItem(str(xe.nam_sx)))
            self.table.setItem(row, 4, QTableWidgetItem(f"{xe.gia_ban:,.0f} VNĐ"))
            self.table.setItem(row, 5, QTableWidgetItem(str(xe.ton_kho)))
    
    def add_xe(self):
        """Mở dialog thêm xe"""
        from ..dialogs.xe_dialog import XeDialog
        dialog = XeDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_data()
            QMessageBox.information(self, "Thành công", "Đã thêm xe mới!")
    
    def delete_xe(self):
        """Xóa xe được chọn"""
        selected = self.table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn xe cần xóa!")
            return
        
        row = selected[0].row()
        ma_xe = self.table.item(row, 0).text()
        
        reply = QMessageBox.question(
            self, "Xác nhận",
            f"Bạn có chắc muốn xóa xe {ma_xe}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.service.delete_xe(ma_xe)
                self.load_data()
                QMessageBox.information(self, "Thành công", "Đã xóa xe!")
            except Exception as e:
                QMessageBox.critical(self, "Lỗi", str(e))
```

## 6. KẾ HOẠCH TRIỂN KHAI

| Giai đoạn | Thời gian | Nội dung | Tech Stack sử dụng |
|-----------|-----------|----------|-------------------|
| 1 | Tuần 1 | Setup project, Database schema, SQLAlchemy Models | SQLite, SQLAlchemy |
| 2 | Tuần 2 | PyQt6 MainWindow, Menu, Dashboard, Xe CRUD | PyQt6, Models |
| 3 | Tuần 3 | Khách hàng, Nhân viên, Phân quyền | PyQt6, bcrypt |
| 4 | Tuần 4 | Hợp đồng, Kho, Thanh toán | PyQt6, SQLAlchemy |
| 5 | Tuần 5 | Báo cáo (QChart), PDF, Testing | ReportLab, pytest |

## 7. LƯU Ý QUAN TRỌNG

### 7.1 PyQt6 với tiếng Việt
- Sử dụng font hỗ trợ Unicode (Arial, Segoe UI, hoặc Noto Sans)
- Encode file `.py` ở UTF-8
- Dùng f-string hoặc `.format()` cho chuỗi tiếng Việt

### 7.2 SQLite tối ưu
- Sử dụng WAL mode (Write-Ahead Logging) cho concurrent access
- Đánh index cho các cột thường tìm kiếm (mã xe, SĐT)
- Backup định kỳ bằng cách copy file `.db`

### 7.3 Bảo mật
- Không lưu password plaintext → dùng bcrypt
- Validate input để chống SQL Injection (dùng SQLAlchemy ORM)
- Log các thao tác quan trọng

---

**Cập nhật:** 16/04/2026  
**Phiên bản:** 1.0  
**Tech Stack cho:** Phần mềm Quản Lý Đại Lý Xe Hơi - Nhóm 4