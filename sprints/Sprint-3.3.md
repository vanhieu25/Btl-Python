# Sprint-3.3: Contract Calculation

**1. Xác định feature:**
- [ ] Define requirements: Tự động tính toán giá trị hợp đồng bao gồm giá xe, phụ kiện, khuyến mãi
- [ ] Identify dependencies: Phụ thuộc vào Sprint-3.2 (Contract Creation), Sprint-8.x (Promotion), Sprint-9.x (Accessory)
- [ ] Plan database schema: Thêm fields để lưu trữ calculation details trong bảng contracts

**2. Database:**
- [ ] Create/migrate tables: Cập nhật bảng contracts với các fields cho calculation (car_price, accessories_price, discount, total_price)
- [ ] Define relationships: Giữ nguyên relationships hiện có, thêm relationship với promotions và accessories nếu cần
- [ ] Add indexes/constraints: Thêm constraints để đảm bảo calculation data integrity
- [ ] Test schema integrity: Kiểm tra khả năng lưu trữ và truy vấn calculation data

**3. Backend Logic:**
- [ ] Create models: Cập nhật model Contract với calculation fields và logic
- [ ] Implement business logic: Implement price calculation logic (base price + accessories - promotions)
- [ ] Add validation rules: Validate calculation inputs, handle promotion applicability, accessory pricing
- [ ] Handle errors appropriately: Xử lý calculation errors, invalid pricing scenarios

**4. UI Design:**
- [ ] Create wireframes: Thiết kế real-time calculator trong contract creation wizard
- [ ] Implement interface: Hiển thị real-time price calculation trong bước xác nhận hợp đồng
- [ ] Add interactions: Real-time updates khi thay đổi phụ kiện/khuyến mãi, calculation breakdown display
- [ ] Ensure responsiveness: Đảm bảo calculator hiển thị đẹp trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test calculation logic với nhiều scenarios (with/without promotions/accessories)
- [ ] UI acceptance tests: Test real-time calculation updates, display accuracy
- [ ] Integration tests: Test end-to-end calculation flow từ input → calculation → storage
- [ ] Edge case scenarios: Test extreme values, multiple promotions, complex accessory combinations

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: contract calculation"
- [ ] Push to remote branch
- [ ] Create pull request if applicable