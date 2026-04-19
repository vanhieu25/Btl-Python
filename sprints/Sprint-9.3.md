# Sprint-9.3: Accessory in Contracts

**1. Xác định feature:**
- [ ] Define requirements: Thêm phụ kiện vào hợp đồng với giá tính toán riêng và tích hợp vào tổng giá trị hợp đồng
- [ ] Identify dependencies: Phụ thuộc vào Sprint-9.2 (Combo Pricing), Sprint-9.1 (Accessory Catalog) và Sprint-3.x (Contract Management)
- [ ] Plan database schema: Thiết kế hệ thống relationship giữa contracts và accessories với pricing details

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng contract_accessories để quản lý phụ kiện trong hợp đồng
- [ ] Define relationships: Thiết lập foreign key relationships giữa contract_accessories, contracts và accessories
- [ ] Add indexes/constraints: Primary keys, foreign key constraints, price fields validation
- [ ] Test schema integrity: Kiểm tra khả năng lưu trữ và truy vấn phụ kiện trong hợp đồng

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy model ContractAccessory với relationships đến Contract và Accessory
- [ ] Implement business logic: Implement accessory addition logic to contracts, price calculation integration
- [ ] Add validation rules: Validate accessory availability, price consistency, contract status compatibility
- [ ] Handle errors appropriately: Xử lý validation errors, out-of-stock accessories, contract modification restrictions

**4. UI Design:**
- [ ] Create wireframes: Thiết kế phần thêm phụ kiện trong contract creation wizard
- [ ] Implement interface: Tạo accessory selection interface trong bước xác nhận hợp đồng với combo/single options
- [ ] Add interactions: Accessory selection with checkboxes, combo vs individual selection, real-time price updates
- [ ] Ensure responsiveness: Đảm bảo accessory interface responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test accessory integration logic với nhiều scenarios, validate price calculations
- [ ] UI acceptance tests: Test accessory selection interactions, real-time price updates, combo application
- [ ] Integration tests: Test end-to-end flow từ accessory selection → contract integration → total calculation
- [ ] Edge case scenarios: Test out-of-stock accessories, cancelled contracts, multiple accessories, performance impact

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: accessories in contracts"
- [ ] Push to remote branch
- [ ] Create pull request if applicable