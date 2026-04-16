# Task Demo - Hướng Dẫn Tạo Giao Diện Demo (Mockup UI)

## Mục tiêu
Tạo giao diện demo (UI mockup) cho **Phần mềm Quản lý Đại Lý Xe Hơi** sử dụng **PyQt6**, **không cần logic nghiệp vụ**, chỉ tập trung vào giao diện và layout.

## Tech Stack Sử Dụng
- **Python 3.10+**
- **PyQt6 6.4+** - GUI Framework
- **Design System**: Notion-inspired (từ DESIGN.md)

---

## 1. Cấu Trúc Giao Diện Demo

```
src/
├── demo/
│   ├── __init__.py
│   ├── main_demo.py          # Entry point chạy demo
│   ├── main_window_demo.py   # MainWindow với sidebar + content area
│   ├── styles/               # QSS stylesheets
│   │   └── notion_theme.qss
│   └── views/                # Các màn hình demo
│       ├── dashboard_demo.py
│       ├── xe_demo.py
│       ├── khach_hang_demo.py
│       ├── hop_dong_demo.py
│       └── nhan_vien_demo.py
```

---

## 2. Các Màn Hình Demo Cần Tạo

### 2.1 Dashboard Demo (Màn hình chính)
**Chức năng hiển thị:**
- Tổng quan thống kê: Số xe trong kho, số khách hàng, hợp đồng tháng này
- Biểu đồ doanh thu (dùng QChart placeholder)
- Danh sách hợp đồng gần đây (dummy data)
- Cảnh báo tồn kho thấp

**Layout:**
```
+------------------+------------------------------------------+
|  LOGO            |  Dashboard                               |
|  - Dashboard     |                                          |
|  - Quản lý xe    |  [Cards: Xe|Khách|Hợp đồng|Doanh thu]   |
|  - Khách hàng    |                                          |
|  - Hợp đồng      |  +------------------+  +-------------+  |
|  - Nhân viên     |  | Biểu đồ doanh    |  | Hợp đồng    |  |
|  - Báo cáo       |  | thu (placeholder)|  | gần đây     |  |
|                  |  +------------------+  +-------------+  |
+------------------+------------------------------------------+
```

### 2.2 Quản lý Xe Demo
**Chức năng hiển thị:**
- Bảng danh sách xe với các cột: Mã xe, Hãng, Dòng xe, Năm SX, Giá, Tồn kho, Trạng thái
- Thanh tìm kiếm + bộ lọc (ComboBox: Tất cả/Còn hàng/Đã bán)
- Nút: Thêm, Sửa, Xóa, Làm mới
- Form dialog thêm/sửa xe (QDialog)

**Layout:**
```
+-------------------------------------------------------------+
|  Quản lý Xe                                                 |
|  [Search________________] [Lọc: Tất cả ▼] [🔍] [+ Thêm]    |
|                                                             |
|  +-----------------------------------------------------+   |
|  | Mã xe | Hãng   | Dòng xe    | Năm | Giá      | Tồn |   |
|  +-------+--------+------------+-----+----------+-----+   |
|  | XE001 | Toyota | Camry      |2023 | 1.2 tỷ   |  5  |   |
|  | XE002 | Honda  | Civic      |2024 | 850tr    |  3  |   |
|  | ...   | ...    | ...        | ... | ...      | ... |   |
|  +-------+--------+------------+-----+----------+-----+   |
|                                                             |
|  [< Trang 1/5 >]                               [Sửa] [Xóa] |
+-------------------------------------------------------------+
```

### 2.3 Quản lý Khách Hàng Demo
**Chức năng hiển thị:**
- Bảng danh sách: Mã KH, Họ tên, SĐT, Email, Loại, Số hợp đồng
- Tìm kiếm theo tên/SĐT
- Tab/Lọc: Tất cả / Cá nhân / Doanh nghiệp
- Dialog xem chi tiết + lịch sử giao dịch (dummy tabs)

