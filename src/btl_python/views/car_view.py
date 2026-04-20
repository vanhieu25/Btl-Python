#!/usr/bin/env python3
"""
Console UI for car management following Apple design system principles
Based on design/DESIGN.md
"""

from typing import List
from ..models import Car
from ..controllers.car_controller import CarController
from ..database.connection import SessionLocal


class CarView:
    """Console UI for car management following Apple design system"""
    
    def __init__(self):
        self.db = SessionLocal()
        self.controller = CarController(self.db)
    
    def display_menu(self):
        """Display main menu following Apple design principles"""
        print("\n" + "="*70)
        print("🚗 PHẦN MỀM QUẢN LÝ ĐẠI LÝ XE HƠI")
        print("="*70)
        print("Apple-inspired design system")
        print("Pure functionality with elegant simplicity")
        print("="*70)
        print("1. 📋 Hiển thị danh sách xe")
        print("2. ➕ Thêm xe mới")
        print("3. 🔍 Tìm kiếm xe")
        print("4. ✏️ Cập nhật thông tin xe")
        print("5. 🗑️ Xóa xe")
        print("6. 🏠 Quay lại menu chính")
        print("="*70)
    
    def display_cars(self, cars: List[Car]):
        """Display list of cars following Apple typography and spacing"""
        if not cars:
            print("\n❌ Không có xe nào trong hệ thống.")
            print("   This space intentionally left empty.")
            return
        
        print(f"\n📋 DANH SÁCH XE ({len(cars)} xe được tìm thấy):")
        print("─" * 140)  # Using full-width line separator
        
        # Apple-style typography: tight line heights, precise alignment
        header_format = "{:<12} {:<18} {:<22} {:<10} {:<15} {:<18} {:<12} {}"
        print(header_format.format(
            "MÃ XE", "HÃNG", "DÒNG XE", "NĂM SX", 
            "MÀU SẮC", "GIÁ BÁN", "TỒN KHO", "TRẠNG THÁI"
        ))
        print("─" * 140)
        
        for i, car in enumerate(cars):
            # Use Apple's approach: clean, precise formatting
            price_str = f"{car.price:,.0f} VNĐ"
            status_symbol = "🟢" if car.stock_quantity > 0 else "🔴"
            status_display = f"{status_symbol} {car.status}"
            
            print(header_format.format(
                car.car_code, 
                car.brand, 
                car.model, 
                str(car.year), 
                car.color or "N/A", 
                price_str, 
                str(car.stock_quantity), 
                status_display
            ))
            
            # Add subtle spacing between items (Apple's cinematic breathing room)
            if i < len(cars) - 1:
                print()  # Additional line for breathing room
    
    def add_car(self):
        """Add new car with Apple-style form design"""
        print("\n➕ THÊM XE MỚI")
        print("─" * 40)
        print("Vui lòng nhập thông tin xe:")
        print("─" * 40)
        
        try:
            car_code = input("Mã xe (bắt buộc): ").strip()
            if not car_code:
                print("\n❌ Mã xe là bắt buộc!")
                return
                
            brand = input("Hãng xe (bắt buộc): ").strip()
            if not brand:
                print("\n❌ Hãng xe là bắt buộc!")
                return
                
            model = input("Dòng xe (bắt buộc): ").strip()
            if not model:
                print("\n❌ Dòng xe là bắt buộc!")
                return
                
            year_input = input("Năm sản xuất (bắt buộc): ").strip()
            if not year_input:
                print("\n❌ Năm sản xuất là bắt buộc!")
                return
            year = int(year_input)
            
            color = input("Màu sắc (có thể bỏ trống): ").strip() or None
            price_input = input("Giá bán (VNĐ, bắt buộc): ").strip()
            if not price_input:
                print("\n❌ Giá bán là bắt buộc!")
                return
            price = float(price_input)
            
            stock_input = input("Số lượng tồn kho (mặc định 0): ").strip()
            stock_quantity = int(stock_input) if stock_input else 0
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
            
            # Apple-style success message
            print(f"\n✅ THÀNH CÔNG!")
            print("─" * 40)
            print(f"  Mã xe:     {car.car_code}")
            print(f"  Hãng:      {car.brand}")
            print(f"  Dòng xe:   {car.model}")
            print(f"  Năm SX:    {car.year}")
            print(f"  Giá bán:   {car.price:,.0f} VNĐ")
            print(f"  Tồn kho:   {car.stock_quantity}")
            print("─" * 40)
            print("  Xe đã được thêm vào hệ thống.")
            
        except ValueError as e:
            print(f"\n❌ LỖI NHẬP LIỆU: Vui lòng nhập giá trị hợp lệ.")
        except Exception as e:
            print(f"\n❌ LỖI KHÔNG XÁC ĐỊNH: {str(e)}")
    
    def search_cars(self):
        """Search cars with Apple-style input and feedback"""
        print("\n🔍 TÌM KIẾM XE")
        print("─" * 40)
        print("Nhập tiêu chí tìm kiếm (bỏ trống nếu không cần lọc):")
        print("─" * 40)
        
        brand = input("Hãng xe (ví dụ: Toyota): ").strip() or None
        model = input("Dòng xe (ví dụ: Camry): ").strip() or None
        year_from = input("Năm SX từ (ví dụ: 2020): ").strip() or None
        year_to = input("Năm SX đến (ví dụ: 2024): ").strip() or None
        price_from = input("Giá từ (VNĐ): ").strip() or None
        price_to = input("Giá đến (VNĐ): ").strip() or None
        
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
            
            print(f"\n🔍 Đang tìm xe...")
            print(f"   Hãng: {brand or 'Bất kỳ'}")
            print(f"   Dòng xe: {model or 'Bất kỳ'}")
            print(f"   Năm: {f'{year_from}-{year_to}' if year_from or year_to else 'Bất kỳ'}")
            print(f"   Giá: {f'{price_from:,.0f}-{price_to:,.0f} VNĐ' if price_from or price_to else 'Bất kỳ'}")
            print()
            
            self.display_cars(cars)
            
        except ValueError:
            print("\n❌ LỖI: Vui lòng nhập số hợp lệ cho năm và giá!")
    
    def update_car(self):
        """Update car information with Apple-style feedback"""
        print("\n✏️ CẬP NHẬT THÔNG TIN XE")
        print("─" * 40)
        
        try:
            car_id = int(input("ID xe cần cập nhật: "))
            car = self.controller.get_car_by_id(car_id)
            
            if not car:
                print("\n❌ KHÔNG TÌM THẤY XE")
                print(f"   Không có xe nào với ID {car_id}")
                return
            
            print(f"\n📋 THÔNG TIN XE HIỆN TẠI:")
            print("─" * 40)
            print(f"  Mã xe:      {car.car_code}")
            print(f"  Hãng:       {car.brand}")
            print(f"  Dòng xe:    {car.model}")
            print(f"  Năm SX:     {car.year}")
            print(f"  Giá bán:    {car.price:,.0f} VNĐ")
            print(f"  Tồn kho:    {car.stock_quantity}")
            print(f"  Trạng thái: {car.status}")
            print("─" * 40)
            print("  Nhập thông tin mới (bỏ trống để giữ nguyên):")
            print("─" * 40)
            
            # Allow updating fields (except car_code)
            brand_input = input(f"  Hãng xe mới (hiện tại: {car.brand}): ").strip()
            brand = brand_input if brand_input else car.brand
            
            model_input = input(f"  Dòng xe mới (hiện tại: {car.model}): ").strip()
            model = model_input if model_input else car.model
            
            year_input = input(f"  Năm SX mới (hiện tại: {car.year}): ").strip()
            year = int(year_input) if year_input else car.year
            
            color_input = input(f"  Màu sắc mới (hiện tại: {car.color or 'N/A'}): ").strip()
            color = color_input if color_input else car.color
            
            price_input = input(f"  Giá bán mới (hiện tại: {car.price:,.0f}): ").strip()
            price = float(price_input) if price_input else car.price
            
            stock_input = input(f"  Tồn kho mới (hiện tại: {car.stock_quantity}): ").strip()
            stock_quantity = int(stock_input) if stock_input else car.stock_quantity
            
            status_input = input(f"  Trạng thái mới (hiện tại: {car.status}): ").strip()
            status = status_input if status_input else car.status
            
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
                print(f"\n✅ CẬP NHẬT THÀNH CÔNG!")
                print("─" * 40)
                print(f"  Mã xe:      {updated_car.car_code}")
                print(f"  Hãng:       {updated_car.brand}")
                print(f"  Dòng xe:    {updated_car.model}")
                print(f"  Giá bán:    {updated_car.price:,.0f} VNĐ")
                print("─" * 40)
                print("  Thông tin xe đã được cập nhật.")
            else:
                print("\n❌ CẬP NHẬT THẤT BẠI!")
                print("   Không thể cập nhật thông tin xe.")
                
        except ValueError as e:
            print(f"\n❌ LỖI NHẬP LIỆU: Vui lòng nhập giá trị hợp lệ.")
        except Exception as e:
            print(f"\n❌ LỖI KHÔNG XÁC ĐỊNH: {str(e)}")
    
    def delete_car(self):
        """Delete car with Apple-style confirmation"""
        print("\n🗑️ XÓA XE")
        print("─" * 40)
        
        try:
            car_id = int(input("ID xe cần xóa: "))
            car = self.controller.get_car_by_id(car_id)
            
            if not car:
                print("\n❌ KHÔNG TÌM THẤY XE")
                print(f"   Không có xe nào với ID {car_id}")
                return
            
            print(f"\n📋 THÔNG TIN XE CẦN XÓA:")
            print("─" * 40)
            print(f"  Mã xe:      {car.car_code}")
            print(f"  Hãng:       {car.brand}")
            print(f"  Dòng xe:    {car.model}")
            print(f"  Giá bán:    {car.price:,.0f} VNĐ")
            print(f"  Tồn kho:    {car.stock_quantity}")
            print("─" * 40)
            
            print("⚠️  CẢNH BÁO:")
            print("   Hành động này không thể hoàn tác.")
            print("   Tất cả thông tin liên quan sẽ bị xóa.")
            print()
            confirm = input("Bạn có chắc chắn muốn xóa xe này? (gõ 'DELETE' để xác nhận): ")
            
            if confirm.strip() == 'DELETE':
                if self.controller.delete_car(car_id):
                    print(f"\n✅ XÓA THÀNH CÔNG!")
                    print(f"   Xe {car.car_code} đã được xóa khỏi hệ thống.")
                else:
                    print(f"\n❌ XÓA THẤT BẠI!")
                    print("   Không thể xóa xe này.")
            else:
                print(f"\n❌ HỦY XÓA XE.")
                print("   Hành động xóa đã được hủy.")
                
        except ValueError:
            print(f"\n❌ LỖI: Vui lòng nhập ID hợp lệ!")
        except Exception as e:
            print(f"\n❌ LỖI: {str(e)}")
    
    def run(self):
        """Run the car management interface"""
        while True:
            self.display_menu()
            choice = input("\nChọn chức năng (1-6): ").strip()
            
            if choice == '1':
                print("\n⏳ Đang tải danh sách xe...")
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
                print("\n🏠 Quay lại menu chính...")
                print("─" * 40)
                break
            else:
                print("\n❌ LỰA CHỌN KHÔNG HỢP LỆ!")
                print("   Vui lòng chọn một số từ 1 đến 6.")