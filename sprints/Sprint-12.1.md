# Sprint-12.1: Maintenance Scheduling

**1. Xác định feature:**
- [ ] Define requirements: Đặt lịch bảo dưỡng định kỳ cho khách hàng dựa trên km/tháng và nhắc nhở tự động
- [ ] Identify dependencies: Phụ thuộc vào Sprint-2.x (Customer Management) và Sprint-3.x (Contract Management)
- [ ] Plan database schema: Thiết kế bảng maintenance_schedules với relationship đến customers và contracts

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng maintenance_schedules trong database với các fields cần thiết
- [ ] Define relationships: Thiết lập foreign key relationships với bảng customers và contracts
- [ ] Add indexes/constraints: Primary key, foreign key constraints, date and km tracking fields
- [ ] Test schema integrity: Kiểm tra relationships hoạt động đúng, đảm bảo data consistency

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy model MaintenanceSchedule với relationships đến Customer và Contract
- [ ] Implement business logic: Implement maintenance scheduling logic, reminder generation system, km/month based triggers
- [ ] Add validation rules: Validate scheduling parameters, handle date/km conflicts, ensure customer/contract validity
- [ ] Handle errors appropriately: Xử lý validation errors, scheduling conflicts, reminder system errors

**4. UI Design:**
- [ ] Create wireframes: Thiết kế maintenance scheduling interface trong chi tiết khách hàng
- [ ] Implement interface: Tạo maintenance calendar/scheduler với hiển thị lịch bảo dưỡng, reminder settings
- [ ] Add interactions: Schedule creation/editing, reminder preferences, km/month input, calendar view
- [ ] Ensure responsiveness: Đảm bảo scheduling interface responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test scheduling logic với nhiều scenarios, validate reminder generation
- [ ] UI acceptance tests: Test schedule creation interactions, calendar display, reminder settings
- [ ] Integration tests: Test end-to-end flow từ schedule creation → reminder generation → notification
- [ ] Edge case scenarios: Test overlapping schedules, past dates, extreme km values, large customer bases

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: maintenance scheduling"
- [ ] Push to remote branch
- [ ] Create pull request if applicable