"""
KhachHang Demo View - Màn hình Quản lý Khách Hàng
Notion-inspired design, chỉ UI không logic
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QFrame, QTableWidget, QTableWidgetItem,
    QPushButton, QHeaderView, QLineEdit, QComboBox,
    QDialog, QFormLayout, QTabWidget, QStackedWidget,
    QSizePolicy, QMessageBox, QScrollArea, QTextEdit
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont


class KhachHangDemo(QWidget):
    """Quản lý Khách Hàng view với tabs, bảng danh sách, chi tiết"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("khachhang-demo")
        self.init_ui()
        self.load_dummy_data()
    
    def init_ui(self):
        """Khởi tạo giao diện"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(32, 24, 32, 24)
        main_layout.setSpacing(24)
        
        # ===== HEADER =====
        header = self.create_header()
        main_layout.addWidget(header)
        
        # ===== TABS + TOOLBAR =====
        tabs_toolbar = self.create_tabs_toolbar()
        main_layout.addWidget(tabs_toolbar)
        
        # ===== CONTENT AREA =====
        self.content_stack = QStackedWidget()
        
        # List view
        self.list_view = self.create_list_view()
        self.content_stack.addWidget(self.list_view)
        
        # Detail view (sẽ được tạo khi click)
        self.detail_placeholder = QWidget()
        self.content_stack.addWidget(self.detail_placeholder)
        
        main_layout.addWidget(self.content_stack, stretch=1)
    
    def create_header(self) -> QWidget:
        """Tạo header"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)
        
        title = QLabel("Quản lý Khách Hàng")
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
            letter-spacing: -0.5px;
        """)
        layout.addWidget(title)
        
        subtitle = QLabel("Danh sách khách hàng và lịch sử giao dịch")
        subtitle.setStyleSheet("""
            font-size: 14px;
            font-weight: 400;
            color: #615d59;
        """)
        layout.addWidget(subtitle)
        
        return widget
    
    def create_tabs_toolbar(self) -> QWidget:
        """Tạo tabs và toolbar"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)
        
        # Tabs
        tabs_layout = QHBoxLayout()
        tabs_layout.setSpacing(8)
        
        self.tab_buttons = {}
        tabs = [
            ("tat_ca", "Tất cả", "128"),
            ("ca_nhan", "Cá nhân", "89"),
            ("doanh_nghiep", "Doanh nghiệp", "39"),
        ]
        
        for tab_id, label, count in tabs:
            btn = QPushButton(f"{label} ({count})")
            btn.setCheckable(True)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(self.get_tab_style(tab_id == "tat_ca"))
            btn.clicked.connect(lambda checked, tid=tab_id: self.switch_tab(tid))
            self.tab_buttons[tab_id] = btn
            tabs_layout.addWidget(btn)
        
        tabs_layout.addStretch()
        layout.addLayout(tabs_layout)
        
        # Toolbar
        toolbar = QWidget()
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.setSpacing(12)
        
        # Search
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Tìm theo tên, SĐT, email...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 14px;
                font-size: 14px;
                min-width: 280px;
            }
            QLineEdit:focus {
                border: 1px solid #0075de;
            }
        """)
        toolbar_layout.addWidget(self.search_input)
        
        toolbar_layout.addStretch()
        
        # Add button
        btn_add = QPushButton("➕ Thêm khách hàng")
        btn_add.setStyleSheet("""
            QPushButton {
                background-color: #0075de;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #005bab;
            }
        """)
        btn_add.clicked.connect(self.show_add_dialog)
        toolbar_layout.addWidget(btn_add)
        
        layout.addWidget(toolbar)
        
        return widget
    
    def get_tab_style(self, is_active: bool) -> str:
        """Get style cho tab button"""
        if is_active:
            return """
                QPushButton {
                    background-color: rgba(0, 0, 0, 0.08);
                    color: rgba(0, 0, 0, 0.95);
                    border: none;
                    border-radius: 8px;
                    padding: 10px 20px;
                    font-size: 14px;
                    font-weight: 600;
                }
            """
        else:
            return """
                QPushButton {
                    background-color: transparent;
                    color: rgba(0, 0, 0, 0.7);
                    border: none;
                    border-radius: 8px;
                    padding: 10px 20px;
                    font-size: 14px;
                    font-weight: 500;
                }
                QPushButton:hover {
                    background-color: rgba(0, 0, 0, 0.05);
                }
            """
    
    def switch_tab(self, tab_id: str):
        """Chuyển tab"""
        for tid, btn in self.tab_buttons.items():
            btn.setStyleSheet(self.get_tab_style(tid == tab_id))
        # Filter table data based on tab
        self.load_dummy_data()
    
    def create_list_view(self) -> QFrame:
        """Tạo bảng danh sách KH"""
        card = QFrame()
        card.setObjectName("card")
        card.setStyleSheet("""
            QFrame#card {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 12px;
            }
        """)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "Mã KH", "Họ tên", "Số điện thoại", "Email", "Loại", "Hợp đồng", "Thao tác"
        ])
        
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                border: none;
                gridline-color: transparent;
                font-size: 13px;
            }
            QTableWidget::item {
                padding: 14px 16px;
                border-bottom: 1px solid rgba(0, 0, 0, 0.05);
            }
            QTableWidget::item:selected {
                background-color: #f2f9ff;
                color: rgba(0, 0, 0, 0.95);
            }
            QHeaderView::section {
                background-color: #f6f5f4;
                color: rgba(0, 0, 0, 0.95);
                padding: 12px 16px;
                font-weight: 600;
                font-size: 13px;
                border: none;
                border-bottom: 1px solid rgba(0, 0, 0, 0.1);
            }
            QHeaderView::section:first {
                border-top-left-radius: 12px;
            }
            QHeaderView::section:last {
                border-top-right-radius: 12px;
            }
        """)
        
        self.table.setShowGrid(False)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        
        # Column widths
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Fixed)
        
        self.table.setColumnWidth(0, 80)
        self.table.setColumnWidth(2, 120)
        self.table.setColumnWidth(4, 110)
        self.table.setColumnWidth(5, 90)
        self.table.setColumnWidth(6, 140)
        
        # Double click to view detail
        self.table.doubleClicked.connect(self.show_detail_dialog)
        
        layout.addWidget(self.table)
        
        return card
    
    def load_dummy_data(self):
        """Load dummy data"""
        dummy_kh = [
            {"ma": "KH001", "ten": "Nguyễn Văn An", "sdt": "0901234567", "email": "an.nguyen@email.com", "loai": "ca_nhan", "hop_dong": 3},
            {"ma": "KH002", "ten": "Công ty TNHH B", "sdt": "0912345678", "email": "contact@congtyb.com", "loai": "doanh_nghiep", "hop_dong": 5},
            {"ma": "KH003", "ten": "Trần Thị C", "sdt": "0923456789", "email": "c.tran@gmail.com", "loai": "ca_nhan", "hop_dong": 1},
            {"ma": "KH004", "ten": "Lê Văn D", "sdt": "0934567890", "email": "d.le@yahoo.com", "loai": "ca_nhan", "hop_dong": 2},
            {"ma": "KH005", "ten": "Tập đoàn E", "sdt": "0945678901", "email": "info@tapdoan-e.com.vn", "loai": "doanh_nghiep", "hop_dong": 8},
            {"ma": "KH006", "ten": "Phạm Thị F", "sdt": "0956789012", "email": "f.pham@outlook.com", "loai": "ca_nhan", "hop_dong": 0},
            {"ma": "KH007", "ten": "Nguyễn Văn G", "sdt": "0967890123", "email": "g.nguyen@company.com", "loai": "ca_nhan", "hop_dong": 4},
        ]
        
        self.table.setRowCount(len(dummy_kh))
        
        for row, kh in enumerate(dummy_kh):
            # Mã KH
            item_ma = QTableWidgetItem(kh["ma"])
            item_ma.setFont(QFont("Inter", 13, QFont.Weight.Medium))
            self.table.setItem(row, 0, item_ma)
            
            # Tên
            item_ten = QTableWidgetItem(kh["ten"])
            item_ten.setFont(QFont("Inter", 13))
            self.table.setItem(row, 1, item_ten)
            
            # SĐT
            item_sdt = QTableWidgetItem(kh["sdt"])
            item_sdt.setFont(QFont("Inter", 13))
            item_sdt.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(row, 2, item_sdt)
            
            # Email
            item_email = QTableWidgetItem(kh["email"])
            item_email.setFont(QFont("Inter", 13))
            self.table.setItem(row, 3, item_email)
            
            # Loại (pill)
            loai_widget = self.create_loai_pill(kh["loai"])
            self.table.setCellWidget(row, 4, loai_widget)
            
            # Số HĐ
            item_hd = QTableWidgetItem(str(kh["hop_dong"]))
            item_hd.setFont(QFont("Inter", 13, QFont.Weight.Medium))
            item_hd.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(row, 5, item_hd)
            
            # Thao tác
            action_widget = self.create_action_buttons(row)
            self.table.setCellWidget(row, 6, action_widget)
            
            self.table.setRowHeight(row, 56)
    
    def create_loai_pill(self, loai: str) -> QLabel:
        """Tạo pill cho loại KH"""
        if loai == "ca_nhan":
            text, color, bg = "Cá nhân", "#0075de", "#f2f9ff"
        else:
            text, color, bg = "Doanh nghiệp", "#7c3aed", "#faf5ff"
        
        pill = QLabel(text)
        pill.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pill.setStyleSheet(f"""
            background-color: {bg};
            color: {color};
            border-radius: 9999px;
            padding: 4px 10px;
            font-size: 11px;
            font-weight: 600;
        """)
        return pill
    
    def create_action_buttons(self, row: int) -> QWidget:
        """Tạo nút thao tác"""
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(6)
        
        # Xem chi tiết
        btn_view = QPushButton("👁️")
        btn_view.setToolTip("Xem chi tiết")
        btn_view.setFixedSize(32, 32)
        btn_view.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 117, 222, 0.1);
                color: #0075de;
                border: none;
                border-radius: 6px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: rgba(0, 117, 222, 0.2);
            }
        """)
        btn_view.clicked.connect(lambda: self.show_detail_dialog(row))
        layout.addWidget(btn_view)
        
        # Sửa
        btn_edit = QPushButton("✏️")
        btn_edit.setToolTip("Sửa")
        btn_edit.setFixedSize(32, 32)
        btn_edit.setStyleSheet("""
            QPushButton {
                background-color: rgba(245, 158, 11, 0.1);
                color: #f59e0b;
                border: none;
                border-radius: 6px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: rgba(245, 158, 11, 0.2);
            }
        """)
        btn_edit.clicked.connect(lambda: self.show_edit_dialog(row))
        layout.addWidget(btn_edit)
        
        # Xóa
        btn_delete = QPushButton("🗑️")
        btn_delete.setToolTip("Xóa")
        btn_delete.setFixedSize(32, 32)
        btn_delete.setStyleSheet("""
            QPushButton {
                background-color: rgba(220, 38, 38, 0.1);
                color: #dc2626;
                border: none;
                border-radius: 6px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: rgba(220, 38, 38, 0.2);
            }
        """)
        btn_delete.clicked.connect(lambda: self.confirm_delete(row))
        layout.addWidget(btn_delete)
        
        return widget
    
    def show_add_dialog(self):
        """Hiển thị dialog thêm KH"""
        dialog = KhachHangDialog(self, "Thêm khách hàng mới")
        if dialog.exec() == QDialog.DialogCode.Accepted:
            QMessageBox.information(self, "Thành công", "Đã thêm khách hàng!")
    
    def show_detail_dialog(self, row: int):
        """Hiển thị dialog xem chi tiết"""
        ma_kh = self.table.item(row, 0).text()
        ten_kh = self.table.item(row, 1).text()
        dialog = KhachHangDetailDialog(self, ma_kh, ten_kh)
        dialog.exec()
    
    def show_edit_dialog(self, row: int):
        """Hiển thị dialog sửa"""
        ma_kh = self.table.item(row, 0).text()
        dialog = KhachHangDialog(self, f"Sửa khách hàng {ma_kh}", edit_mode=True)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            QMessageBox.information(self, "Thành công", "Đã cập nhật!")
    
    def confirm_delete(self, row: int):
        """Xác nhận xóa"""
        ma_kh = self.table.item(row, 0).text()
        ten_kh = self.table.item(row, 1).text()
        
        reply = QMessageBox.question(
            self, "Xác nhận xóa",
            f"Bạn có chắc muốn xóa khách hàng {ma_kh} - {ten_kh}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self, "Thành công", f"Đã xóa {ten_kh}!")


class KhachHangDialog(QDialog):
    """Dialog thêm/sửa khách hàng"""
    
    def __init__(self, parent=None, title: str = "Thêm KH", edit_mode: bool = False):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(500)
        self.edit_mode = edit_mode
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 28, 28, 28)
        layout.setSpacing(20)
        
        # Title
        title = QLabel(self.windowTitle())
        title.setStyleSheet("""
            font-size: 22px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
        """)
        layout.addWidget(title)
        
        # Form
        form = QWidget()
        form_layout = QFormLayout(form)
        form_layout.setSpacing(16)
        
        # Mã KH
        self.txt_ma = QLineEdit()
        self.txt_ma.setPlaceholderText("Nhập mã KH (vd: KH001)")
        self.txt_ma.setStyleSheet(self.input_style())
        if self.edit_mode:
            self.txt_ma.setText("KH001")
            self.txt_ma.setEnabled(False)
        form_layout.addRow("Mã khách hàng *:", self.txt_ma)
        
        # Họ tên
        self.txt_ten = QLineEdit()
        self.txt_ten.setPlaceholderText("Nhập họ tên")
        self.txt_ten.setStyleSheet(self.input_style())
        form_layout.addRow("Họ tên *:", self.txt_ten)
        
        # Loại
        self.combo_loai = QComboBox()
        self.combo_loai.addItems(["Cá nhân", "Doanh nghiệp"])
        self.combo_loai.setStyleSheet(self.combo_style())
        form_layout.addRow("Loại khách hàng *:", self.combo_loai)
        
        # SĐT
        self.txt_sdt = QLineEdit()
        self.txt_sdt.setPlaceholderText("Nhập số điện thoại")
        self.txt_sdt.setStyleSheet(self.input_style())
        form_layout.addRow("Số điện thoại *:", self.txt_sdt)
        
        # Email
        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText("Nhập email")
        self.txt_email.setStyleSheet(self.input_style())
        form_layout.addRow("Email:", self.txt_email)
        
        # Địa chỉ
        self.txt_diachi = QLineEdit()
        self.txt_diachi.setPlaceholderText("Nhập địa chỉ")
        self.txt_diachi.setStyleSheet(self.input_style())
        form_layout.addRow("Địa chỉ:", self.txt_diachi)
        
        layout.addWidget(form)
        layout.addStretch()
        
        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        
        btn_cancel = QPushButton("Hủy")
        btn_cancel.setStyleSheet(self.btn_secondary_style())
        btn_cancel.clicked.connect(self.reject)
        btn_layout.addWidget(btn_cancel)
        
        btn_layout.addStretch()
        
        btn_save = QPushButton("💾 Lưu" if self.edit_mode else "➕ Thêm mới")
        btn_save.setStyleSheet(self.btn_primary_style())
        btn_save.clicked.connect(self.accept)
        btn_layout.addWidget(btn_save)
        
        layout.addLayout(btn_layout)
    
    def input_style(self) -> str:
        return """
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
                min-width: 300px;
            }
            QLineEdit:focus {
                border: 1px solid #0075de;
            }
        """
    
    def combo_style(self) -> str:
        return """
            QComboBox {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
                min-width: 300px;
            }
            QComboBox:focus {
                border: 1px solid #0075de;
            }
        """
    
    def btn_primary_style(self) -> str:
        return """
            QPushButton {
                background-color: #0075de;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 24px;
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #005bab;
            }
        """
    
    def btn_secondary_style(self) -> str:
        return """
            QPushButton {
                background-color: transparent;
                color: #615d59;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 24px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.05);
            }
        """


class KhachHangDetailDialog(QDialog):
    """Dialog xem chi tiết KH với tabs"""
    
    def __init__(self, parent=None, ma_kh: str = "", ten_kh: str = ""):
        super().__init__(parent)
        self.setWindowTitle(f"Chi tiết khách hàng - {ten_kh}")
        self.setMinimumSize(700, 500)
        self.ma_kh = ma_kh
        self.ten_kh = ten_kh
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 28, 28, 28)
        layout.setSpacing(20)
        
        # Header
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        # Avatar
        avatar = QLabel("👤")
        avatar.setStyleSheet("""
            font-size: 48px;
            background-color: rgba(0, 117, 222, 0.1);
            border-radius: 32px;
            padding: 8px;
        """)
        header_layout.addWidget(avatar)
        
        # Info
        info = QWidget()
        info_layout = QVBoxLayout(info)
        info_layout.setContentsMargins(12, 0, 0, 0)
        info_layout.setSpacing(4)
        
        name = QLabel(self.ten_kh)
        name.setStyleSheet("""
            font-size: 22px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
        """)
        info_layout.addWidget(name)
        
        ma = QLabel(f"Mã: {self.ma_kh}")
        ma.setStyleSheet("""
            font-size: 14px;
            color: #615d59;
        """)
        info_layout.addWidget(ma)
        
        header_layout.addWidget(info)
        header_layout.addStretch()
        
        # Edit button
        btn_edit = QPushButton("✏️ Sửa")
        btn_edit.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0.05);
                color: rgba(0, 0, 0, 0.95);
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.08);
            }
        """)
        header_layout.addWidget(btn_edit)
        
        layout.addWidget(header)
        
        # Separator
        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setStyleSheet("background-color: rgba(0, 0, 0, 0.1); max-height: 1px;")
        sep.setFixedHeight(1)
        layout.addWidget(sep)
        
        # Tabs
        tabs = QTabWidget()
        tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                background-color: #ffffff;
            }
            QTabBar::tab {
                background-color: transparent;
                color: #615d59;
                padding: 12px 20px;
                font-size: 14px;
                font-weight: 500;
                border: none;
            }
            QTabBar::tab:selected {
                color: #0075de;
                font-weight: 600;
            }
        """)
        
        # Tab 1: Thông tin
        tab_info = self.create_info_tab()
        tabs.addTab(tab_info, "📋 Thông tin")
        
        # Tab 2: Lịch sử giao dịch
        tab_history = self.create_history_tab()
        tabs.addTab(tab_history, "📜 Lịch sử (3)")
        
        layout.addWidget(tabs)
    
    def create_info_tab(self) -> QWidget:
        """Tab thông tin chi tiết"""
        widget = QWidget()
        layout = QFormLayout(widget)
        layout.setSpacing(16)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Info items
        info_items = [
            ("Loại khách hàng:", "Cá nhân"),
            ("Số điện thoại:", "0901234567"),
            ("Email:", "an.nguyen@email.com"),
            ("Địa chỉ:", "123 Nguyễn Văn A, Q.1, TP.HCM"),
            ("Ngày đăng ký:", "15/01/2024"),
            ("Tổng hợp đồng:", "3"),
            ("Tổng giá trị:", "3.2 tỷ VNĐ"),
        ]
        
        for label, value in info_items:
            lbl_label = QLabel(label)
            lbl_label.setStyleSheet("font-weight: 600; color: #615d59;")
            
            lbl_value = QLabel(value)
            lbl_value.setStyleSheet("color: rgba(0, 0, 0, 0.95);")
            
            layout.addRow(lbl_label, lbl_value)
        
        return widget
    
    def create_history_tab(self) -> QWidget:
        """Tab lịch sử giao dịch"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)
        
        # History items
        history_items = [
            {"hd": "HD0042", "xe": "Toyota Camry 2.5G", "ngay": "15/04/2024", "gia": "1.2 tỷ", "status": "Hoàn thành"},
            {"hd": "HD0038", "xe": "Honda Civic RS", "ngay": "10/02/2024", "gia": "850tr", "status": "Hoàn thành"},
            {"hd": "HD0025", "xe": "Mazda CX-5", "ngay": "05/12/2023", "gia": "950tr", "status": "Hoàn thành"},
        ]
        
        for item in history_items:
            card = QFrame()
            card.setStyleSheet("""
                QFrame {
                    background-color: #f6f5f4;
                    border-radius: 8px;
                    padding: 4px;
                }
            """)
            
            card_layout = QHBoxLayout(card)
            card_layout.setContentsMargins(16, 12, 16, 12)
            
            # Info
            info = QWidget()
            info_layout = QVBoxLayout(info)
            info_layout.setSpacing(4)
            
            hd_label = QLabel(f"Hợp đồng {item['hd']} - {item['xe']}")
            hd_label.setStyleSheet("font-weight: 600; color: rgba(0, 0, 0, 0.95);")
            info_layout.addWidget(hd_label)
            
            date_label = QLabel(f"Ngày: {item['ngay']} | Giá: {item['gia']}")
            date_label.setStyleSheet("font-size: 13px; color: #615d59;")
            info_layout.addWidget(date_label)
            
            card_layout.addWidget(info)
            card_layout.addStretch()
            
            # Status
            status = QLabel(item['status'])
            status.setStyleSheet("""
                background-color: #f0fdf4;
                color: #1aae39;
                border-radius: 9999px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: 600;
            """)
            card_layout.addWidget(status)
            
            layout.addWidget(card)
        
        layout.addStretch()
        return widget