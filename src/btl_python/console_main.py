#!/usr/bin/env python3
"""
Main console application for Btl Python following Apple design system
"""

from .views.car_view import CarView


def main():
    """Main application entry point with Apple design principles"""
    print("┌" + "─" * 78 + "┐")
    print("│" + " " * 78 + "│")
    print("│" + " " * 25 + "🚗 PHẦN MỀM QUẢN LÝ ĐẠI LÝ XE HƠI" + " " * 24 + "│")
    print("│" + " " * 30 + "Apple-inspired design" + " " * 30 + "│")
    print("│" + " " * 78 + "│")
    print("└" + "─" * 78 + "┘")
    
    print()
    
    while True:
        print("┌" + "─" * 50 + "┐")
        print("│" + " " * 50 + "│")
        print("│" + " " * 15 + "📋 MENU CHÍNH" + " " * 21 + "│")
        print("│" + " " * 50 + "│")
        print("│" + " " * 5 + "1. 🚗 Quản lý xe" + " " * 29 + "│")
        print("│" + " " * 5 + "2. 🚪 Thoát chương trình" + " " * 21 + "│")
        print("│" + " " * 50 + "│")
        print("└" + "─" * 50 + "┘")
        
        choice = input("\nChọn chức năng (1-2): ").strip()
        
        if choice == '1':
            print("\n┌" + "─" * 30 + "┐")
            print("│" + " " * 30 + "│")
            print("│" + " " * 8 + "🔧 ĐANG MỞ" + " " * 12 + "│")
            print("│" + " " * 8 + "QUẢN LÝ XE" + " " * 11 + "│")
            print("│" + " " * 30 + "│")
            print("└" + "─" * 30 + "┘")
            print()
            
            car_view = CarView()
            car_view.run()
        elif choice == '2':
            print("\n┌" + "─" * 40 + "┐")
            print("│" + " " * 40 + "│")
            print("│" + " " * 10 + "👋 CẢM ƠN BẠN!" + " " * 14 + "│")
            print("│" + " " * 8 + "HẸN GẶP LẠI SAU" + " " * 11 + "│")
            print("│" + " " * 40 + "│")
            print("└" + "─" * 40 + "┘")
            break
        else:
            print("\n❌ Lựa chọn không hợp lệ! Vui lòng chọn 1-2.")
            print()


if __name__ == "__main__":
    main()