**Layout:**
```
+-------------------------------------------------------------+
|  Quản lý Khách Hàng                                         |
|  [Tab: Tất cả | Cá nhân | Doanh nghiệp]                     |
|  [Search________________] [🔍] [+ Thêm KH]                 |
|                                                             |
|  +-----------------------------------------------------+   |
|  | Mã KH | Họ tên         | SĐT        | Email        |   |
|  +-------+----------------+------------+--------------+   |
|  | KH001 | Nguyễn Văn A   | 0901234567 | a@email.com  |   |
|  | KH002 | Công ty B      | 0912345678 | b@email.com  |   |
|  +-------+----------------+------------+--------------+   |
|                                                             |
|  [Chi tiết] [Lịch sử]                                      |
+-------------------------------------------------------------+
```

### 2.4 Quản lý Hợp Đồng Demo
**Chức năng hiển thị:**
- Bảng hợp đồng: Mã HĐ, Khách hàng, Xe, Ngày, Giá trị, Trạng thái
- Trạng thái dùng **Pill Badge** (Mới/Đã thanh toán/Đã giao - Notion style)
- Filter theo trạng thái
- Dialog tạo hợp đồng với form đầy đủ fields

**Layout:**
```
+-------------------------------------------------------------+
|  Quản lý Hợp Đồng                                           |
|  [Filter: Tất cả ▼] [Search_____] [+ Tạo HĐ]               |
|                                                             |
|  +-----------------------------------------------------+   |
|  | Mã HĐ | Khách hàng | Xe        | Giá      | Trạng  |   |
|  +-------+------------+-----------+----------+--------+   |
|  |HD0001 | Nguyễn A   | Camry 2023| 1.2 tỷ   |[Mới 🔵]|   |
|  |HD0002 | Công ty B  | Civic 2024| 850tr    |[Đã TT 🟢]|  |
|  +-------+------------+-----------+----------+--------+   |
|                                                             |
|  Nút: [Xem] [Sửa] [In PDF]                                 |
+-------------------------------------------------------------+
```

### 2.5 Quản lý Nhân Viên Demo
**Chức năng hiển thị:**
- Bảng: Mã NV, Họ tên, Chức vụ, SĐT, Email, Trạng thái
- Thêm/Sửa/Xóa nhân viên
- Phân quyền (Admin/Nhân viên) dùng Toggle/Combo

---

## 3. Design System Áp Dụng (Từ DESIGN.md)

### 3.1 Màu Sắc
```python
# Màu chính - Notion Style
NOTION_BLACK = "rgba(0, 0, 0, 0.95)"      # Text chính
NOTION_BLUE = "#0075de"                    # CTA, buttons, links
PURE_WHITE = "#ffffff"                     # Background
WARM_WHITE = "#f6f5f4"                     # Section alt bg
WARM_GRAY_500 = "#615d59"                  # Secondary text
WARM_GRAY_300 = "#a39e98"                  # Placeholder, muted
BORDER_COLOR = "rgba(0, 0, 0, 0.1)"        # Whisper borders

# Semantic Colors
GREEN_BADGE = "#1aae39"                    # Success/Đã thanh toán
ORANGE_BADGE = "#dd5b00"                   # Warning/Chờ
BLUE_BADGE_BG = "#f2f9ff"                  # Pill badge bg
BLUE_BADGE_TEXT = "#097fe8"                # Pill badge text
```

### 3.2 Typography (PyQt6)
```python
# Font chính
font_family = "Inter, -apple-system, Segoe UI, Helvetica, Arial"

# Hierarchy
DISPLAY_HERO = {"size": 32, "weight": 700, "spacing": -1}
SECTION_HEADING = {"size": 24, "weight": 700, "spacing": -0.5}
CARD_TITLE = {"size": 18, "weight": 600}
BODY = {"size": 14, "weight": 400}
CAPTION = {"size": 12, "weight": 500}
BADGE = {"size": 11, "weight": 600}
```

### 3.3 Components Style

#### Button Primary (Notion Blue)
```css
QPushButton#primary {
    background-color: #0075de;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    font-weight: 600;
}
QPushButton#primary:hover {
    background-color: #005bab;
}
```

#### Button Secondary
```css
QPushButton#secondary {
    background-color: rgba(0, 0, 0, 0.05);
    color: rgba(0, 0, 0, 0.95);
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
}
```

