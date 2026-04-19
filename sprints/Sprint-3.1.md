# Sprint-3.1: Contract Management

**1. Xác định feature:**
- [ ] Define requirements: Quản lý hợp đồng bán xe cơ bản với thông tin khách hàng, xe, giá trị, trạng thái
- [ ] Identify dependencies: Phụ thuộc vào Sprint-1.x (Car Management) và Sprint-2.x (Customer Management)
- [ ] Plan database schema: Thiết kế bảng contracts với foreign keys đến customers và cars

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng contracts trong database
- [ ] Define relationships: Thiết lập foreign key relationships với bảng customers và cars
- [ ] Add indexes/constraints: Primary key, foreign key constraints, enum cho trạng thái hợp đồng
- [ ] Test schema integrity: Kiểm tra relationships hoạt động đúng, đảm bảo data consistency

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy model Contract với enum ContractStatus
- [ ] Implement business logic: CRUD operations cơ bản cho hợp đồng
- [ ] Add validation rules: Validate required fields, customer-car relationship, status transitions
- [ ] Handle errors appropriately: Xử lý exception và error messages cho contract management

**4. UI Design:**
- [ ] Create wireframes: Thiết kế layout danh sách hợp đồng với filter theo trạng thái
- [ ] Implement interface: Tạo list view hiển thị thông tin hợp đồng, status filters (mới/đã thanh toán/đã giao/đã hủy)
- [ ] Add interactions: Status filtering, basic table interactions, view contract details
- [ ] Ensure responsiveness: Đảm bảo giao diện responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test CRUD operations, validation rules, status handling
- [ ] UI acceptance tests: Test status filtering, hiển thị danh sách hợp đồng, detail views
- [ ] Integration tests: Test kết nối database → UI, relationships với customers và cars
- [ ] Edge case scenarios: Test empty data, invalid inputs, status transition violations

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: contract management initial"
- [ ] Push to remote branch
- [ ] Create pull request if applicable