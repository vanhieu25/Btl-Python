# Sprint-1.2: Car CRUD Operations

**1. Xác định feature:**
- [ ] Define requirements: Thêm, sửa, xóa thông tin xe (trừ mã xe không được sửa)
- [ ] Identify dependencies: Phụ thuộc vào Sprint-1.1 (Car Management)
- [ ] Plan database schema: Sử dụng bảng cars đã có, thêm ràng buộc business logic

**2. Database:**
- [ ] Create/migrate tables: Cập nhật bảng cars nếu cần
- [ ] Define relationships: Thiết lập foreign key relationship với bảng contracts
- [ ] Add indexes/constraints: Constraint để ngăn xóa xe có hợp đồng liên quan
- [ ] Test schema integrity: Kiểm tra relationships và constraints hoạt động đúng

**3. Backend Logic:**
- [ ] Create models: Cập nhật model Car với relationship contracts
- [ ] Implement business logic: Implement CRUD functions đầy đủ (create, read, update, delete)
- [ ] Add validation rules: Không cho phép sửa mã xe, không xóa xe có hợp đồng
- [ ] Handle errors appropriately: Xử lý validation errors và business rule violations

**4. UI Design:**
- [ ] Create wireframes: Thiết kế dialog thêm/sửa xe
- [ ] Implement interface: Tạo Add/Edit dialog với form fields đầy đủ
- [ ] Add interactions: Form validation, submit handlers, cancel buttons
- [ ] Ensure responsiveness: Đảm bảo dialog responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test CRUD functions, validation rules, business logic
- [ ] UI acceptance tests: Test form interactions, validation messages
- [ ] Integration tests: Test end-to-end flow từ UI → backend → database
- [ ] Edge case scenarios: Test xóa xe có hợp đồng, sửa mã xe, invalid inputs

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: car CRUD operations"
- [ ] Push to remote branch
- [ ] Create pull request if applicable