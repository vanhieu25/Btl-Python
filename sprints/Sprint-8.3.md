# Sprint-8.3: Promotion Effectiveness

**1. Xác định feature:**
- [ ] Define requirements: Theo dõi hiệu quả khuyến mãi (số xe bán được với KM, doanh thu từ KM) và báo cáo thống kê
- [ ] Identify dependencies: Phụ thuộc vào Sprint-8.2 (Promotion Application) và Sprint-3.x (Contract Management)
- [ ] Plan database schema: Sử dụng dữ liệu từ bảng promotions và contracts để tính toán hiệu quả KM

**2. Database:**
- [ ] Create/migrate tables: Không cần tạo bảng mới, sử dụng bảng promotions và contracts hiện có
- [ ] Define relationships: Sử dụng relationship giữa contracts và promotions thông qua discount fields
- [ ] Add indexes/constraints: Thêm indexes cho promotion-related fields trong bảng contracts để tối ưu truy vấn
- [ ] Test schema integrity: Kiểm tra khả năng truy vấn và tổng hợp dữ liệu hiệu quả khuyến mãi

**3. Backend Logic:**
- [ ] Create models: Sử dụng models Promotion và Contract hiện có
- [ ] Implement business logic: Implement effectiveness calculation logic, ROI analysis, sales impact metrics
- [ ] Add validation rules: Validate effectiveness calculations, handle edge cases (cancelled contracts with KM)
- [ ] Handle errors appropriately: Xử lý lỗi calculation, đảm bảo performance với large datasets

**4. UI Design:**
- [ ] Create wireframes: Thiết kế promotion effectiveness dashboard với biểu đồ và metrics
- [ ] Implement interface: Tạo effectiveness report với hiển thị số xe bán, doanh thu từ KM, ROI metrics
- [ ] Add interactions: Time period filtering, promotion comparison, export reports, detailed breakdown views
- [ ] Ensure responsiveness: Đảm bảo effectiveness dashboard responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test effectiveness calculation logic với nhiều scenarios, validate accuracy
- [ ] UI acceptance tests: Test dashboard display, chart rendering, filtering functionality
- [ ] Integration tests: Test end-to-end flow từ data query → effectiveness calculation → report display
- [ ] Edge case scenarios: Test new promotions (zero effectiveness), cancelled contracts impact, large datasets, performance impact

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: promotion effectiveness"
- [ ] Push to remote branch
- [ ] Create pull request if applicable