# Sprint-10.1: Supplier Management

**1. Xác định feature:**
- [ ] Define requirements: Quản lý thông tin nhà cung cấp cơ bản (tên, địa chỉ, SĐT, email, người liên hệ, đánh giá)
- [ ] Identify dependencies: Không có dependencies ban đầu cho module Supplier
- [ ] Plan database schema: Thiết kế bảng suppliers với các fields cần thiết và hệ thống đánh giá

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng suppliers trong database với các fields cần thiết
- [ ] Define relationships: Chưa có relationships ban đầu
- [ ] Add indexes/constraints: Primary key, required fields validation, rating field constraints (1-5)
- [ ] Test schema integrity: Kiểm tra schema hoạt động đúng với dữ liệu nhà cung cấp đầy đủ

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy model Supplier với các fields cần thiết
- [ ] Implement business logic: CRUD operations cơ bản cho nhà cung cấp
- [ ] Add validation rules: Validate required fields, phone/email format, rating range (1-5)
- [ ] Handle errors appropriately: Xử lý exception và error messages cho supplier management

**4. UI Design:**
- [ ] Create wireframes: Thiết kế layout danh sách nhà cung cấp với hiển thị đánh giá (⭐ ratings)
- [ ] Implement interface: Tạo list view hiển thị thông tin nhà cung cấp, rating stars, contact details
- [ ] Add interactions: Basic table interactions, view supplier details, rating display
- [ ] Ensure responsiveness: Đảm bảo giao diện responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test CRUD operations, validation rules, rating handling
- [ ] UI acceptance tests: Test hiển thị danh sách nhà cung cấp, rating stars, detail views
- [ ] Integration tests: Test kết nối database → UI cho quản lý nhà cung cấp
- [ ] Edge case scenarios: Test empty data, invalid inputs, extreme rating values, duplicate suppliers

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: supplier management"
- [ ] Push to remote branch
- [ ] Create pull request if applicable