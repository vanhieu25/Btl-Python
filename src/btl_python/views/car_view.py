"""
Car View - Console-based UI for car management
"""

from typing import List
from ..models import Car
from ..controllers.car_controller import CarController
from ..database.connection import SessionLocal


class CarView:
    """Console UI for car management"""
    
    def __init__(self):
        self.db = SessionLocal()
        self.controller = CarController(self.db)
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("🚗 QUẢN LÝ XE")
        print("="*50)
        print("1. Hiển thị danh sách xe")
        print("2. Thêm xe mới")
        print("3. Tìm kiếm xe")
        print("4. Cập nhật thông tin xe")
        print("5. Xóa xe")
        print("6. Quay lại menu chính")
        print("="*50)
    
    def display_cars(self, cars: List[Car]):
        """Display list of cars"""
        if not cars:
            print("\n❌ Không có xe nào trong hệ thống.")
            return
        
        print(f"\n📋 Danh sách xe ({len(cars)} xe):")
        print("-" * 120)
        print(f"{'Mã xe':<10} {'Hãng':<15} {'Dòng xe':<20} {'Năm SX':<8} {'Màu sắc':<12} {'Giá bán':<15} {'Tồn kho':<10} {'Trạng thái'}")
        print("-" * 120)
        
        for car in cars:
            price_str = f"{car.price:,.0f} VNĐ"
            print(f"{car.car_code:<10} {car.brand:<15} {car.model:<20} {car.year:<8} {car.color or 'N/A':<12} {price_str:<15} {car.stock_quantity:<10} {car.status}")
    
    def add_car(self):
        """Add new car"""
        print("\n➕ THÊM XE MỚI")
        try:
            car_code = input("Mã xe (bắt buộc): ").strip()
            brand = input("Hãng xe (bắt buộc): ").strip()
            model = input("Dòng xe (bắt buộc): ").strip()
            year = int(input("Năm sản xuất (bắt buộc): "))
            color = input("Màu sắc (có thể bỏ trống): ").strip() or None
            price = float(input("Giá bán (VNĐ, bắt buộc): "))
            stock_quantity = int(input("Số lượng tồn kho (mặc định 0): ") or "0")
            description = input("Mô tả (có thể bỏ trống): ").strip() or None
            
            car = self.controller.create_car(
                car_code=car_code,
                brand=brand,
                model=model,
                year=year,
                color=color,
                price=price,
                stock_quantity=stock_quantity,
                description=description
            )
            
            print(f"\n✅ Thêm xe thành công! Mã xe: {car.car_code}")
            
        except ValueError as e:
            print(f"\n❌ Lỗi: {e}")
        except Exception as e:
            print(f"\n❌ Lỗi không xác định: {e}")
    
    def search_cars(self):
        """Search cars"""
        print("\n🔍 TÌM KIẾM XE")
        brand = input("Hãng xe (có thể bỏ trống): ").strip() or None
        model = input("Dòng xe (có thể bỏ trống): ").strip() or None
        year_from = input("Năm SX từ (có thể bỏ trống): ").strip() or None
        year_to = input("Năm SX đến (có thể bỏ trống): ").strip() or None
        price_from = input("Giá từ (có thể bỏ trống): ").strip() or None
        price_to = input("Giá đến (có thể bỏ trống): ").strip() or None
        
        # Convert to appropriate types
        try:
            year_from = int(year_from) if year_from else None
            year_to = int(year_to) if year_to else None
            price_from = float(price_from) if price_from else None
            price_to = float(price_to) if price_to else None
            
            cars = self.controller.search_cars(
                brand=brand,
                model=model,
                year_from=year_from,
                year_to=year_to,
                price_from=price_from,
                price_to=price_to
            )
            
            self.display_cars(cars)
            
        except ValueError:
            print("\n❌ Lỗi: Vui lòng nhập số hợp lệ cho năm và giá!")
    
    def update_car(self):
        """Update car information"""
        print("\n✏️ CẬP NHẬT THÔNG TIN XE")
        try:
            car_id = int(input("ID xe cần cập nhật: "))
            car = self.controller.get_car_by_id(car_id)
            
            if not car:
                print("\n❌ Không tìm thấy xe với ID này!")
                return
            
            print(f"\nXe hiện tại: {car.car_code} - {car.brand} {car.model}")
            
            # Allow updating fields (except car_code)
            brand = input(f"Hãng xe mới (hiện tại: {car.brand}): ").strip() or car.brand
            model = input(f"Dòng xe mới (hiện tại: {car.model}): ").strip() or car.model
            year = input(f"Năm SX mới (hiện tại: {car.year}): ").strip() or str(car.year)
            color = input(f"Màu sắc mới (hiện tại: {car.color or 'N/A'}): ").strip() or car.color
            price = input(f"Giá bán mới (hiện tại: {car.price:,.0f}): ").strip() or str(car.price)
            stock_quantity = input(f"Tồn kho mới (hiện tại: {car.stock_quantity}): ").strip() or str(car.stock_quantity)
            status = input(f"Trạng thái mới (hiện tại: {car.status}): ").strip() or car.status
            
            # Convert types
            year = int(year)
            price = float(price)
            stock_quantity = int(stock_quantity)
            
            updated_car = self.controller.update_car(
                car_id=car_id,
                brand=brand,
                model=model,
                year=year,
                color=color,
                price=price,
                stock_quantity=stock_quantity,
                status=status
            )
            
            if updated_car:
                print(f"\n✅ Cập nhật xe thành công! Mã xe: {updated_car.car_code}")
            else:
                print("\n❌ Cập nhật thất bại!")
                
        except ValueError as e:
            print(f"\n❌ Lỗi: {e}")
        except Exception as e:
            print(f"\n❌ Lỗi không xác định: {e}")
    
    def delete_car(self):
        """Delete car"""
        print("\n🗑️ XÓA XE")
        try:
            car_id = int(input("ID xe cần xóa: "))
            car = self.controller.get_car_by_id(car_id)
            
            if not car:
                print("\n❌ Không tìm thấy xe với ID này!")
                return
            
            confirm = input(f"Bạn có chắc muốn xóa xe {car.car_code} - {car.brand} {car.model}? (y/N): ")
            
            if confirm.lower() == 'y':
                if self.controller.delete_car(car_id):
                    print(f"\n✅ Xóa xe thành công!")
                else:
                    print("\n❌ Xóa xe thất bại!")
            else:
                print("\n❌ Hủy xóa xe.")
                
        except ValueError:
            print("\n❌ Lỗi: Vui lòng nhập ID hợp lệ!")
    
    def run(self):
        """Run the car management interface"""
        while True:
            self.display_menu()
            choice = input("\nChọn chức năng (1-6): ").strip()
            
            if choice == '1':
                cars = self.controller.get_all_cars()
                self.display_cars(cars)
            elif choice == '2':
                self.add_car()
            elif choice == '3':
                self.search_cars()
            elif choice == '4':
                self.update_car()
            elif choice == '5':
                self.delete_car()
            elif choice == '6':
                print("\n👋 Quay lại menu chính...")
                break
            else:
                print("\n❌ Lựa chọn không hợp lệ! Vui lòng chọn 1-6.")