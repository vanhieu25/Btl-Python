# Sprint-8.2: Promotion Application

**1. Xác định feature:**
- [ ] Define requirements: Tự động áp dụng khuyến mãi khi tạo hợp đồng nếu đủ điều kiện (thời gian, loại xe, v.v.)
- [ ] Identify dependencies: Phụ thuộc vào Sprint-8.1 (Promotion Management) và Sprint-3.x (Contract Management)
- [ ] Plan database schema: Sử dụng bảng promotions hiện có, thêm fields để xác định phạm vi áp dụng (brands, models)

**2. Database:**
- [ ] Create/migrate tables: Cập nhật bảng promotions với các fields cho phạm vi áp dụng (applicable_brands, applicable_models)
- [ ] Define relationships: Giữ nguyên cấu trúc hiện tại
- [ ] Add indexes/constraints: Thêm indexes cho applicable_brands field để tối ưu truy vấn áp dụng KM
- [ ] Test schema integrity: Kiểm tra khả năng lưu trữ và truy vấn điều kiện áp dụng khuyến mãi

**3. Backend Logic:**
- [ ] Create models: Cập nhật model Promotion với fields phạm vi áp dụng
- [ ] Implement business logic: Implement auto-application logic khi tạo hợp đồng, validate eligibility conditions
- [ ] Add validation rules: Validate promotion applicability based on car brand/model, time validity, active status
- [ ] Handle errors appropriately: Xử lý trường hợp không có KM phù hợp, multiple eligible promotions

**4. UI Design:**
- [ ] Create wireframes: Thiết kế phần hiển thị và áp dụng khuyến mãi trong contract creation wizard
- [ ] Implement interface: Hiển thị danh sách KM áp dụng được trong bước xác nhận hợp đồng, auto-apply default KM
- [ ] Add interactions: Manual KM selection override, real-time discount calculation, KM details display
- [ ] Ensure responsiveness: Đảm bảo KM application interface responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test auto-application logic với nhiều scenarios (eligible/not eligible, multiple promotions)
- [ ] UI acceptance tests: Test KM display, manual selection, real-time discount updates
- [ ] Integration tests: Test end-to-end flow từ contract creation → KM eligibility check → auto-application
- [ ] Edge case scenarios: Test expired promotions, overlapping conditions, no eligible promotions, performance impact

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: promotion application"
- [ ] Push to remote branch
- [ ] Create pull request if applicable