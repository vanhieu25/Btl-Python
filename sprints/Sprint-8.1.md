# Sprint-8.1: Promotion Management

**1. Xác định feature:**
- [ ] Define requirements: Quản lý chương trình khuyến mãi cơ bản (tên, mô tả, thời gian, loại KM, mức giảm giá)
- [ ] Identify dependencies: Không có dependencies ban đầu cho module Promotion
- [ ] Plan database schema: Thiết kế bảng promotions với các fields cần thiết và enum cho loại khuyến mãi

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng promotions trong database với các fields cần thiết
- [ ] Define relationships: Chưa có relationships ban đầu
- [ ] Add indexes/constraints: Primary key, required fields validation, date range constraints
- [ ] Test schema integrity: Kiểm tra schema hoạt động đúng với các loại khuyến mãi khác nhau

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy model Promotion với các fields cần thiết
- [ ] Implement business logic: CRUD operations cơ bản cho chương trình khuyến mãi
- [ ] Add validation rules: Validate required fields, date ranges (start_date <= end_date), discount values
- [ ] Handle errors appropriately: Xử lý exception và error messages cho promotion management

**4. UI Design:**
- [ ] Create wireframes: Thiết kế layout danh sách khuyến mãi với filter theo trạng thái (đang diễn ra/sắp diễn ra/đã kết thúc)
- [ ] Implement interface: Tạo list view hiển thị thông tin khuyến mãi, status indicators, date ranges
- [ ] Add interactions: Status filtering, basic table interactions, view promotion details
- [ ] Ensure responsiveness: Đảm bảo giao diện responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test CRUD operations, validation rules, date range handling
- [ ] UI acceptance tests: Test hiển thị danh sách khuyến mãi, status indicators, detail views
- [ ] Integration tests: Test kết nối database → UI cho quản lý khuyến mãi
- [ ] Edge case scenarios: Test empty data, invalid inputs, overlapping date ranges, extreme discount values

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: promotion management"
- [ ] Push to remote branch
- [ ] Create pull request if applicable