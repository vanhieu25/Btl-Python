# Sprint-6.2: Top Cars Report

**1. Xác định feature:**
- [ ] Define requirements: Báo cáo top 10 xe bán chạy nhất với thống kê số lượng và doanh thu
- [ ] Identify dependencies: Phụ thuộc vào Sprint-3.x (Contract Management) và Sprint-1.x (Car Management)
- [ ] Plan database schema: Sử dụng dữ liệu từ bảng contracts và cars để tính toán top xe bán chạy

**2. Database:**
- [ ] Create/migrate tables: Không cần tạo bảng mới, sử dụng bảng contracts và cars hiện có
- [ ] Define relationships: Sử dụng relationship giữa contracts và cars để đếm số lượng bán theo xe
- [ ] Add indexes/constraints: Thêm indexes cho car_id field trong bảng contracts để tối ưu truy vấn top cars
- [ ] Test schema integrity: Kiểm tra khả năng truy vấn và sắp xếp top xe bán chạy hiệu quả

**3. Backend Logic:**
- [ ] Create models: Sử dụng models Contract và Car hiện có
- [ ] Implement business logic: Implement top cars calculation logic, ranking system, sales count aggregation
- [ ] Add validation rules: Validate ranking accuracy, handle ties in rankings, ensure data completeness
- [ ] Handle errors appropriately: Xử lý lỗi truy vấn, đảm bảo performance với large datasets

**4. UI Design:**
- [ ] Create wireframes: Thiết kế top cars report với bảng xếp hạng và visual indicators (medals 🥇🥈🥉)
- [ ] Implement interface: Tạo top cars chart/table với hiển thị ranking, số lượng bán, doanh thu
- [ ] Add interactions: Sort by different criteria, time period filtering, export to Excel/PDF
- [ ] Ensure responsiveness: Đảm bảo top cars report responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test top cars calculation logic với nhiều scenarios, validate ranking accuracy
- [ ] UI acceptance tests: Test ranking display, medal indicators, sorting functionality
- [ ] Integration tests: Test end-to-end flow từ data query → ranking calculation → UI display
- [ ] Edge case scenarios: Test empty data, ties in rankings, large car catalogs, performance impact

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: top cars report"
- [ ] Push to remote branch
- [ ] Create pull request if applicable