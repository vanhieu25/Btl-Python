# Sprint-5.1: Employee Management

**1. Xác định feature:**
- [ ] Define requirements: Quản lý thông tin nhân viên cơ bản (tên, username, email, vai trò, trạng thái)
- [ ] Identify dependencies: Không có dependencies ban đầu cho module Employee
- [ ] Plan database schema: Thiết kế bảng users/employees với các trường cần thiết và phân quyền vai trò

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng users trong database (sử dụng bảng users đã có trong models.py)
- [ ] Define relationships: Chưa có relationships ban đầu
- [ ] Add indexes/constraints: Primary key, unique constraint cho username và email, required fields validation
- [ ] Test schema integrity: Kiểm tra schema hoạt động đúng với các vai trò khác nhau (admin, sales, manager)

**3. Backend Logic:**
- [ ] Create models: Sử dụng SQLAlchemy model User đã có trong models.py với enum UserRole
- [ ] Implement business logic: CRUD operations cơ bản cho nhân viên/quản trị viên
- [ ] Add validation rules: Validate required fields, username/email uniqueness, role validation
- [ ] Handle errors appropriately: Xử lý exception và error messages cho employee management

**4. UI Design:**
- [ ] Create wireframes: Thiết kế layout danh sách nhân viên với hiển thị vai trò và trạng thái
- [ ] Implement interface: Tạo list view hiển thị thông tin nhân viên, role badges, status indicators
- [ ] Add interactions: Basic table interactions, role filtering, status toggling
- [ ] Ensure responsiveness: Đảm bảo giao diện responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test CRUD operations, validation rules, role handling
- [ ] UI acceptance tests: Test hiển thị danh sách nhân viên, role badges, status indicators
- [ ] Integration tests: Test kết nối database → UI cho quản lý nhân viên
- [ ] Edge case scenarios: Test empty data, invalid inputs, duplicate usernames/emails

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: employee management"
- [ ] Push to remote branch
- [ ] Create pull request if applicable