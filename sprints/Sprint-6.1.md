# Sprint-6.1: Revenue Reports

**1. Xác định feature:**
- [ ] Define requirements: Báo cáo doanh thu theo thời gian (ngày/tháng/năm) với biểu đồ trực quan
- [ ] Identify dependencies: Phụ thuộc vào Sprint-3.x (Contract Management) và Sprint-5.x (Employee Management)
- [ ] Plan database schema: Sử dụng dữ liệu từ bảng contracts để tính toán doanh thu theo thời gian

**2. Database:**
- [ ] Create/migrate tables: Không cần tạo bảng mới, sử dụng bảng contracts hiện có
- [ ] Define relationships: Sử dụng relationship giữa contracts và users (created_by) để phân tích theo nhân viên
- [ ] Add indexes/constraints: Thêm indexes cho created_at field trong bảng contracts để tối ưu truy vấn theo thời gian
- [ ] Test schema integrity: Kiểm tra khả năng truy vấn và tổng hợp doanh thu theo các khoảng thời gian khác nhau

**3. Backend Logic:**
- [ ] Create models: Sử dụng models Contract và User hiện có
- [ ] Implement business logic: Implement revenue aggregation logic theo ngày/tháng/năm, time range filtering
- [ ] Add validation rules: Validate date ranges, handle empty date ranges, ensure data accuracy
- [ ] Handle errors appropriately: Xử lý lỗi truy vấn, đảm bảo performance với large datasets

**4. UI Design:**
- [ ] Create wireframes: Thiết kế revenue report dashboard với biểu đồ doanh thu và controls lọc thời gian
- [ ] Implement interface: Tạo revenue chart UI với line/bar charts, time period selectors (hôm nay, tuần này, tháng này, tùy chỉnh)
- [ ] Add interactions: Time range selection, chart type switching, export options, real-time updates
- [ ] Ensure responsiveness: Đảm bảo revenue dashboard responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test revenue calculation logic với nhiều scenarios, validate accuracy
- [ ] UI acceptance tests: Test chart rendering, time range filtering, export functionality
- [ ] Integration tests: Test end-to-end flow từ data query → calculation → chart display
- [ ] Edge case scenarios: Test empty date ranges, large datasets, performance impact, timezone handling

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: revenue reports"
- [ ] Push to remote branch
- [ ] Create pull request if applicable