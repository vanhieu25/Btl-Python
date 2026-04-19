# Sprint-5.3: Authorization

**1. Xác định feature:**
- [ ] Define requirements: Hệ thống phân quyền dựa trên vai trò (admin, sales, manager) với nguyên tắc least privilege
- [ ] Identify dependencies: Phụ thuộc vào Sprint-5.2 (Authentication) và Sprint-5.1 (Employee Management)
- [ ] Plan database schema: Sử dụng bảng users đã có với role field và enum UserRole

**2. Database:**
- [ ] Create/migrate tables: Sử dụng bảng users hiện có với role field
- [ ] Define relationships: Giữ nguyên cấu trúc hiện tại
- [ ] Add indexes/constraints: Đảm bảo role field sử dụng enum UserRole đúng
- [ ] Test schema integrity: Kiểm tra khả năng query và filter theo roles

**3. Backend Logic:**
- [ ] Create models: Sử dụng model User hiện có với role field và enum UserRole
- [ ] Implement business logic: Implement role-based authorization logic, permission checking middleware
- [ ] Add validation rules: Validate user permissions trước khi thực hiện hành động, handle unauthorized access
- [ ] Handle errors appropriately: Xử lý unauthorized access errors, redirect to appropriate pages

**4. UI Design:**
- [ ] Create wireframes: Thiết kế role assignment interface trong quản lý nhân viên
- [ ] Implement interface: Hiển thị role-specific UI elements, hide/show features based on permissions
- [ ] Add interactions: Role assignment dropdowns, permission-based button visibility, access denied messages
- [ ] Ensure responsiveness: Đảm bảo authorization UI responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test authorization logic với các vai trò khác nhau, permission validation
- [ ] UI acceptance tests: Test role-based UI visibility, permission-based interactions
- [ ] Integration tests: Test end-to-end authorization flow từ login → role assignment → feature access
- [ ] Edge case scenarios: Test unauthorized access attempts, role escalation prevention, admin override scenarios

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: authorization system"
- [ ] Push to remote branch
- [ ] Create pull request if applicable