#### Card
```css
QFrame#card {
    background-color: white;
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 12px;
}
```

#### Pill Badge
```css
QLabel#pill-badge {
    background-color: #f2f9ff;
    color: #097fe8;
    border-radius: 9999px;
    padding: 4px 10px;
    font-size: 11px;
    font-weight: 600;
}
```

#### Table
```css
QTableWidget {
    background-color: white;
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    gridline-color: rgba(0, 0, 0, 0.05);
}
QHeaderView::section {
    background-color: #f6f5f4;
    color: rgba(0, 0, 0, 0.95);
    padding: 10px;
    font-weight: 600;
    border: none;
}
```

---

## 4. Dummy Data Mẫu

### 4.1 Danh sách Xe (10 records)
```python
DUMMY_XE = [
    {"ma": "XE001", "hang": "Toyota", "dong": "Camry 2.5G", "nam": 2023, "gia": 1200000000, "ton": 5, "trang_thai": "Còn hàng"},
    {"ma": "XE002", "hang": "Honda", "dong": "Civic RS", "nam": 2024, "gia": 850000000, "ton": 3, "trang_thai": "Còn hàng"},
    {"ma": "XE003", "hang": "Hyundai", "dong": "Santa Fe", "nam": 2023, "gia": 1100000000, "ton": 0, "trang_thai": "Hết hàng"},
    {"ma": "XE004", "hang": "Kia", "dong": "Seltos", "nam": 2024, "gia": 650000000, "ton": 8, "trang_thai": "Còn hàng"},
    {"ma": "XE005", "hang": "Mazda", "dong": "CX-5", "nam": 2023, "gia": 900000000, "ton": 2, "trang_thai": "Sắp hết"},
]
```

### 4.2 Danh sách Khách Hàng
```python
DUMMY_KHACH_HANG = [
    {"ma": "KH001", "ten": "Nguyễn Văn An", "sdt": "0901234567", "email": "an.nguyen@email.com", "loai": "Cá nhân", "hop_dong": 2},
    {"ma": "KH002", "ten": "Công ty TNHH B", "sdt": "0912345678", "email": "contact@congtyb.com", "loai": "Doanh nghiệp", "hop_dong": 5},
]
```

### 4.3 Danh sách Hợp Đồng
```python
DUMMY_HOP_DONG = [
    {"ma": "HD0001", "khach": "Nguyễn Văn An", "xe": "Toyota Camry", "ngay": "15/04/2024", "gia": 1200000000, "trang_thai": "Mới"},
    {"ma": "HD0002", "khach": "Công ty TNHH B", "xe": "Honda Civic", "ngay": "10/04/2024", "gia": 850000000, "trang_thai": "Đã thanh toán"},
]
```

---

## 5. Checklist Tạo Demo

### Phase 1: Setup (30 phút)
- [ ] Tạo thư mục `src/demo/`
- [ ] Tạo file `notion_theme.qss` với các style cơ bản
- [ ] Tạo `main_demo.py` entry point

### Phase 2: Main Window (1 giờ)
- [ ] MainWindow với sidebar navigation (Dashboard, Xe, KH, HĐ, NV)
- [ ] Content area dùng QStackedWidget
- [ ] Sidebar style: warm white bg, hover effect

### Phase 3: Dashboard View (45 phút)
- [ ] 4 summary cards (Xe, KH, HĐ, Doanh thu)
- [ ] Placeholder cho biểu đồ
- [ ] Table hợp đồng gần đây (dummy data)

### Phase 4: Xe View (1 giờ)
- [ ] Search bar + Filter combo
- [ ] QTableWidget với 6 cột
- [ ] Populate với DUMMY_XE
- [ ] Nút Thêm/Sửa/Xóa (chưa cần logic)
- [ ] Dialog form thêm xe (UI only)

### Phase 5: Khách Hàng & Hợp Đồng (1.5 giờ)
- [ ] KH View: Table + Tabs (Tất cả/CN/Doanh nghiệp)
- [ ] HĐ View: Table + Pill badges trạng thái
- [ ] Dialog tạo HĐ (form đầy đủ)

