#!/usr/bin/env python3
"""
Console UI for car management following Apple design system principles
Based on design/DESIGN.md
"""

import os
from datetime import datetime
from typing import List
from ..models import Car
from ..controllers.car_controller import CarController
from ..services.import_export_service import ImportExportService
from ..database.connection import SessionLocal


class CarView:
    """Console UI for car management following Apple design system"""
    
    def __init__(self):
        self.db = SessionLocal()
        self.controller = CarController(self.db)
        self.import_export_service = ImportExportService(self.db)
    
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
        print("3. 🔍 Tìm kiếm và lọc xe")
        print("4. ✏️ Cập nhật thông tin xe")
        print("5. 🗑️ Xóa xe")
        print("6. 📥 Nhập dữ liệu từ file")
        print("7. 📤 Xuất dữ liệu ra file")
        print("8. 🏠 Quay lại menu chính")
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
        """Search cars with Apple-style input and advanced filtering"""
        print("\n🔍 TÌM KIẾM VÀ LỌC XE NÂNG CAO")
        print("─" * 50)
        print("Nhập tiêu chí tìm kiếm (bỏ trống nếu không cần lọc):")
        print("─" * 50)
        
        # Basic search criteria
        brand = input("Hãng xe (ví dụ: Toyota, Honda): ").strip() or None
        model = input("Dòng xe (ví dụ: Camry, Civic): ").strip() or None
        color = input("Màu sắc (ví dụ: Đen, Trắng): ").strip() or None
        
        # Year range
        year_from = input("Năm SX từ (ví dụ: 2020): ").strip() or None
        year_to = input("Năm SX đến (ví dụ: 2024): ").strip() or None
        
        # Price range
        price_from = input("Giá từ (VNĐ, ví dụ: 500000000): ").strip() or None
        price_to = input("Giá đến (VNĐ, ví dụ: 2000000000): ").strip() or None
        
        # Status filter
        print("\n📋 TRẠNG THÁI XE:")
        print("   1. Còn hàng (available)")
        print("   2. Đã bán (sold)")
        print("   3. Sắp về (reserved)")
        print("   4. Tất cả trạng thái")
        status_choice = input("Chọn trạng thái (1-4): ").strip()
        
        status_map = {
            "1": "available",
            "2": "sold", 
            "3": "reserved"
        }
        status = status_map.get(status_choice, None)
        
        # Convert to appropriate types
        try:
            year_from = int(year_from) if year_from else None
            year_to = int(year_to) if year_to else None
            price_from = float(price_from) if price_from else None
            price_to = float(price_to) if price_to else None
            
            cars = self.controller.search_cars(
                brand=brand,
                model=model,
                color=color,
                year_from=year_from,
                year_to=year_to,
                price_from=price_from,
                price_to=price_to,
                status=status
            )
            
            print(f"\n🔍 KẾT QUẢ TÌM KIẾM:")
            print(f"   Hãng: {brand or 'Bất kỳ'}")
            print(f"   Dòng xe: {model or 'Bất kỳ'}")
            print(f"   Màu sắc: {color or 'Bất kỳ'}")
            print(f"   Năm: {f'{year_from}-{year_to}' if year_from or year_to else 'Bất kỳ'}")
            print(f"   Giá: {f'{price_from:,.0f}-{price_to:,.0f} VNĐ' if price_from or price_to else 'Bất kỳ'}")
            print(f"   Trạng thái: {status or 'Bất kỳ'}")
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
        """Delete car with Apple-style confirmation and contract validation"""
        print("\n🗑️ XÓA XE")
        print("─" * 40)
        
        try:
            car_id = int(input("ID xe cần xóa: "))
            car = self.controller.get_car_by_id(car_id)
            
            if not car:
                print("\n❌ KHÔNG TÌM THẤY XE")
                print(f"   Không có xe nào với ID {car_id}")
                return
            
            # Check if car has contracts before deletion
            if len(car.contracts) > 0:
                print(f"\n⚠️  KHÔNG THỂ XÓA XE")
                print(f"   Xe {car.car_code} có {len(car.contracts)} hợp đồng liên quan.")
                print(f"   Vui lòng hủy/xử lý các hợp đồng trước khi xóa xe.")
                print("─" * 40)
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
    
    def import_cars(self):
        """Import cars from file with Apple-style interface"""
        print("\n📥 NHẬP DỮ LIỆU XE TỪ FILE")
        print("─" * 50)
        print("Hỗ trợ định dạng: Excel (.xlsx) và CSV (.csv)")
        print("─" * 50)
        
        try:
            filename = input("Nhập đường dẫn file (hoặc kéo thả file vào đây): ").strip()
            if not filename:
                print("\n❌ Đường dẫn file không được để trống!")
                return
            
            # Remove quotes if user copied with quotes
            filename = filename.strip('\"\'')
            
            if not os.path.exists(filename):
                print(f"\n❌ KHÔNG TÌM THẤY FILE!")
                print(f"   File '{filename}' không tồn tại.")
                return
            
            # Determine file type
            if filename.lower().endswith('.xlsx'):
                file_type = 'Excel'
            elif filename.lower().endswith('.csv'):
                file_type = 'CSV'
            else:
                print(f"\n❌ ĐỊNH DẠNG KHÔNG HỖ TRỢ!")
                print("   Chỉ hỗ trợ file .xlsx (Excel) và .csv (CSV)")
                return
            
            print(f"\n🔄 ĐANG NHẬP DỮ LIỆU TỪ FILE {file_type}...")
            print(f"   File: {filename}")
            
            # Ask about duplicate handling
            print("\n📋 XỬ LÝ DỮ LIỆU TRÙNG:")
            print("   1. Bỏ qua dữ liệu trùng (mặc định)")
            print("   2. Cập nhật dữ liệu trùng")
            duplicate_choice = input("Chọn phương thức (1-2): ").strip()
            skip_duplicates = duplicate_choice != '2'
            
            # Import data
            if file_type == 'Excel':
                success_count, error_count, errors = self.import_export_service.import_cars_from_excel(
                    filename, skip_duplicates=skip_duplicates
                )
            else:
                success_count, error_count, errors = self.import_export_service.import_cars_from_csv(
                    filename, skip_duplicates=skip_duplicates
                )
            
            # Display results
            print(f"\n✅ NHẬP DỮ LIỆU HOÀN TẤT!")
            print("─" * 50)
            print(f"   Thành công: {success_count} xe")
            print(f"   Lỗi:       {error_count} dòng")
            
            if errors:
                print(f"\n⚠️  CHI TIẾT LỖI:")
                for error in errors[:5]:  # Show first 5 errors
                    print(f"   • {error}")
                if len(errors) > 5:
                    print(f"   • ... và {len(errors) - 5} lỗi khác")
            
            print("─" * 50)
            
        except Exception as e:
            print(f"\n❌ LỖI NHẬP DỮ LIỆU: {str(e)}")
    
    def export_cars(self):
        """Export cars to file with Apple-style interface"""
        print("\n📤 XUẤT DỮ LIỆU XE RA FILE")
        print("─" * 50)
        print("Hỗ trợ định dạng: Excel (.xlsx) và CSV (.csv)")
        print("─" * 50)
        
        try:
            # Get export scope
            print("📋 PHẠM VI XUẤT DỮ LIỆU:")
            print("   1. Toàn bộ danh sách xe")
            print("   2. Kết quả tìm kiếm hiện tại")
            scope_choice = input("Chọn phạm vi (1-2): ").strip()
            
            cars = None
            if scope_choice == '2':
                # Use current search results (simplified - just get all for now)
                cars = self.controller.get_all_cars()
                print("   (Lưu ý: Hiện tại chỉ hỗ trợ xuất toàn bộ danh sách)")
            
            # Choose file format
            print("\n📄 ĐỊNH DẠNG FILE:")
            print("   1. Excel (.xlsx)")
            print("   2. CSV (.csv)")
            format_choice = input("Chọn định dạng (1-2): ").strip()
            
            file_extension = '.xlsx' if format_choice == '1' else '.csv'
            default_filename = f"danh_sach_xe_{datetime.now().strftime('%Y%m%d_%H%M%S')}{file_extension}"
            
            filename = input(f"\nNhập tên file (mặc định: {default_filename}): ").strip()
            if not filename:
                filename = default_filename
            
            # Add extension if not provided
            if not filename.endswith(file_extension):
                filename += file_extension
            
            # Ensure exports directory exists
            export_dir = "exports"
            full_path = os.path.join(export_dir, filename)
            
            print(f"\n🔄 ĐANG XUẤT DỮ LIỆU...")
            print(f"   File: {full_path}")
            
            # Export data
            if file_extension == '.xlsx':
                exported_file = self.import_export_service.export_cars_to_excel(full_path, cars)
            else:
                exported_file = self.import_export_service.export_cars_to_csv(full_path, cars)
            
            print(f"\n✅ XUẤT DỮ LIỆU HOÀN TẤT!")
            print("─" * 50)
            print(f"   File đã được lưu tại:")
            print(f"   {exported_file}")
            print("─" * 50)
            
        except Exception as e:
            print(f"\n❌ LỖI XUẤT DỮ LIỆU: {str(e)}")
    
    def run(self):
        """Run the car management interface"""
        while True:
            self.display_menu()
            choice = input("\nChọn chức năng (1-8): ").strip()
            
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
                self.import_cars()
            elif choice == '7':
                self.export_cars()
            elif choice == '8':
                print("\n🏠 Quay lại menu chính...")
                print("─" * 40)
                break
            else:
                print("\n❌ LỰA CHỌN KHÔNG HỢP LỆ!")
                print("   Vui lòng chọn một số từ 1 đến 8.")