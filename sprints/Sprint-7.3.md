# Sprint-7.3: Warranty Alerts

**1. Xác định feature:**
- [ ] Define requirements: Cảnh báo bảo hành sắp hết hạn (trước 30 ngày) và theo dõi thời hạn bảo hành tự động
- [ ] Identify dependencies: Phụ thuộc vào Sprint-7.1 (Warranty Management) và Sprint-7.2 (Warranty Claims)
- [ ] Plan database schema: Sử dụng bảng warranties hiện có với warranty_months và end_date fields

**2. Database:**
- [ ] Create/migrate tables: Sử dụng bảng warranties hiện có, đảm bảo end_date được tính toán đúng
- [ ] Define relationships: Giữ nguyên relationships hiện có với contracts và customers
- [ ] Add indexes/constraints: Thêm indexes cho end_date field để tối ưu truy vấn cảnh báo
- [ ] Test schema integrity: Kiểm tra khả năng tính toán và truy vấn thời hạn bảo hành chính xác

**3. Backend Logic:**
- [ ] Create models: Sử dụng model Warranty hiện có với end_date field
- [ ] Implement business logic: Implement warranty expiration detection logic, alert generation system (30 days before expiry)
- [ ] Add validation rules: Validate warranty duration calculation, handle date arithmetic correctly
- [ ] Handle errors appropriately: Xử lý lỗi date calculations, ensure performance with large datasets

**4. UI Design:**
- [ ] Create wireframes: Thiết kế hệ thống notification và alert display trong warranty dashboard
- [ ] Implement interface: Hiển thị cảnh báo bảo hành sắp hết hạn với visual indicators (màu sắc, icons ⏰)
- [ ] Add interactions: Alert acknowledgment, view expiring warranties, configure alert thresholds
- [ ] Ensure responsiveness: Đảm bảo alert system hiển thị đẹp trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test expiration detection logic với nhiều scenarios (30 days, 15 days, expired)
- [ ] UI acceptance tests: Test alert display, visual indicators, notification interactions
- [ ] Integration tests: Test end-to-end flow từ warranty creation → expiration calculation → alert generation
- [ ] Edge case scenarios: Test timezone handling, leap years, multiple expiring warranties, performance impact

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: warranty alerts"
- [ ] Push to remote branch
- [ ] Create pull request if applicable