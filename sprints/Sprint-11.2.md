# Sprint-11.2: Payment Tracking

**1. Xác định feature:**
- [ ] Define requirements: Theo dõi tiến độ trả góp (số tiền còn nợ, số kỳ còn lại, lịch sử thanh toán)
- [ ] Identify dependencies: Phụ thuộc vào Sprint-11.1 (Installment Calculation) và Sprint-3.x (Contract Management)
- [ ] Plan database schema: Thiết kế hệ thống payment tracking với bảng installment_payments và relationship đến contracts

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng installment_payments để lưu trữ lịch sử thanh toán trả góp
- [ ] Define relationships: Thiết lập foreign key relationship giữa installment_payments và contracts
- [ ] Add indexes/constraints: Primary key, foreign key constraints, payment date and amount validation
- [ ] Test schema integrity: Kiểm tra khả năng lưu trữ và truy vấn lịch sử thanh toán chính xác

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy model InstallmentPayment với relationship đến Contract
- [ ] Implement business logic: Implement payment tracking logic, remaining balance calculation, term remaining calculation
- [ ] Add validation rules: Validate payment amounts, dates, ensure no overpayment, handle partial payments
- [ ] Handle errors appropriately: Xử lý validation errors, payment schedule inconsistencies, data integrity issues

**4. UI Design:**
- [ ] Create wireframes: Thiết kế payment tracking dashboard trong chi tiết hợp đồng trả góp
- [ ] Implement interface: Hiển thị payment progress (progress bar), remaining balance, terms remaining, payment history table
- [ ] Add interactions: Record new payments, view payment details, export payment history, payment reminders
- [ ] Ensure responsiveness: Đảm bảo payment tracking interface responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test payment tracking logic với nhiều scenarios, validate balance calculations
- [ ] UI acceptance tests: Test payment progress display, history table, payment recording interactions
- [ ] Integration tests: Test end-to-end flow từ payment recording → balance update → UI refresh
- [ ] Edge case scenarios: Test overpayments, early payments, missed payments, large payment histories

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: payment tracking"
- [ ] Push to remote branch
- [ ] Create pull request if applicable