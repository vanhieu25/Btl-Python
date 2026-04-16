"""
Dashboard Demo View - Màn hình chính Dashboard
Notion-inspired design, chỉ UI không logic
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QFrame, QTableWidget, QTableWidgetItem,
    QPushButton, QHeaderView, QSizePolicy
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont


class DashboardDemo(QWidget):
    """Dashboard view với summary cards, chart placeholder và recent contracts table"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("dashboard-demo")
        self.init_ui()
        self.load_dummy_data()
    
    def init_ui(self):
        """Khởi tạo giao diện Dashboard"""
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(32, 24, 32, 24)
        main_layout.setSpacing(24)
        
        # ===== HEADER SECTION =====
        header_widget = self.create_header()
        main_layout.addWidget(header_widget)
        
        # ===== SUMMARY CARDS SECTION =====
        cards_widget = self.create_summary_cards()
        main_layout.addWidget(cards_widget)
        
        # ===== CONTENT ROW: Chart + Recent Contracts =====
        content_row = QHBoxLayout()
        content_row.setSpacing(24)
        
        # Chart placeholder (left side - 60%)
        chart_widget = self.create_chart_section()
        content_row.addWidget(chart_widget, 6)
        
        # Recent contracts table (right side - 40%)
        contracts_widget = self.create_recent_contracts_section()
        content_row.addWidget(contracts_widget, 4)
        
        main_layout.addLayout(content_row, stretch=1)
    
    def create_header(self) -> QWidget:
        """Tạo header với title và subtitle"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)
        
        # Title
        title = QLabel("Dashboard")
        title.setObjectName("page-title")
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
            letter-spacing: -0.5px;
        """)
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Tổng quan hoạt động đại lý xe hơi")
        subtitle.setObjectName("page-subtitle")
        subtitle.setStyleSheet("""
            font-size: 14px;
            font-weight: 400;
            color: #615d59;
        """)
        layout.addWidget(subtitle)
        
        return widget
    
    def create_summary_cards(self) -> QWidget:
        """Tạo 4 summary cards: Xe, Khách hàng, Hợp đồng, Doanh thu"""
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)
        
        # Card data
        cards_data = [
            {
                "title": "TỔNG XE TRONG KHO",
                "value": "45",
                "subtitle": "+3 xe mới nhập tháng này",
                "subtitle_style": "up",
                "card_style": "card-blue"
            },
            {
                "title": "KHÁCH HÀNG",
                "value": "128",
                "subtitle": "+12 khách hàng mới",
                "subtitle_style": "up",
                "card_style": "card-green"
            },
            {
                "title": "HỢP ĐỒNG THÁNG",
                "value": "23",
                "subtitle": "5 hợp đồng chờ xử lý",
                "subtitle_style": "warning",
                "card_style": "card-orange"
            },
            {
                "title": "DOANH THU THÁNG",
                "value": "12.5 tỷ",
                "subtitle": "+15% so với tháng trước",
                "subtitle_style": "up",
                "card_style": "card-purple"
            }
        ]
        
        for card_info in cards_data:
            card = self.create_card(
                title=card_info["title"],
                value=card_info["value"],
                subtitle=card_info["subtitle"],
                subtitle_style=card_info["subtitle_style"],
                card_style=card_info["card_style"]
            )
            layout.addWidget(card)
        
        return widget
    
    def create_card(self, title: str, value: str, subtitle: str, 
                    subtitle_style: str = "normal", card_style: str = "card") -> QFrame:
        """Tạo một summary card"""
        card = QFrame()
        card.setObjectName(card_style)
        card.setMinimumHeight(120)
        card.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(8)
        
        # Title
        lbl_title = QLabel(title)
        lbl_title.setObjectName("card-title")
        lbl_title.setStyleSheet("""
            font-size: 12px;
            font-weight: 600;
            color: #615d59;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        """)
        layout.addWidget(lbl_title)
        
        # Value
        lbl_value = QLabel(value)
        lbl_value.setObjectName("card-value")
        lbl_value.setStyleSheet("""
            font-size: 32px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
            letter-spacing: -0.5px;
        """)
        layout.addWidget(lbl_value)
        
        # Subtitle with style
        lbl_subtitle = QLabel(subtitle)
        lbl_subtitle.setObjectName("card-subtitle")
        
        if subtitle_style == "up":
            lbl_subtitle.setStyleSheet("""
                font-size: 13px;
                font-weight: 500;
                color: #1aae39;
            """)
        elif subtitle_style == "down":
            lbl_subtitle.setStyleSheet("""
                font-size: 13px;
                font-weight: 500;
                color: #dd5b00;
            """)
        elif subtitle_style == "warning":
            lbl_subtitle.setStyleSheet("""
                font-size: 13px;
                font-weight: 500;
                color: #dd5b00;
            """)
        else:
            lbl_subtitle.setStyleSheet("""
                font-size: 13px;
                font-weight: 400;
                color: #615d59;
            """)
        
        layout.addWidget(lbl_subtitle)
        layout.addStretch()
        
        return card
    
    def create_chart_section(self) -> QFrame:
        """Tạo section biểu đồ doanh thu (placeholder)"""
        card = QFrame()
        card.setObjectName("card")
        card.setMinimumWidth(400)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)
        
        # Header
        header_layout = QHBoxLayout()
        
        chart_title = QLabel("📊 Doanh Thu Theo Tháng")
        chart_title.setStyleSheet("""
            font-size: 16px;
            font-weight: 600;
            color: rgba(0, 0, 0, 0.95);
        """)
        header_layout.addWidget(chart_title)
        
        header_layout.addStretch()
        
        # Filter buttons
        btn_6m = QPushButton("6 tháng")
        btn_6m.setObjectName("btn-ghost")
        btn_6m.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #0075de;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(0, 117, 222, 0.08);
            }
        """)
        header_layout.addWidget(btn_6m)
        
        btn_1y = QPushButton("1 năm")
        btn_1y.setObjectName("btn-ghost")
        btn_1y.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #615d59;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.05);
            }
        """)
        header_layout.addWidget(btn_1y)
        
        layout.addLayout(header_layout)
        
        # Chart Placeholder
        placeholder = QFrame()
        placeholder.setObjectName("chart-placeholder")
        placeholder.setMinimumHeight(250)
        placeholder.setStyleSheet("""
            background-color: #f6f5f4;
            border: 2px dashed rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        """)
        
        placeholder_layout = QVBoxLayout(placeholder)
        placeholder_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        placeholder_text = QLabel("📈 Biểu đồ doanh thu\n(Chart placeholder)")
        placeholder_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        placeholder_text.setStyleSheet("""
            font-size: 14px;
            font-weight: 500;
            color: #a39e98;
        """)
        placeholder_layout.addWidget(placeholder_text)
        
        layout.addWidget(placeholder)
        
        # Chart legend (dummy)
        legend_layout = QHBoxLayout()
        legend_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        legend_layout.setSpacing(24)
        
        # Legend items
        legend_items = [
            ("🟦 Doanh thu", "#0075de"),
            ("🟩 Lợi nhuận", "#1aae39"),
            ("🟨 Dự kiến", "#fbbf24"),
        ]
        
        for text, color in legend_items:
            lbl = QLabel(text)
            lbl.setStyleSheet(f"""
                font-size: 12px;
                font-weight: 500;
                color: #615d59;
            """)
            legend_layout.addWidget(lbl)
        
        layout.addLayout(legend_layout)
        
        return card
    
    def create_recent_contracts_section(self) -> QFrame:
        """Tạo section hợp đồng gần đây"""
        card = QFrame()
        card.setObjectName("card")
        card.setMinimumWidth(350)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)
        
        # Header
        header_layout = QHBoxLayout()
        
        contracts_title = QLabel("📋 Hợp Đồng Gần Đây")
        contracts_title.setStyleSheet("""
            font-size: 16px;
            font-weight: 600;
            color: rgba(0, 0, 0, 0.95);
        """)
        header_layout.addWidget(contracts_title)
        
        header_layout.addStretch()
        
        btn_view_all = QPushButton("Xem tất cả →")
        btn_view_all.setObjectName("btn-ghost")
        btn_view_all.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #0075de;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                text-decoration: underline;
            }
        """)
        header_layout.addWidget(btn_view_all)
        
        layout.addLayout(header_layout)
        
        # Contracts table
        self.contracts_table = QTableWidget()
        self.contracts_table.setObjectName("contracts-table")
        self.contracts_table.setColumnCount(4)
        self.contracts_table.setHorizontalHeaderLabels([
            "Mã HĐ", "Khách hàng", "Giá trị", "Trạng thái"
        ])
        
        # Table styling
        self.contracts_table.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                border: none;
                gridline-color: transparent;
            }
            QTableWidget::item {
                padding: 12px 8px;
                border-bottom: 1px solid rgba(0, 0, 0, 0.05);
            }
            QHeaderView::section {
                background-color: transparent;
                color: #615d59;
                padding: 8px;
                font-weight: 600;
                font-size: 12px;
                border: none;
                text-transform: uppercase;
            }
        """)
        
        # Hide grid, set selection mode
        self.contracts_table.setShowGrid(False)
        self.contracts_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.contracts_table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.contracts_table.verticalHeader().setVisible(False)
        
        # Column widths
        self.contracts_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        self.contracts_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.contracts_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        self.contracts_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        
        self.contracts_table.setColumnWidth(0, 70)
        self.contracts_table.setColumnWidth(2, 90)
        self.contracts_table.setColumnWidth(3, 90)
        
        layout.addWidget(self.contracts_table)
        
        return card
    
    def load_dummy_data(self):
        """Load dummy data cho contracts table"""
        dummy_contracts = [
            {"ma": "HD0042", "khach": "Nguyễn Văn An", "gia": "1.2 tỷ", "trang_thai": "Mới", "status_type": "new"},
            {"ma": "HD0041", "khach": "Công ty TNHH B", "gia": "850tr", "trang_thai": "Đã TT", "status_type": "paid"},
            {"ma": "HD0040", "khach": "Trần Thị C", "gia": "2.1 tỷ", "trang_thai": "Đã giao", "status_type": "delivered"},
            {"ma": "HD0039", "khach": "Lê Văn D", "gia": "650tr", "trang_thai": "Đã TT", "status_type": "paid"},
            {"ma": "HD0038", "khach": "Phạm Thị E", "gia": "1.8 tỷ", "trang_thai": "Mới", "status_type": "new"},
        ]
        
        self.contracts_table.setRowCount(len(dummy_contracts))
        
        for row, contract in enumerate(dummy_contracts):
            # Mã HĐ
            item_ma = QTableWidgetItem(contract["ma"])
            item_ma.setFont(QFont("Inter", 13, QFont.Weight.Medium))
            self.contracts_table.setItem(row, 0, item_ma)
            
            # Khách hàng
            item_khach = QTableWidgetItem(contract["khach"])
            item_khach.setFont(QFont("Inter", 13))
            self.contracts_table.setItem(row, 1, item_khach)
            
            # Giá trị
            item_gia = QTableWidgetItem(contract["gia"])
            item_gia.setFont(QFont("Inter", 13, QFont.Weight.Medium))
            item_gia.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.contracts_table.setItem(row, 2, item_gia)
            
            # Trạng thái (custom widget for pill badge)
            status_widget = self.create_status_pill(contract["trang_thai"], contract["status_type"])
            self.contracts_table.setCellWidget(row, 3, status_widget)
            
            # Set row height
            self.contracts_table.setRowHeight(row, 44)
    
    def create_status_pill(self, text: str, status_type: str) -> QLabel:
        """Tạo pill badge cho trạng thái"""
        pill = QLabel(text)
        pill.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        if status_type == "new":
            pill.setStyleSheet("""
                background-color: #f2f9ff;
                color: #097fe8;
                border-radius: 9999px;
                padding: 4px 10px;
                font-size: 11px;
                font-weight: 600;
            """)
        elif status_type == "paid":
            pill.setStyleSheet("""
                background-color: #f0fdf4;
                color: #1aae39;
                border-radius: 9999px;
                padding: 4px 10px;
                font-size: 11px;
                font-weight: 600;
            """)
        elif status_type == "delivered":
            pill.setStyleSheet("""
                background-color: #f6f5f4;
                color: #615d59;
                border-radius: 9999px;
                padding: 4px 10px;
                font-size: 11px;
                font-weight: 600;
            """)
        else:
            pill.setStyleSheet("""
                background-color: #f6f5f4;
                color: #615d59;
                border-radius: 9999px;
                padding: 4px 10px;
                font-size: 11px;
                font-weight: 600;
            """)
        
        return pill