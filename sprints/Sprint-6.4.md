# Sprint-6.4: VIP Customer Report

**1. Xác định feature:**
- [ ] Define requirements: Báo cáo khách hàng VIP theo tổng giá trị mua hàng và xếp hạng theo loại (cá nhân/doanh nghiệp)
- [ ] Identify dependencies: Phụ thuộc vào Sprint-2.4 (Customer VIP Classification) và Sprint-3.x (Contract Management)
- [ ] Plan database schema: Sử dụng dữ liệu từ bảng customers và contracts để xác định và xếp hạng khách hàng VIP

**2. Database:**
- [ ] Create/migrate tables: Không cần tạo bảng mới, sử dụng bảng customers và contracts hiện có
- [ ] Define relationships: Sử dụng relationship giữa customers và contracts để tính toán tổng giá trị mua hàng
- [ ] Add indexes/constraints: Thêm indexes cho customer_id field trong bảng contracts để tối ưu truy vấn VIP customers
- [ ] Test schema integrity: Kiểm tra khả năng truy vấn và xếp hạng khách hàng VIP hiệu quả

**3. Backend Logic:**
- [ ] Create models: Sử dụng models Customer và Contract hiện có
- [ ] Implement business logic: Implement VIP customer identification logic, ranking system, total value calculation
- [ ] Add validation rules: Validate VIP classification accuracy, handle customer type differentiation, ensure data completeness
- [ ] Handle errors appropriately: Xử lý lỗi truy vấn, đảm bảo performance với large datasets

**4. UI Design:**
- [ ] Create wireframes: Thiết kế VIP customer report với bảng xếp hạng và phân loại theo loại khách hàng
- [ ] Implement interface: Tạo VIP customer report với hiển thị ranking, total purchase value, customer type indicators (👤/🏢)
- [ ] Add interactions: Filter by customer type, time period filtering, export to Excel/PDF, view customer details
- [ ] Ensure responsiveness: Đảm bảo VIP customer report responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test VIP identification logic với nhiều scenarios, validate ranking accuracy
- [ ] UI acceptance tests: Test ranking display, customer type indicators, filtering functionality
- [ ] Integration tests: Test end-to-end flow từ data query → VIP identification → report display
- [ ] Edge case scenarios: Test new customers (zero purchases), mixed customer types, large customer bases, performance impact

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: VIP customer report"
- [ ] Push to remote branch
- [ ] Create pull request if applicable