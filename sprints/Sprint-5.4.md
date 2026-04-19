# Sprint-5.4: Employee KPI

**1. Xác định feature:**
- [ ] Define requirements: Theo dõi KPI nhân viên (số xe bán được, doanh thu tạo ra) và hiển thị dashboard
- [ ] Identify dependencies: Phụ thuộc vào Sprint-5.3 (Authorization), Sprint-3.x (Contract Management)
- [ ] Plan database schema: Thêm fields để tracking KPI metrics trong bảng users hoặc tạo bảng riêng

**2. Database:**
- [ ] Create/migrate tables: Thêm KPI tracking fields vào bảng users (total_contracts, total_revenue) hoặc tạo bảng employee_kpi
- [ ] Define relationships: Sử dụng relationship giữa users và contracts để tính toán KPI
- [ ] Add indexes/constraints: Thêm indexes cho KPI-related fields để tối ưu truy vấn
- [ ] Test schema integrity: Kiểm tra khả năng tính toán và lưu trữ KPI metrics

**3. Backend Logic:**
- [ ] Create models: Cập nhật model User với KPI fields hoặc tạo model EmployeeKPI mới
- [ ] Implement business logic: Implement KPI calculation logic dựa trên hợp đồng đã tạo, real-time updates
- [ ] Add validation rules: Validate KPI calculation accuracy, handle edge cases (cancelled contracts)
- [ ] Handle errors appropriately: Xử lý lỗi calculation, đảm bảo performance với large datasets

**4. UI Design:**
- [ ] Create wireframes: Thiết kế KPI dashboard cho nhân viên và quản trị viên
- [ ] Implement interface: Tạo KPI dashboard với cards hiển thị metrics, charts cho xu hướng
- [ ] Add interactions: View personal KPI vs team average, time period filtering, export KPI reports
- [ ] Ensure responsiveness: Đảm bảo KPI dashboard responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test KPI calculation logic với nhiều scenarios, validate accuracy
- [ ] UI acceptance tests: Test KPI dashboard display, chart rendering, filtering interactions
- [ ] Integration tests: Test end-to-end flow từ contract creation → KPI update → dashboard refresh
- [ ] Edge case scenarios: Test new employees (zero KPI), cancelled contracts impact, performance with large datasets

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: employee KPI"
- [ ] Push to remote branch
- [ ] Create pull request if applicable