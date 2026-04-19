# Sprint-2.1: Customer Management

**1. Xác định feature:**
- [ ] Define requirements: Quản lý thông tin khách hàng cơ bản (họ tên, SĐT, email, loại KH cá nhân/doanh nghiệp)
- [ ] Identify dependencies: Không có dependencies ban đầu cho module Customer
- [ ] Plan database schema: Thiết kế bảng customers với các trường cần thiết và phân loại KH

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng customers trong database
- [ ] Define relationships: Chưa có relationships ban đầu
- [ ] Add indexes/constraints: Primary key, unique constraint cho mã khách hàng, required fields validation
- [ ] Test schema integrity: Kiểm tra schema hoạt động đúng với cả KH cá nhân và doanh nghiệp

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy model Customer với enum CustomerType
- [ ] Implement business logic: CRUD operations cơ bản cho khách hàng
- [ ] Add validation rules: Validate required fields (tên, SĐT, email), validate customer type
- [ ] Handle errors appropriately: Xử lý exception và error messages cho customer management

**4. UI Design:**
- [ ] Create wireframes: Thiết kế layout danh sách khách hàng với tabs cá nhân/doanh nghiệp
- [ ] Implement interface: Tạo list view hiển thị thông tin khách hàng, tabs để chuyển đổi loại KH
- [ ] Add interactions: Tab switching, basic table interactions
- [ ] Ensure responsiveness: Đảm bảo giao diện responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test CRUD operations, validation rules, customer type handling
- [ ] UI acceptance tests: Test tab switching, hiển thị danh sách khách hàng theo loại
- [ ] Integration tests: Test kết nối database → UI cho cả hai loại khách hàng
- [ ] Edge case scenarios: Test empty data, invalid inputs, mixed customer types

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: customer management initial"
- [ ] Push to remote branch
- [ ] Create pull request if applicable