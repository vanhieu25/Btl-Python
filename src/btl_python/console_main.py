"""
Main console application for Btl Python
"""

from .views.car_view import CarView


def main():
    """Main application entry point"""
    print("="*60)
    print("🚗 PHẦN MỀM QUẢN LÝ ĐẠI LÝ XE HƠI")
    print("="*60)
    
    while True:
        print("\n📋 MENU CHÍNH")
        print("-"*30)
        print("1. Quản lý xe")
        print("2. Thoát chương trình")
        print("-"*30)
        
        choice = input("\nChọn chức năng (1-2): ").strip()
        
        if choice == '1':
            car_view = CarView()
            car_view.run()
        elif choice == '2':
            print("\n👋 Cảm ơn bạn đã sử dụng phần mềm!")
            break
        else:
            print("\n❌ Lựa chọn không hợp lệ! Vui lòng chọn 1-2.")


if __name__ == "__main__":
    main()