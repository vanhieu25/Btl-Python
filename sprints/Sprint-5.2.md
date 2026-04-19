# Sprint-5.2: Authentication

**1. Xác định feature:**
- [ ] Define requirements: Hệ thống đăng nhập bằng tài khoản/mật khẩu với mã hóa bcrypt
- [ ] Identify dependencies: Phụ thuộc vào Sprint-5.1 (Employee Management)
- [ ] Plan database schema: Sử dụng bảng users đã có với password_hash field

**2. Database:**
- [ ] Create/migrate tables: Sử dụng bảng users hiện có với password_hash field
- [ ] Define relationships: Giữ nguyên cấu trúc hiện tại
- [ ] Add indexes/constraints: Đảm bảo password_hash field đủ dài để lưu trữ bcrypt hash
- [ ] Test schema integrity: Kiểm tra khả năng lưu trữ và truy vấn password hashes

**3. Backend Logic:**
- [ ] Create models: Sử dụng model User hiện có với password_hash field
- [ ] Implement business logic: Implement login/logout logic, password hashing with bcrypt, session management
- [ ] Add validation rules: Validate username/password format, handle authentication failures securely
- [ ] Handle errors appropriately: Xử lý authentication errors, prevent timing attacks, secure error messages

**4. UI Design:**
- [ ] Create wireframes: Thiết kế màn hình đăng nhập với form username/password
- [ ] Implement interface: Tạo login screen với form fields, remember me option, forgot password link
- [ ] Add interactions: Form validation, password visibility toggle, login/logout buttons
- [ ] Ensure responsiveness: Đảm bảo login screen responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test authentication logic, password hashing, session management
- [ ] UI acceptance tests: Test login form interactions, validation messages, successful login flow
- [ ] Integration tests: Test end-to-end authentication flow từ login → session → protected routes
- [ ] Edge case scenarios: Test invalid credentials, empty inputs, SQL injection attempts, brute force protection

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: authentication system"
- [ ] Push to remote branch
- [ ] Create pull request if applicable