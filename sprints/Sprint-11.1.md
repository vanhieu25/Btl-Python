# Sprint-11.1: Installment Calculation

**1. Xác định feature:**
- [ ] Define requirements: Tính toán trả góp tự động (số tiền trả hàng tháng, lãi suất, thời hạn) cho khách hàng
- [ ] Identify dependencies: Phụ thuộc vào Sprint-3.x (Contract Management)
- [ ] Plan database schema: Thiết kế hệ thống installment calculation với các fields cần thiết trong hợp đồng

**2. Database:**
- [ ] Create/migrate tables: Cập nhật bảng contracts với các fields cho installment (bank, loan_amount, interest_rate, term_months)
- [ ] Define relationships: Giữ nguyên relationships hiện có với customers và cars
- [ ] Add indexes/constraints: Thêm constraints để đảm bảo installment data integrity (interest_rate >= 0, term > 0)
- [ ] Test schema integrity: Kiểm tra khả năng lưu trữ và truy vấn dữ liệu trả góp chính xác

**3. Backend Logic:**
- [ ] Create models: Cập nhật model Contract với installment fields và calculation logic
- [ ] Implement business logic: Implement installment calculation logic (monthly payment = P * r * (1+r)^n / ((1+r)^n - 1))
- [ ] Add validation rules: Validate loan parameters, handle edge cases (zero interest, short terms), ensure mathematical accuracy
- [ ] Handle errors appropriately: Xử lý calculation errors, invalid parameters, floating point precision issues

**4. UI Design:**
- [ ] Create wireframes: Thiết kế installment calculator trong contract creation wizard
- [ ] Implement interface: Hiển thị installment calculator với inputs (bank, loan amount, interest rate, term) và kết quả monthly payment
- [ ] Add interactions: Real-time calculation updates, parameter validation, amortization schedule preview
- [ ] Ensure responsiveness: Đảm bảo calculator interface responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test installment calculation logic với nhiều scenarios, validate mathematical accuracy
- [ ] UI acceptance tests: Test real-time calculation updates, input validation, result display
- [ ] Integration tests: Test end-to-end flow từ input → calculation → storage in contract
- [ ] Edge case scenarios: Test zero interest rates, very long terms, extreme loan amounts, floating point precision

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: installment calculation"
- [ ] Push to remote branch
- [ ] Create pull request if applicable