### Phase 6: Polish (30 phút)
- [ ] Apply QSS stylesheet toàn app
- [ ] Kiểm tra spacing, alignment
- [ ] Thêm icons (nếu có)

**Tổng thời gian ước tính: ~5 giờ**

---

## 6. Code Template Khởi Đầu

### main_demo.py
```python
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from main_window_demo import MainWindowDemo

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Quản Lý Đại Lý Xe Hơi - Demo")
    
    # Load stylesheet
    with open("styles/notion_theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    
    window = MainWindowDemo()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```

### main_window_demo.py (Template)
```python
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QStackedWidget, QFrame
)
from PyQt6.QtCore import Qt

class MainWindowDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản Lý Đại Lý Xe Hơi")
        self.setGeometry(100, 100, 1400, 900)
        self.init_ui()
    
    def init_ui(self):
        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        
        # Main layout: Sidebar + Content
        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Sidebar
        self.sidebar = self.create_sidebar()
        layout.addWidget(self.sidebar, 1)
        
        # Content area
        self.content = QStackedWidget()
        layout.addWidget(self.content, 5)
        
        # Add views
        self.setup_views()
    
    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setStyleSheet("""
            QFrame#sidebar {
                background-color: #f6f5f4;
                border-right: 1px solid rgba(0, 0, 0, 0.1);
            }
        """)
        
        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(16, 24, 16, 24)
        layout.setSpacing(8)
        
        # Logo
        logo = QLabel("🚗 Đại Lý Xe")
        logo.setStyleSheet("font-size: 20px; font-weight: 700; margin-bottom: 24px;")
        layout.addWidget(logo)
        
        # Nav buttons
        nav_items = [
            ("Dashboard", "dashboard"),
            ("Quản lý Xe", "xe"),
            ("Khách Hàng", "khachhang"),
            ("Hợp Đồng", "hopdong"),
            ("Nhân Viên", "nhanvien"),
        ]
        
        for label, view_id in nav_items:
            btn = QPushButton(label)
            btn.setObjectName("nav-btn")
            btn.setStyleSheet("""
                QPushButton#nav-btn {
                    text-align: left;
                    padding: 12px 16px;
                    border: none;
                    border-radius: 6px;
                    font-weight: 500;
                    background: transparent;
                }
                QPushButton#nav-btn:hover {
                    background-color: rgba(0, 0, 0, 0.05);
                }
            """)
            btn.clicked.connect(lambda checked, v=view_id: self.switch_view(v))
            layout.addWidget(btn)
        
        layout.addStretch()
        return sidebar
    
    def setup_views(self):
        # Import and add views
        from views.dashboard_demo import DashboardDemo
        from views.xe_demo import XeDemo
        from views.khach_hang_demo import KhachHangDemo
        from views.hop_dong_demo import HopDongDemo
        
        self.views = {
            "dashboard": DashboardDemo(),
            "xe": XeDemo(),
            "khachhang": KhachHangDemo(),
            "hopdong": HopDongDemo(),
        }
        
        for view in self.views.values():
            self.content.addWidget(view)
    
    def switch_view(self, view_id):
        view = self.views.get(view_id)
        if view:
            self.content.setCurrentWidget(view)
```

---

## 7. Lưu Ý Quan Trọng

### Không cần logic:
- ❌ Không cần kết nối database
- ❌ Không cần validate dữ liệu thực
- ❌ Không cần xử lý CRUD thực
- ❌ Không cần tính toán, báo cáo thực

### Chỉ cần UI:
- ✅ Layout đúng, đẹp
- ✅ Đủ các widgets cần thiết
- ✅ Dummy data hiển thị
- ✅ Style đúng design system
- ✅ Navigation hoạt động (switch view)

### Demo nên có:
- Tooltip/hover effects
- Dialog mẫu (chưa cần submit)
- Placeholder cho charts
- Responsive cơ bản (min size)

---

**Mục tiêu cuối cùng**: Có thể chạy `python main_demo.py` và xem được toàn bộ giao diện các màn hình chính, di chuyển qua lại giữa các view, thấy được layout và design.