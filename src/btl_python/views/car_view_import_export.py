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
            filename = filename.strip('"\'')
            
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