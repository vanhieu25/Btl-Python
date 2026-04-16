"""
Xe Demo View - Màn hình Quản lý Xe
Notion-inspired design, chỉ UI không logic
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QFrame, QTableWidget, QTableWidgetItem,
    QPushButton, QHeaderView, QLineEdit, QComboBox,
    QDialog, QFormLayout, QSpinBox, QDoubleSpinBox,
    QSizePolicy, QMessageBox
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont


class XeDemo(QWidget):
    """Quản lý Xe view với bảng danh sách, tìm kiếm, filter"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("xe-demo")
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
        
        # ===== TOOLBAR (Search + Filter + Add) =====
        toolbar = self.create_toolbar()
        main_layout.addWidget(toolbar)
        
        # ===== TABLE =====
        table = self.create_table()
        main_layout.addWidget(table, stretch=1)
        
        # ===== PAGINATION =====
        pagination = self.create_pagination()
        main_layout.addWidget(pagination)
    
    def create_header(self) -> QWidget:
        """Tạo header với title"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)
        
        # Title
        title = QLabel("Quản lý Xe")
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
            letter-spacing: -0.5px;
        """)
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Danh sách xe trong kho và thông tin chi tiết")
        subtitle.setStyleSheet("""
            font-size: 14px;
            font-weight: 400;
            color: #615d59;
        """)
        layout.addWidget(subtitle)
        
        return widget
    
    def create_toolbar(self) -> QWidget:
        """Tạo toolbar với search, filter, add button"""
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        
        # Search box
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Tìm kiếm xe theo mã, hãng, dòng xe...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 14px;
                font-size: 14px;
                min-width: 320px;
            }
            QLineEdit:focus {
                border: 1px solid #0075de;
            }
        """)
        layout.addWidget(self.search_input)
        
        # Filter combo
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Tất cả", "Còn hàng", "Sắp hết", "Hết hàng"])
        self.filter_combo.setStyleSheet("""
            QComboBox {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 14px;
                font-size: 14px;
                min-width: 140px;
            }
            QComboBox:focus {
                border: 1px solid #0075de;
            }
            QComboBox::drop-down {
                border: none;
                width: 24px;
            }
        """)
        layout.addWidget(self.filter_combo)
        
        # Refresh button
        btn_refresh = QPushButton("🔄 Làm mới")
        btn_refresh.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0.05);
                color: rgba(0, 0, 0, 0.95);
                border: none;
                border-radius: 6px;
                padding: 10px 16px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.08);
            }
        """)
        btn_refresh.clicked.connect(self.load_dummy_data)
        layout.addWidget(btn_refresh)
        
        layout.addStretch()
        
        # Add button
        btn_add = QPushButton("➕ Thêm xe mới")
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
        layout.addWidget(btn_add)
        
        return widget
    
    def create_table(self) -> QFrame:
        """Tạo bảng danh sách xe"""
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
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "Mã xe", "Hãng", "Dòng xe", "Năm SX", "Giá bán", "Tồn kho", "Trạng thái", "Thao tác"
        ])
        
        # Table styling
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                border: none;
                gridline-color: transparent;
                font-size: 13px;
            }
            QTableWidget::item {
                padding: 12px 16px;
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
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeMode.Fixed)
        
        self.table.setColumnWidth(0, 80)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(3, 80)
        self.table.setColumnWidth(4, 110)
        self.table.setColumnWidth(5, 80)
        self.table.setColumnWidth(6, 100)
        self.table.setColumnWidth(7, 120)
        
        layout.addWidget(self.table)
        
        return card
    
    def create_pagination(self) -> QWidget:
        """Tạo pagination bar"""
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        
        # Info label
        lbl_info = QLabel("Hiển thị 1-10 / 45 xe")
        lbl_info.setStyleSheet("""
            font-size: 13px;
            color: #615d59;
        """)
        layout.addWidget(lbl_info)
        
        layout.addStretch()
        
        # Pagination buttons
        btn_prev = QPushButton("← Trước")
        btn_prev.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #615d59;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.05);
            }
        """)
        layout.addWidget(btn_prev)
        
        # Page numbers
        for i in range(1, 6):
            btn_page = QPushButton(str(i))
            if i == 1:
                btn_page.setStyleSheet("""
                    QPushButton {
                        background-color: #0075de;
                        color: white;
                        border: none;
                        border-radius: 6px;
                        padding: 8px 14px;
                        font-size: 13px;
                        font-weight: 600;
                    }
                """)
            else:
                btn_page.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        color: #615d59;
                        border: none;
                        border-radius: 6px;
                        padding: 8px 14px;
                        font-size: 13px;
                        font-weight: 500;
                    }
                    QPushButton:hover {
                        background-color: rgba(0, 0, 0, 0.05);
                    }
                """)
            layout.addWidget(btn_page)
        
        btn_next = QPushButton("Sau →")
        btn_next.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #615d59;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.05);
            }
        """)
        layout.addWidget(btn_next)
        
        return widget
    
    def load_dummy_data(self):
        """Load dummy data cho bảng"""
        dummy_xe = [
            {"ma": "XE001", "hang": "Toyota", "dong": "Camry 2.5G", "nam": 2023, "gia": 1200000000, "ton": 5, "status": "con_hang"},
            {"ma": "XE002", "hang": "Honda", "dong": "Civic RS", "nam": 2024, "gia": 850000000, "ton": 3, "status": "con_hang"},
            {"ma": "XE003", "hang": "Hyundai", "dong": "Santa Fe", "nam": 2023, "gia": 1100000000, "ton": 0, "status": "het_hang"},
            {"ma": "XE004", "hang": "Kia", "dong": "Seltos", "nam": 2024, "gia": 650000000, "ton": 8, "status": "con_hang"},
            {"ma": "XE005", "hang": "Mazda", "dong": "CX-5", "nam": 2023, "gia": 900000000, "ton": 2, "status": "sap_het"},
            {"ma": "XE006", "hang": "Toyota", "dong": "Corolla Altis", "nam": 2024, "gia": 750000000, "ton": 12, "status": "con_hang"},
            {"ma": "XE007", "hang": "Honda", "dong": "City", "nam": 2024, "gia": 580000000, "ton": 7, "status": "con_hang"},
            {"ma": "XE008", "hang": "Mitsubishi", "dong": "Outlander", "nam": 2023, "gia": 950000000, "ton": 1, "status": "sap_het"},
            {"ma": "XE009", "hang": "Kia", "dong": "Cerato", "nam": 2024, "gia": 620000000, "ton": 0, "status": "het_hang"},
            {"ma": "XE010", "hang": "Hyundai", "dong": "Tucson", "nam": 2024, "gia": 1050000000, "ton": 4, "status": "con_hang"},
        ]
        
        self.table.setRowCount(len(dummy_xe))
        
        for row, xe in enumerate(dummy_xe):
            # Mã xe
            item_ma = QTableWidgetItem(xe["ma"])
            item_ma.setFont(QFont("Inter", 13, QFont.Weight.Medium))
            self.table.setItem(row, 0, item_ma)
            
            # Hãng
            item_hang = QTableWidgetItem(xe["hang"])
            item_hang.setFont(QFont("Inter", 13))
            self.table.setItem(row, 1, item_hang)
            
            # Dòng xe
            item_dong = QTableWidgetItem(xe["dong"])
            item_dong.setFont(QFont("Inter", 13))
            self.table.setItem(row, 2, item_dong)
            
            # Năm SX
            item_nam = QTableWidgetItem(str(xe["nam"]))
            item_nam.setFont(QFont("Inter", 13))
            item_nam.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(row, 3, item_nam)
            
            # Giá bán
            gia_formatted = f"{xe['gia']/1000000000:.1f} tỷ" if xe["gia"] >= 1000000000 else f"{xe['gia']/1000000:.0f}tr"
            item_gia = QTableWidgetItem(gia_formatted)
            item_gia.setFont(QFont("Inter", 13, QFont.Weight.Medium))
            item_gia.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.table.setItem(row, 4, item_gia)
            
            # Tồn kho
            item_ton = QTableWidgetItem(str(xe["ton"]))
            item_ton.setFont(QFont("Inter", 13))
            item_ton.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            # Color based on stock
            if xe["ton"] == 0:
                item_ton.setForeground(Qt.GlobalColor.red)
            elif xe["ton"] <= 2:
                item_ton.setForeground(Qt.GlobalColor.darkYellow)
            self.table.setItem(row, 5, item_ton)
            
            # Trạng thái (pill badge)
            status_widget = self.create_status_pill(xe["status"])
            self.table.setCellWidget(row, 6, status_widget)
            
            # Thao tác buttons
            action_widget = self.create_action_buttons(row)
            self.table.setCellWidget(row, 7, action_widget)
            
            # Row height
            self.table.setRowHeight(row, 52)
    
    def create_status_pill(self, status: str) -> QLabel:
        """Tạo pill badge cho trạng thái"""
        status_map = {
            "con_hang": ("Còn hàng", "#1aae39", "#f0fdf4"),
            "sap_het": ("Sắp hết", "#dd5b00", "#fff7ed"),
            "het_hang": ("Hết hàng", "#dc2626", "#fef2f2"),
        }
        
        text, color, bg = status_map.get(status, ("Không rõ", "#615d59", "#f6f5f4"))
        
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
        """Tạo nút thao tác cho mỗi dòng"""
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(6)
        
        # Sửa button
        btn_edit = QPushButton("✏️")
        btn_edit.setToolTip("Sửa")
        btn_edit.setFixedSize(32, 32)
        btn_edit.setStyleSheet("""
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
        btn_edit.clicked.connect(lambda: self.show_edit_dialog(row))
        layout.addWidget(btn_edit)
        
        # Xóa button
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
        """Hiển thị dialog thêm xe mới"""
        dialog = XeDialog(self, "Thêm xe mới")
        if dialog.exec() == QDialog.DialogCode.Accepted:
            QMessageBox.information(self, "Thành công", "Đã thêm xe mới!")
    
    def show_edit_dialog(self, row: int):
        """Hiển thị dialog sửa xe"""
        ma_xe = self.table.item(row, 0).text()
        dialog = XeDialog(self, f"Sửa xe {ma_xe}", edit_mode=True)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            QMessageBox.information(self, "Thành công", "Đã cập nhật thông tin xe!")
    
    def confirm_delete(self, row: int):
        """Xác nhận xóa xe"""
        ma_xe = self.table.item(row, 0).text()
        ten_xe = self.table.item(row, 2).text()
        
        reply = QMessageBox.question(
            self, "Xác nhận xóa",
            f"Bạn có chắc muốn xóa xe {ma_xe} - {ten_xe}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self, "Thành công", f"Đã xóa xe {ma_xe}!")


class XeDialog(QDialog):
    """Dialog thêm/sửa xe"""
    
    def __init__(self, parent=None, title: str = "Thêm xe", edit_mode: bool = False):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(480)
        self.edit_mode = edit_mode
        self.init_ui()
    
    def init_ui(self):
        """Khởi tạo dialog"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(20)
        
        # Title
        title = QLabel(self.windowTitle())
        title.setStyleSheet("""
            font-size: 20px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
            margin-bottom: 8px;
        """)
        layout.addWidget(title)
        
        # Form
        form = QWidget()
        form_layout = QFormLayout(form)
        form_layout.setSpacing(16)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        
        # Mã xe
        self.txt_ma = QLineEdit()
        self.txt_ma.setPlaceholderText("Nhập mã xe (vd: XE001)")
        self.txt_ma.setStyleSheet(self.input_style())
        if self.edit_mode:
            self.txt_ma.setText("XE001")
            self.txt_ma.setEnabled(False)
        form_layout.addRow("Mã xe *:", self.txt_ma)
        
        # Hãng xe
        self.combo_hang = QComboBox()
        self.combo_hang.addItems(["Toyota", "Honda", "Hyundai", "Kia", "Mazda", "Mitsubishi", "Ford", "Chevrolet"])
        self.combo_hang.setStyleSheet(self.combo_style())
        form_layout.addRow("Hãng xe *:", self.combo_hang)
        
        # Dòng xe
        self.txt_dong = QLineEdit()
        self.txt_dong.setPlaceholderText("Nhập dòng xe (vd: Camry 2.5G)")
        self.txt_dong.setStyleSheet(self.input_style())
        form_layout.addRow("Dòng xe *:", self.txt_dong)
        
        # Năm sản xuất
        self.spin_nam = QSpinBox()
        self.spin_nam.setRange(2015, 2030)
        self.spin_nam.setValue(2024)
        self.spin_nam.setStyleSheet(self.spin_style())
        form_layout.addRow("Năm SX *:", self.spin_nam)
        
        # Giá bán
        self.spin_gia = QDoubleSpinBox()
        self.spin_gia.setRange(100, 10000)
        self.spin_gia.setValue(1000)
        self.spin_gia.setSuffix(" triệu")
        self.spin_gia.setStyleSheet(self.spin_style())
        form_layout.addRow("Giá bán *:", self.spin_gia)
        
        # Tồn kho
        self.spin_ton = QSpinBox()
        self.spin_ton.setRange(0, 100)
        self.spin_ton.setValue(5)
        self.spin_ton.setStyleSheet(self.spin_style())
        form_layout.addRow("Tồn kho:", self.spin_ton)
        
        layout.addWidget(form)
        layout.addStretch()
        
        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        
        btn_cancel = QPushButton("Hủy")
        btn_cancel.setStyleSheet("""
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
        """)
        btn_cancel.clicked.connect(self.reject)
        btn_layout.addWidget(btn_cancel)
        
        btn_layout.addStretch()
        
        btn_save = QPushButton("💾 Lưu" if self.edit_mode else "➕ Thêm mới")
        btn_save.setStyleSheet("""
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
        """)
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
                min-width: 280px;
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
                min-width: 280px;
            }
            QComboBox:focus {
                border: 1px solid #0075de;
            }
        """
    
    def spin_style(self) -> str:
        return """
            QSpinBox, QDoubleSpinBox {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
                min-width: 280px;
            }
            QSpinBox:focus, QDoubleSpinBox:focus {
                border: 1px solid #0075de;
            }
        """