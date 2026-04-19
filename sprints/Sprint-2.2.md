# Sprint-2.2: Customer CRUD Operations

**1. Xác định feature:**
- [ ] Define requirements: Thêm, sửa, xóa thông tin khách hàng với validation đầy đủ
- [ ] Identify dependencies: Phụ thuộc vào Sprint-2.1 (Customer Management)
- [ ] Plan database schema: Sử dụng bảng customers đã có, thêm ràng buộc business logic

**2. Database:**
- [ ] Create/migrate tables: Cập nhật bảng customers nếu cần
- [ ] Define relationships: Thiết lập foreign key relationship với bảng contracts
- [ ] Add indexes/constraints: Constraint để đảm bảo data integrity, unique email/phone nếu cần
- [ ] Test schema integrity: Kiểm tra relationships và constraints hoạt động đúng

**3. Backend Logic:**
- [ ] Create models: Cập nhật model Customer với relationship contracts
- [ ] Implement business logic: Implement CRUD functions đầy đủ (create, read, update, delete)
- [ ] Add validation rules: Validate required fields, phone/email format, business rules
- [ ] Handle errors appropriately: Xử lý validation errors và business rule violations

**4. UI Design:**
- [ ] Create wireframes: Thiết kế dialog thêm/sửa khách hàng với form fields khác nhau cho cá nhân/doanh nghiệp
- [ ] Implement interface: Tạo Add/Edit dialog với dynamic form dựa trên loại khách hàng
- [ ] Add interactions: Form validation, customer type switching, submit handlers, cancel buttons
- [ ] Ensure responsiveness: Đảm bảo dialog responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test CRUD functions, validation rules, business logic, customer type handling
- [ ] UI acceptance tests: Test form interactions, validation messages, customer type switching
- [ ] Integration tests: Test end-to-end flow từ UI → backend → database cho cả hai loại KH
- [ ] Edge case scenarios: Test invalid inputs, duplicate emails/phones, mixed customer types

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: customer CRUD operations"
- [ ] Push to remote branch
- [ ] Create pull request if applicable