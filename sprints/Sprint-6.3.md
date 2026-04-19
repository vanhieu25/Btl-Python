# Sprint-6.3: Employee Performance

**1. Xác định feature:**
- [ ] Define requirements: Báo cáo hiệu suất nhân viên theo KPI (số hợp đồng, xe bán, doanh thu tạo ra)
- [ ] Identify dependencies: Phụ thuộc vào Sprint-5.4 (Employee KPI) và Sprint-3.x (Contract Management)
- [ ] Plan database schema: Sử dụng dữ liệu từ bảng users và contracts để tính toán hiệu suất nhân viên

**2. Database:**
- [ ] Create/migrate tables: Không cần tạo bảng mới, sử dụng bảng users và contracts hiện có
- [ ] Define relationships: Sử dụng relationship giữa users và contracts (created_by) để tính toán hiệu suất
- [ ] Add indexes/constraints: Thêm indexes cho created_by_id field trong bảng contracts để tối ưu truy vấn hiệu suất
- [ ] Test schema integrity: Kiểm tra khả năng truy vấn và tổng hợp hiệu suất nhân viên hiệu quả

**3. Backend Logic:**
- [ ] Create models: Sử dụng models User và Contract hiện có
- [ ] Implement business logic: Implement employee performance calculation logic, ranking system, KPI aggregation
- [ ] Add validation rules: Validate performance metrics accuracy, handle inactive employees, ensure data completeness
- [ ] Handle errors appropriately: Xử lý lỗi truy vấn, đảm bảo performance với large datasets

**4. UI Design:**
- [ ] Create wireframes: Thiết kế employee performance dashboard với biểu đồ so sánh và bảng xếp hạng
- [ ] Implement interface: Tạo performance dashboard với charts hiển thị KPI, employee rankings, comparative metrics
- [ ] Add interactions: Time period filtering, role-based filtering (sales only), export reports, drill-down details
- [ ] Ensure responsiveness: Đảm bảo performance dashboard responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test performance calculation logic với nhiều scenarios, validate KPI accuracy
- [ ] UI acceptance tests: Test chart rendering, ranking display, filtering functionality
- [ ] Integration tests: Test end-to-end flow từ data query → performance calculation → dashboard display
- [ ] Edge case scenarios: Test new employees (zero performance), inactive employees, large teams, performance impact

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: employee performance"
- [ ] Push to remote branch
- [ ] Create pull request if applicable