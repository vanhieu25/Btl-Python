"""
Main Window Demo - Cửa sổ chính với sidebar navigation
Notion-inspired design
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QStackedWidget, QFrame, QSizePolicy
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont

# Import views
from views.dashboard_demo import DashboardDemo


class MainWindowDemo(QMainWindow):
    """Main window với sidebar navigation và content area"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản Lý Đại Lý Xe Hơi - Demo")
        self.setMinimumSize(1400, 900)
        self.setGeometry(100, 100, 1400, 900)
        
        self.current_view = "dashboard"
        self.nav_buttons = {}
        
        self.init_ui()
        self.apply_stylesheet()
    
    def init_ui(self):
        """Khởi tạo giao diện chính"""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout: Sidebar + Content
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar, 0)
        
        # Content area
        self.content_stack = QStackedWidget()
        self.content_stack.setObjectName("content-stack")
        main_layout.addWidget(self.content_stack, 1)
        
        # Add views
        self.setup_views()
    
    def create_sidebar(self) -> QFrame:
        """Tạo sidebar với navigation"""
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(260)
        sidebar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        
        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(20, 24, 20, 24)
        layout.setSpacing(4)
        
        # Logo section
        logo_widget = QWidget()
        logo_layout = QHBoxLayout(logo_widget)
        logo_layout.setContentsMargins(0, 0, 0, 0)
        logo_layout.setSpacing(8)
        
        # Logo icon (emoji hoặc text)
        logo_icon = QLabel("🚗")
        logo_icon.setStyleSheet("font-size: 24px;")
        logo_layout.addWidget(logo_icon)
        
        # Logo text
        logo_text = QLabel("Đại Lý Xe")
        logo_text.setObjectName("sidebar-logo")
        logo_text.setStyleSheet("""
            font-size: 20px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
        """)
        logo_layout.addWidget(logo_text)
        logo_layout.addStretch()
        
        layout.addWidget(logo_widget)
        
        # Separator
        separator = QFrame()
        separator.setObjectName("separator")
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet("background-color: rgba(0, 0, 0, 0.1); max-height: 1px;")
        separator.setFixedHeight(1)
        layout.addSpacing(16)
        layout.addWidget(separator)
        layout.addSpacing(16)
        
        # Navigation buttons
        nav_items = [
            ("dashboard", "📊", "Dashboard"),
            ("xe", "🚙", "Quản lý Xe"),
            ("khachhang", "👥", "Khách Hàng"),
            ("hopdong", "📄", "Hợp Đồng"),
            ("nhanvien", "👨‍💼", "Nhân Viên"),
            ("baocao", "📈", "Báo Cáo"),
        ]
        
        for view_id, icon, label in nav_items:
            btn = self.create_nav_button(view_id, icon, label)
            self.nav_buttons[view_id] = btn
            layout.addWidget(btn)
        
        layout.addStretch()
        
        # User section at bottom
        user_separator = QFrame()
        user_separator.setFrameShape(QFrame.Shape.HLine)
        user_separator.setStyleSheet("background-color: rgba(0, 0, 0, 0.1); max-height: 1px;")
        user_separator.setFixedHeight(1)
        layout.addWidget(user_separator)
        layout.addSpacing(16)
        
        # User info
        user_widget = QWidget()
        user_layout = QHBoxLayout(user_widget)
        user_layout.setContentsMargins(12, 8, 12, 8)
        user_layout.setSpacing(12)
        
        # Avatar placeholder
        avatar = QLabel("👤")
        avatar.setStyleSheet("""
            font-size: 20px;
            background-color: rgba(0, 0, 0, 0.05);
            border-radius: 16px;
            padding: 4px;
        """)
        user_layout.addWidget(avatar)
        
        # User name
        user_name = QLabel("Admin")
        user_name.setStyleSheet("""
            font-size: 14px;
            font-weight: 600;
            color: rgba(0, 0, 0, 0.95);
        """)
        user_layout.addWidget(user_name)
        user_layout.addStretch()
        
        layout.addWidget(user_widget)
        
        return sidebar
    
    def create_nav_button(self, view_id: str, icon: str, label: str) -> QPushButton:
        """Tạo navigation button"""
        btn = QPushButton(f"{icon}  {label}")
        btn.setObjectName("nav-btn")
        btn.setCheckable(True)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # Set active if current view
        if view_id == self.current_view:
            btn.setChecked(True)
            btn.setObjectName("nav-btn-active")
        
        # Style
        btn.setStyleSheet(self.get_nav_button_style(view_id == self.current_view))
        
        # Connect click
        btn.clicked.connect(lambda: self.switch_view(view_id))
        
        return btn
    
    def get_nav_button_style(self, is_active: bool) -> str:
        """Get style cho nav button"""
        if is_active:
            return """
                QPushButton {
                    text-align: left;
                    padding: 12px 16px;
                    border: none;
                    border-radius: 8px;
                    font-size: 14px;
                    font-weight: 600;
                    color: rgba(0, 0, 0, 0.95);
                    background-color: rgba(0, 0, 0, 0.08);
                }
            """
        else:
            return """
                QPushButton {
                    text-align: left;
                    padding: 12px 16px;
                    border: none;
                    border-radius: 8px;
                    font-size: 14px;
                    font-weight: 500;
                    color: rgba(0, 0, 0, 0.85);
                    background: transparent;
                }
                QPushButton:hover {
                    background-color: rgba(0, 0, 0, 0.05);
                }
            """
    
    def setup_views(self):
        """Setup các views cho content area"""
        # Dashboard
        self.dashboard_view = DashboardDemo()
        self.content_stack.addWidget(self.dashboard_view)
        
        # Placeholder views for other sections
        self.xe_view = self.create_placeholder_view("Quản lý Xe", "🚙")
        self.khachhang_view = self.create_placeholder_view("Khách Hàng", "👥")
        self.hopdong_view = self.create_placeholder_view("Hợp Đồng", "📄")
        self.nhanvien_view = self.create_placeholder_view("Nhân Viên", "👨‍💼")
        self.baocao_view = self.create_placeholder_view("Báo Cáo", "📈")
        
        self.content_stack.addWidget(self.xe_view)
        self.content_stack.addWidget(self.khachhang_view)
        self.content_stack.addWidget(self.hopdong_view)
        self.content_stack.addWidget(self.nhanvien_view)
        self.content_stack.addWidget(self.baocao_view)
    
    def create_placeholder_view(self, title: str, icon: str) -> QWidget:
        """Tạo placeholder view cho các màn hình chưa hoàn thiện"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        icon_label = QLabel(icon)
        icon_label.setStyleSheet("font-size: 64px; margin-bottom: 16px;")
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(icon_label)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: rgba(0, 0, 0, 0.95);
            margin-bottom: 8px;
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        subtitle = QLabel("(Đang phát triển)")
        subtitle.setStyleSheet("""
            font-size: 14px;
            color: #615d59;
        """)
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle)
        
        return widget
    
    def switch_view(self, view_id: str):
        """Chuyển đổi giữa các views"""
        self.current_view = view_id
        
        # Update nav button styles
        for vid, btn in self.nav_buttons.items():
            btn.setObjectName("nav-btn-active" if vid == view_id else "nav-btn")
            btn.setStyleSheet(self.get_nav_button_style(vid == view_id))
        
        # Switch content
        view_map = {
            "dashboard": 0,
            "xe": 1,
            "khachhang": 2,
            "hopdong": 3,
            "nhanvien": 4,
            "baocao": 5,
        }
        
        if view_id in view_map:
            self.content_stack.setCurrentIndex(view_map[view_id])
    
    def apply_stylesheet(self):
        """Apply stylesheet từ file"""
        try:
            with open("styles/notion_theme.qss", "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print("Warning: notion_theme.qss not found, using default styles")


def main():
    """Entry point"""
    app = QApplication(sys.argv)
    app.setApplicationName("Quản Lý Đại Lý Xe Hơi - Demo")
    app.setApplicationVersion("1.0.0")
    
    # Set application font
    font = QFont("Inter", 10)
    font.setStyleHint(QFont.StyleHint.SansSerif)
    app.setFont(font)
    
    window = MainWindowDemo()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()