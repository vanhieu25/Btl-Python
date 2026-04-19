# Sprint-15.2: Activity Logging

**1. Xác định feature:**
- [ ] Define requirements: Ghi log mọi hoạt động quan trọng của người dùng (tạo/sửa/xóa dữ liệu, đăng nhập/đăng xuất)
- [ ] Identify dependencies: Phụ thuộc vào Sprint-15.1 (Session Management) và Sprint-5.x (Authentication/Authorization)
- [ ] Plan database schema: Thiết kế bảng audit_logs với relationship đến users và tracking các hành động

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng audit_logs trong database với các fields cần thiết
- [ ] Define relationships: Thiết lập foreign key relationship với bảng users
- [ ] Add indexes/constraints: Primary key, foreign key constraints, indexes cho user_id, action_type, và timestamp
- [ ] Test schema integrity: Kiểm tra khả năng lưu trữ và truy vấn log data hiệu quả

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy model AuditLog với relationship đến User
- [ ] Implement business logic: Implement comprehensive logging logic cho mọi hành động quan trọng, log rotation, data retention
- [ ] Add validation rules: Validate log entries completeness, handle sensitive data filtering, ensure log integrity
- [ ] Handle errors appropriately: Xử lý logging failures, disk space issues, performance impact minimization

**4. UI Design:**
- [ ] Create wireframes: Thiết kế log viewer interface với filter theo người dùng, hành động, thời gian
- [ ] Implement interface: Tạo log viewer dashboard với hiển thị chronological logs, action type indicators, user information
- [ ] Add interactions: Time range filtering, user filtering, action type filtering, export log data, search functionality
- [ ] Ensure responsiveness: Đảm bảo log viewer interface responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test logging logic với nhiều scenarios, validate log completeness and accuracy
- [ ] UI acceptance tests: Test log viewer display, filtering functionality, export capabilities
- [ ] Integration tests: Test end-to-end flow từ user action → log creation → log display
- [ ] Edge case scenarios: Test high volume logging, sensitive data handling, log rotation, performance impact

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: activity logging"
- [ ] Push to remote branch
- [ ] Create pull request if applicable