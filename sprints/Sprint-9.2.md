# Sprint-9.2: Combo Pricing

**1. Xác định feature:**
- [ ] Define requirements: Quản lý combo phụ kiện đi kèm với giá ưu đãi và tính toán giá combo tự động
- [ ] Identify dependencies: Phụ thuộc vào Sprint-9.1 (Accessory Catalog)
- [ ] Plan database schema: Thiết kế hệ thống combo pricing với relationship đến bảng accessories

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng accessory_combos và combo_items để quản lý combo pricing
- [ ] Define relationships: Thiết lập foreign key relationships giữa combo_items và accessories
- [ ] Add indexes/constraints: Primary keys, foreign key constraints, unique constraint cho combo names
- [ ] Test schema integrity: Kiểm tra relationships hoạt động đúng, đảm bảo data consistency

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy models AccessoryCombo và ComboItem với relationships
- [ ] Implement business logic: Implement combo pricing logic, discount calculation, bundle validation
- [ ] Add validation rules: Validate combo items existence, price calculations, duplicate items prevention
- [ ] Handle errors appropriately: Xử lý validation errors, combo calculation errors, missing accessories

**4. UI Design:**
- [ ] Create wireframes: Thiết kế interface tạo và quản lý combo phụ kiện
- [ ] Implement interface: Tạo combo creation form với selection of accessories và combo pricing display
- [ ] Add interactions: Accessory selection with checkboxes/radios, real-time combo price calculation, validation feedback
- [ ] Ensure responsiveness: Đảm bảo combo interface responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test combo pricing logic với nhiều scenarios, validate discount calculations
- [ ] UI acceptance tests: Test combo creation interactions, real-time pricing updates, validation messages
- [ ] Integration tests: Test end-to-end flow từ combo creation → pricing calculation → storage
- [ ] Edge case scenarios: Test empty combos, single item combos, extreme discounts, large combo sizes

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: combo pricing"
- [ ] Push to remote branch
- [ ] Create pull request if applicable