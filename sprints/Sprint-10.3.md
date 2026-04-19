# Sprint-10.3: Supplier Rating

**1. Xác định feature:**
- [ ] Define requirements: Đánh giá nhà cung cấp dựa trên chất lượng, thời gian giao hàng, giá cả và tính toán rating tổng hợp
- [ ] Identify dependencies: Phụ thuộc vào Sprint-10.1 (Supplier Management) và Sprint-10.2 (Purchase Orders)
- [ ] Plan database schema: Sử dụng bảng suppliers hiện có với rating field, thêm hệ thống đánh giá chi tiết

**2. Database:**
- [ ] Create/migrate tables: Cập nhật bảng suppliers với rating calculation logic, tạo bảng supplier_ratings nếu cần
- [ ] Define relationships: Thiết lập relationship giữa suppliers và purchase_orders để tính toán rating
- [ ] Add indexes/constraints: Thêm indexes cho rating-related fields để tối ưu truy vấn
- [ ] Test schema integrity: Kiểm tra khả năng tính toán và lưu trữ rating chính xác

**3. Backend Logic:**
- [ ] Create models: Cập nhật model Supplier với rating calculation logic hoặc tạo model SupplierRating mới
- [ ] Implement business logic: Implement rating calculation logic dựa trên purchase order history, quality scores, delivery times
- [ ] Add validation rules: Validate rating inputs, handle missing data, ensure rating accuracy
- [ ] Handle errors appropriately: Xử lý lỗi calculation, đảm bảo performance với large datasets

**4. UI Design:**
- [ ] Create wireframes: Thiết kế hệ thống đánh giá trong chi tiết nhà cung cấp với visual rating display
- [ ] Implement interface: Hiển thị rating tổng hợp và breakdown theo các tiêu chí (chất lượng ⭐, thời gian ⏰, giá cả 💰)
- [ ] Add interactions: Rating input forms, historical rating trends, comparison with other suppliers
- [ ] Ensure responsiveness: Đảm bảo rating interface responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test rating calculation logic với nhiều scenarios, validate accuracy
- [ ] UI acceptance tests: Test rating display, visual indicators, input interactions
- [ ] Integration tests: Test end-to-end flow từ PO completion → rating calculation → supplier update
- [ ] Edge case scenarios: Test new suppliers (no rating), incomplete data, extreme ratings, performance impact

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: supplier rating"
- [ ] Push to remote branch
- [ ] Create pull request if applicable