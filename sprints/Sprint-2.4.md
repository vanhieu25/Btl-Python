# Sprint-2.4: Customer VIP Classification

**1. Xác định feature:**
- [ ] Define requirements: Phân loại tự động khách hàng VIP dựa trên số lần mua và tổng giá trị giao dịch
- [ ] Identify dependencies: Phụ thuộc vào Sprint-2.3 (Customer History) và Sprint-3.x (Contract Management)
- [ ] Plan database schema: Thêm fields để tracking VIP status, total contracts, total value

**2. Database:**
- [ ] Create/migrate tables: Thêm VIP-related fields vào bảng customers (is_vip, total_contracts, total_value)
- [ ] Define relationships: Sử dụng relationship existing với contracts để tính toán thống kê
- [ ] Add indexes/constraints: Thêm indexes cho VIP-related fields để tối ưu truy vấn phân loại
- [ ] Test schema integrity: Kiểm tra data consistency giữa history và VIP fields

**3. Backend Logic:**
- [ ] Create models: Cập nhật model Customer với VIP fields và classification logic
- [ ] Implement business logic: Implement VIP classification logic dựa trên business rules (số lần mua, tổng giá trị)
- [ ] Add validation rules: Validate VIP classification thresholds, handle edge cases
- [ ] Handle errors appropriately: Xử lý lỗi classification, đảm bảo performance với large datasets

**4. UI Design:**
- [ ] Create wireframes: Thiết kế VIP badges trong danh sách khách hàng và chi tiết khách hàng
- [ ] Implement interface: Hiển thị VIP badges (⭐) trong customer list và customer detail views
- [ ] Add interactions: Hover effects cho VIP badges, filtering VIP customers
- [ ] Ensure responsiveness: Đảm bảo VIP badges hiển thị đẹp trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test VIP classification logic với nhiều scenarios (threshold boundaries, edge cases)
- [ ] UI acceptance tests: Test hiển thị VIP badges, filtering VIP customers, badge interactions
- [ ] Integration tests: Test end-to-end flow từ contract creation → VIP recalculation → UI update
- [ ] Edge case scenarios: Test customers near threshold, large datasets, performance impact

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: customer VIP system"
- [ ] Push to remote branch
- [ ] Create pull request if applicable