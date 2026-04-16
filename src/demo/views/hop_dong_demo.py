"""
HopDong Demo View - Màn hình Quản lý Hợp Đồng
Notion-inspired design, chỉ UI không logic
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QFrame, QTableWidget, QTableWidgetItem,
    QPushButton, QHeaderView, QLineEdit, QComboBox,
    QDialog, QFormLayout, QTextEdit, QScrollArea,
    QSizePolicy, QMessageBox, QDateEdit
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont


class HopDongDemo(QWidget):
    """Quản lý Hợp Đồng view với bảng, filter, chi tiết"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("hopdong-demo")
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
        
        # ===== STATS CARDS =====
        stats = self.create_stats_cards()
        main_layout.addWidget(stats)
        
        # ===== TOOLBAR =====
        toolbar = self.create_toolbar()
        main_layout.addWidget(toolbar)
        
        # ===== TABLE =====
        table = self.create_table()
        main_layout.addWidget(table, stretch=1)
    
    def create_header(self) -> QWidget:
        """Tạo header"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)
        
        title = QLabel("Quản lý Hợp Đồng")
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
            letter-spacing: -0.5px;
        """)
        layout.addWidget(title)
        
        subtitle = QLabel("Danh sách hợp đồng bán xe và quản lý thanh toán")
        subtitle.setStyleSheet("""
            font-size: 14px;
            font-weight: 400;
            color: #615d59;
        """)
        layout.addWidget(subtitle)
        
        return widget
    
    def create_stats_cards(self) -> QWidget:
        """Tạo cards thống kê hợp đồng"""
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)
        
        stats = [
            ("TỔNG HỢP ĐỒNG", "156", "card"),
            ("MỚI TẠO", "12", "card-blue"),
            ("ĐÃ THANH TOÁN", "89", "card-green"),
            ("CHỜ GIAO", "8", "card-orange"),
        ]
        
        for title, value, style in stats:
            card = self.create_stat_card(title, value, style)
            layout.addWidget(card)
        
        return widget
    
    def create_stat_card(self, title: str, value: str, style: str) -> QFrame:
        """Tạo stat card"""
        card = QFrame()
        card.setObjectName(style)
        
        if style == "card-blue":
            card.setStyleSheet("""
                QFrame {
                    background-color: #f2f9ff;
                    border: 1px solid rgba(0, 117, 222, 0.15);
                    border-radius: 12px;
                }
            """)
        elif style == "card-green":
            card.setStyleSheet("""
                QFrame {
                    background-color: #f0fdf4;
                    border: 1px solid rgba(26, 174, 57, 0.15);
                    border-radius: 12px;
                }
            """)
        elif style == "card-orange":
            card.setStyleSheet("""
                QFrame {
                    background-color: #fff7ed;
                    border: 1px solid rgba(221, 91, 0, 0.15);
                    border-radius: 12px;
                }
            """)
        else:
            card.setStyleSheet("""
                QFrame {
                    background-color: #ffffff;
                    border: 1px solid rgba(0, 0, 0, 0.1);
                    border-radius: 12px;
                }
            """)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(8)
        
        lbl_title = QLabel(title)
        lbl_title.setStyleSheet("""
            font-size: 12px;
            font-weight: 600;
            color: #615d59;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        """)
        layout.addWidget(lbl_title)
        
        lbl_value = QLabel(value)
        lbl_value.setStyleSheet("""
            font-size: 28px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
        """)
        layout.addWidget(lbl_value)
        
        return card
    
    def create_toolbar(self) -> QWidget:
        """Tạo toolbar"""
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        
        # Search
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Tìm theo mã HĐ, tên KH...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 14px;
                font-size: 14px;
                min-width: 260px;
            }
            QLineEdit:focus {
                border: 1px solid #0075de;
            }
        """)
        layout.addWidget(self.search_input)
        
        # Filter status
        self.filter_status = QComboBox()
        self.filter_status.addItems(["Tất cả trạng thái", "Mới", "Đã thanh toán", "Đã giao xe", "Đã hủy"])
        self.filter_status.setStyleSheet("""
            QComboBox {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 14px;
                font-size: 14px;
                min-width: 150px;
            }
            QComboBox:focus {
                border: 1px solid #0075de;
            }
        """)
        layout.addWidget(self.filter_status)
        
        # Date range
        self.date_from = QDateEdit()
        self.date_from.setCalendarPopup(True)
        self.date_from.setDate(QDate.currentDate().addMonths(-1))
        self.date_from.setStyleSheet("""
            QDateEdit {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
            }
        """)
        layout.addWidget(self.date_from)
        
        lbl_to = QLabel("đến")
        lbl_to.setStyleSheet("color: #615d59;")
        layout.addWidget(lbl_to)
        
        self.date_to = QDateEdit()
        self.date_to.setCalendarPopup(True)
        self.date_to.setDate(QDate.currentDate())
        self.date_to.setStyleSheet("""
            QDateEdit {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
            }
        """)
        layout.addWidget(self.date_to)
        
        layout.addStretch()
        
        # Add button
        btn_add = QPushButton("➕ Tạo hợp đồng mới")
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
        btn_add.clicked.connect(self.show_create_dialog)
        layout.addWidget(btn_add)
        
        return widget
    
    def create_table(self) -> QFrame:
        """Tạo bảng hợp đồng"""
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
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
            "Mã HĐ", "Khách hàng", "Xe", "Ngày tạo", "Giá trị", "Trạng thái", "Thao tác"
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
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        
        # Column widths
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Fixed)
        
        self.table.setColumnWidth(0, 80)
        self.table.setColumnWidth(3, 100)
        self.table.setColumnWidth(4, 110)
        self.table.setColumnWidth(5, 120)
        self.table.setColumnWidth(6, 150)
        
        layout.addWidget(self.table)
        
        return card
    
    def load_dummy_data(self):
        """Load dummy data"""
        dummy_hd = [
            {"ma": "HD0056", "khach": "Nguyễn Văn An", "xe": "Toyota Camry 2.5G 2023", "ngay": "15/04/2024", "gia": 1200000000, "status": "moi"},
            {"ma": "HD0055", "khach": "Công ty TNHH B", "xe": "Honda Civic RS 2024", "ngay": "14/04/2024", "gia": 850000000, "status": "da_tt"},
            {"ma": "HD0054", "khach": "Trần Thị C", "xe": "Hyundai Santa Fe 2023", "ngay": "12/04/2024", "gia": 1100000000, "status": "da_giao"},
            {"ma": "HD0053", "khach": "Lê Văn D", "xe": "Kia Seltos 2024", "ngay": "10/04/2024", "gia": 650000000, "status": "da_tt"},
            {"ma": "HD0052", "khach": "Tập đoàn E", "xe": "Mazda CX-5 2023", "ngay": "08/04/2024", "gia": 900000000, "status": "da_giao"},
            {"ma": "HD0051", "khach": "Phạm Thị F", "xe": "Toyota Corolla Altis 2024", "ngay": "05/04/2024", "gia": 750000000, "status": "da_tt"},
            {"ma": "HD0050", "khach": "Nguyễn Văn G", "xe": "Honda City 2024", "ngay": "03/04/2024", "gia": 580000000, "status": "da_giao"},
            {"ma": "HD0049", "khach": "Công ty H", "xe": "Mitsubishi Outlander 2023", "ngay": "01/04/2024", "gia": 950000000, "status": "da_huy"},
        ]
        
        self.table.setRowCount(len(dummy_hd))
        
        for row, hd in enumerate(dummy_hd):
            # Mã HĐ
            item_ma = QTableWidgetItem(hd["ma"])
            item_ma.setFont(QFont("Inter", 13, QFont.Weight.Medium))
            self.table.setItem(row, 0, item_ma)
            
            # Khách hàng
            item_khach = QTableWidgetItem(hd["khach"])
            item_khach.setFont(QFont("Inter", 13))
            self.table.setItem(row, 1, item_khach)
            
            # Xe
            item_xe = QTableWidgetItem(hd["xe"])
            item_xe.setFont(QFont("Inter", 13))
            self.table.setItem(row, 2, item_xe)
            
            # Ngày
            item_ngay = QTableWidgetItem(hd["ngay"])
            item_ngay.setFont(QFont("Inter", 13))
            item_ngay.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(row, 3, item_ngay)
            
            # Giá
            gia_formatted = f"{hd['gia']/1000000000:.1f} tỷ" if hd["gia"] >= 1000000000 else f"{hd['gia']/1000000:.0f}tr"
            item_gia = QTableWidgetItem(gia_formatted)
            item_gia.setFont(QFont("Inter", 13, QFont.Weight.Medium))
            item_gia.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.table.setItem(row, 4, item_gia)
            
            # Status pill
            status_widget = self.create_status_pill(hd["status"])
            self.table.setCellWidget(row, 5, status_widget)
            
            # Actions
            actions = self.create_action_buttons(row)
            self.table.setCellWidget(row, 6, actions)
            
            self.table.setRowHeight(row, 56)
    
    def create_status_pill(self, status: str) -> QLabel:
        """Tạo pill badge cho trạng thái"""
        styles = {
            "moi": ("Mới", "#0075de", "#f2f9ff"),
            "da_tt": ("Đã thanh toán", "#1aae39", "#f0fdf4"),
            "da_giao": ("Đã giao", "#615d59", "#f6f5f4"),
            "da_huy": ("Đã hủy", "#dc2626", "#fef2f2"),
        }
        
        text, color, bg = styles.get(status, ("Không rõ", "#615d59", "#f6f5f4"))
        
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
        
        # Xem
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
        
        # In
        btn_print = QPushButton("🖨️")
        btn_print.setToolTip("In hợp đồng")
        btn_print.setFixedSize(32, 32)
        btn_print.setStyleSheet("""
            QPushButton {
                background-color: rgba(139, 92, 246, 0.1);
                color: #8b5cf6;
                border: none;
                border-radius: 6px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: rgba(139, 92, 246, 0.2);
            }
        """)
        btn_print.clicked.connect(lambda: self.print_contract(row))
        layout.addWidget(btn_print)
        
        # Hủy (if not cancelled)
        btn_cancel = QPushButton("✕")
        btn_cancel.setToolTip("Hủy hợp đồng")
        btn_cancel.setFixedSize(32, 32)
        btn_cancel.setStyleSheet("""
            QPushButton {
                background-color: rgba(220, 38, 38, 0.1);
                color: #dc2626;
                border: none;
                border-radius: 6px;
                font-size: 12px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: rgba(220, 38, 38, 0.2);
            }
        """)
        btn_cancel.clicked.connect(lambda: self.confirm_cancel(row))
        layout.addWidget(btn_cancel)
        
        return widget
    
    def show_create_dialog(self):
        """Hiển thị dialog tạo HĐ"""
        dialog = HopDongCreateDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            QMessageBox.information(self, "Thành công", "Đã tạo hợp đồng mới!")
    
    def show_detail_dialog(self, row: int):
        """Hiển thị dialog xem chi tiết"""
        ma_hd = self.table.item(row, 0).text()
        dialog = HopDongDetailDialog(self, ma_hd)
        dialog.exec()
    
    def print_contract(self, row: int):
        """In hợp đồng"""
        ma_hd = self.table.item(row, 0).text()
        QMessageBox.information(self, "In hợp đồng", f"Đang in hợp đồng {ma_hd}...")
    
    def confirm_cancel(self, row: int):
        """Xác nhận hủy"""
        ma_hd = self.table.item(row, 0).text()
        
        reply = QMessageBox.question(
            self, "Xác nhận hủy",
            f"Bạn có chắc muốn hủy hợp đồng {ma_hd}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self, "Thành công", f"Đã hủy hợp đồng {ma_hd}!")


class HopDongCreateDialog(QDialog):
    """Dialog tạo hợp đồng mới"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tạo hợp đồng mới")
        self.setMinimumSize(600, 700)
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 28, 28, 28)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("📝 Tạo hợp đồng mới")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
        """)
        layout.addWidget(title)
        
        # Form
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none;")
        
        form_widget = QWidget()
        form_layout = QFormLayout(form_widget)
        form_layout.setSpacing(16)
        
        # Mã HĐ (auto)
        txt_ma = QLineEdit("HD0057")
        txt_ma.setEnabled(False)
        txt_ma.setStyleSheet(self.input_style_disabled())
        form_layout.addRow("Mã hợp đồng:", txt_ma)
        
        # Ngày tạo
        date_create = QDateEdit()
        date_create.setDate(QDate.currentDate())
        date_create.setCalendarPopup(True)
        date_create.setStyleSheet(self.date_style())
        form_layout.addRow("Ngày tạo *:", date_create)
        
        # Khách hàng
        combo_kh = QComboBox()
        combo_kh.addItems(["Chọn khách hàng...", "Nguyễn Văn An", "Công ty TNHH B", "Trần Thị C"])
        combo_kh.setStyleSheet(self.combo_style())
        form_layout.addRow("Khách hàng *:", combo_kh)
        
        # Xe
        combo_xe = QComboBox()
        combo_xe.addItems(["Chọn xe...", "Toyota Camry 2.5G - 1.2 tỷ", "Honda Civic RS - 850tr", "Hyundai Santa Fe - 1.1 tỷ"])
        combo_xe.setStyleSheet(self.combo_style())
        form_layout.addRow("Xe *:", combo_xe)
        
        # Giá bán
        txt_gia = QLineEdit("1,200,000,000")
        txt_gia.setStyleSheet(self.input_style())
        form_layout.addRow("Giá bán (VNĐ) *:", txt_gia)
        
        # Phụ kiện
        txt_pk = QTextEdit()
        txt_pk.setPlaceholderText("Nhập danh sách phụ kiện (nếu có)")
        txt_pk.setMaximumHeight(80)
        txt_pk.setStyleSheet(self.textarea_style())
        form_layout.addRow("Phụ kiện:", txt_pk)
        
        # Khuyến mãi
        txt_km = QLineEdit("0")
        txt_km.setStyleSheet(self.input_style())
        form_layout.addRow("Khuyến mãi (VNĐ):", txt_km)
        
        # Tổng thanh toán
        txt_total = QLineEdit("1,200,000,000")
        txt_total.setEnabled(False)
        txt_total.setStyleSheet(self.input_style_disabled())
        form_layout.addRow("Tổng thanh toán:", txt_total)
        
        # Tiền cọc
        txt_coc = QLineEdit("200,000,000")
        txt_coc.setStyleSheet(self.input_style())
        form_layout.addRow("Tiền cọc (VNĐ) *:", txt_coc)
        
        # Ghi chú
        txt_ghichu = QTextEdit()
        txt_ghichu.setPlaceholderText("Ghi chú thêm về hợp đồng")
        txt_ghichu.setMaximumHeight(80)
        txt_ghichu.setStyleSheet(self.textarea_style())
        form_layout.addRow("Ghi chú:", txt_ghichu)
        
        scroll.setWidget(form_widget)
        layout.addWidget(scroll)
        
        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        
        btn_cancel = QPushButton("Hủy")
        btn_cancel.setStyleSheet(self.btn_secondary_style())
        btn_cancel.clicked.connect(self.reject)
        btn_layout.addWidget(btn_cancel)
        
        btn_layout.addStretch()
        
        btn_preview = QPushButton("👁️ Xem trước")
        btn_preview.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0.05);
                color: rgba(0, 0, 0, 0.95);
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.08);
            }
        """)
        btn_layout.addWidget(btn_preview)
        
        btn_save = QPushButton("💾 Tạo hợp đồng")
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
            }
            QLineEdit:focus {
                border: 1px solid #0075de;
            }
        """
    
    def input_style_disabled(self) -> str:
        return """
            QLineEdit {
                background-color: #f6f5f4;
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
                color: #615d59;
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
            }
            QComboBox:focus {
                border: 1px solid #0075de;
            }
        """
    
    def date_style(self) -> str:
        return """
            QDateEdit {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
            }
        """
    
    def textarea_style(self) -> str:
        return """
            QTextEdit {
                background-color: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
            }
            QTextEdit:focus {
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


class HopDongDetailDialog(QDialog):
    """Dialog xem chi tiết hợp đồng"""
    
    def __init__(self, parent=None, ma_hd: str = ""):
        super().__init__(parent)
        self.setWindowTitle(f"Chi tiết hợp đồng {ma_hd}")
        self.setMinimumSize(550, 600)
        self.ma_hd = ma_hd
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 28, 28, 28)
        layout.setSpacing(20)
        
        # Header
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        # Title
        title = QLabel(f"📝 {self.ma_hd}")
        title.setStyleSheet("""
            font-size: 22px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
        """)
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        # Status
        status = QLabel("Đã thanh toán")
        status.setStyleSheet("""
            background-color: #f0fdf4;
            color: #1aae39;
            border-radius: 9999px;
            padding: 6px 14px;
            font-size: 12px;
            font-weight: 600;
        """)
        header_layout.addWidget(status)
        
        layout.addWidget(header)
        
        # Content
        content = QFrame()
        content.setStyleSheet("""
            QFrame {
                background-color: #f6f5f4;
                border-radius: 12px;
            }
        """)
        
        content_layout = QFormLayout(content)
        content_layout.setSpacing(16)
        content_layout.setContentsMargins(24, 24, 24, 24)
        
        # Info items
        info_items = [
            ("Khách hàng:", "Nguyễn Văn An"),
            ("Số điện thoại:", "0901234567"),
            ("Xe:", "Toyota Camry 2.5G 2023"),
            ("Ngày tạo:", "15/04/2024"),
            ("Giá bán:", "1,200,000,000 VNĐ"),
            ("Phụ kiện:", "Dán phim cách nhiệt, lót sàn"),
            ("Khuyến mãi:", "-50,000,000 VNĐ"),
            ("Tổng thanh toán:", "1,150,000,000 VNĐ"),
            ("Tiền cọc:", "200,000,000 VNĐ"),
            ("Còn nợ:", "950,000,000 VNĐ"),
            ("Ngày giao xe dự kiến:", "20/04/2024"),
        ]
        
        for label, value in info_items:
            lbl_label = QLabel(label)
            lbl_label.setStyleSheet("font-weight: 600; color: #615d59;")
            
            lbl_value = QLabel(value)
            lbl_value.setStyleSheet("color: rgba(0, 0, 0, 0.95);")
            
            content_layout.addRow(lbl_label, lbl_value)
        
        layout.addWidget(content)
        layout.addStretch()
        
        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        
        btn_close = QPushButton("Đóng")
        btn_close.setStyleSheet(self.btn_secondary_style())
        btn_close.clicked.connect(self.reject)
        btn_layout.addWidget(btn_close)
        
        btn_layout.addStretch()
        
        btn_print = QPushButton("🖨️ In hợp đồng")
        btn_print.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0.05);
                color: rgba(0, 0, 0, 0.95);
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.08);
            }
        """)
        btn_layout.addWidget(btn_print)
        
        btn_pay = QPushButton("💳 Thanh toán")
        btn_pay.setStyleSheet(self.btn_primary_style())
        btn_layout.addWidget(btn_pay)
        
        layout.addLayout(btn_layout)
    
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