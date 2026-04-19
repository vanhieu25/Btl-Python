# Sprint-7.1: Warranty Management

**1. Xác định feature:**
- [ ] Define requirements: Quản lý thông tin bảo hành cơ bản (thời hạn, phạm vi, trạng thái) cho từng xe đã bán
- [ ] Identify dependencies: Phụ thuộc vào Sprint-3.x (Contract Management) và Sprint-1.x (Car Management)
- [ ] Plan database schema: Thiết kế bảng warranties với relationship đến contracts và customers

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng warranties trong database với các fields cần thiết
- [ ] Define relationships: Thiết lập foreign key relationships với bảng contracts và customers
- [ ] Add indexes/constraints: Primary key, foreign key constraints, enum cho warranty status
- [ ] Test schema integrity: Kiểm tra relationships hoạt động đúng, đảm bảo data consistency

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy model Warranty với enum WarrantyStatus
- [ ] Implement business logic: CRUD operations cơ bản cho bảo hành, auto-create warranty khi tạo hợp đồng
- [ ] Add validation rules: Validate required fields, warranty duration, status transitions
- [ ] Handle errors appropriately: Xử lý exception và error messages cho warranty management

**4. UI Design:**
- [ ] Create wireframes: Thiết kế layout danh sách bảo hành với filter theo trạng thái
- [ ] Implement interface: Tạo list view hiển thị thông tin bảo hành, status indicators, expiration dates
- [ ] Add interactions: Status filtering, basic table interactions, view warranty details
- [ ] Ensure responsiveness: Đảm bảo giao diện responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test CRUD operations, validation rules, status handling
- [ ] UI acceptance tests: Test hiển thị danh sách bảo hành, status indicators, detail views
- [ ] Integration tests: Test kết nối database → UI, relationships với contracts và customers
- [ ] Edge case scenarios: Test empty data, invalid inputs, status transition violations

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: warranty management"
- [ ] Push to remote branch
- [ ] Create pull request if applicable