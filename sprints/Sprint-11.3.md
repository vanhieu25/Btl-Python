# Sprint-11.3: Payment Alerts

**1. Xác định feature:**
- [ ] Define requirements: Cảnh báo chậm trả góp và nhắc nhở thanh toán sắp đến hạn
- [ ] Identify dependencies: Phụ thuộc vào Sprint-11.2 (Payment Tracking) và Sprint-11.1 (Installment Calculation)
- [ ] Plan database schema: Sử dụng bảng installment_payments hiện có, thêm hệ thống alert configuration

**2. Database:**
- [ ] Create/migrate tables: Sử dụng bảng installment_payments hiện có, tạo bảng payment_alerts nếu cần
- [ ] Define relationships: Giữ nguyên relationships hiện có với contracts
- [ ] Add indexes/constraints: Thêm indexes cho payment_due_date field để tối ưu truy vấn cảnh báo
- [ ] Test schema integrity: Kiểm tra khả năng phát hiện và theo dõi các khoản thanh toán quá hạn

**3. Backend Logic:**
- [ ] Create models: Sử dụng model InstallmentPayment hiện có, tạo model PaymentAlert nếu cần
- [ ] Implement business logic: Implement late payment detection logic, upcoming payment reminders, alert generation system
- [ ] Add validation rules: Validate alert thresholds, handle timezone differences, ensure accurate date comparisons
- [ ] Handle errors appropriately: Xử lý lỗi date calculations, đảm bảo performance với large datasets

**4. UI Design:**
- [ ] Create wireframes: Thiết kế hệ thống notification và alert display trong dashboard và chi tiết hợp đồng
- [ ] Implement interface: Hiển thị cảnh báo thanh toán quá hạn với visual indicators (màu đỏ 🔴), upcoming payment reminders (màu vàng 🟡)
- [ ] Add interactions: Alert acknowledgment, mark as paid, snooze reminders, configure alert preferences
- [ ] Ensure responsiveness: Đảm bảo alert system hiển thị đẹp trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test late payment detection logic với nhiều scenarios (1 day late, 30 days late, v.v.)
- [ ] UI acceptance tests: Test alert display, visual indicators, acknowledgment interactions
- [ ] Integration tests: Test end-to-end flow từ payment due date → alert generation → UI notification
- [ ] Edge case scenarios: Test timezone handling, weekend/holiday payments, multiple overdue payments, performance impact

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: payment alerts"
- [ ] Push to remote branch
- [ ] Create pull request if applicable