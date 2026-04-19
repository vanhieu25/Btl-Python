# Sprint-7.2: Warranty Claims

**1. Xác định feature:**
- [ ] Define requirements: Quản lý yêu cầu bảo hành (ngày đến, nội dung sửa chữa, chi phí) với phân loại miễn phí/tính phí
- [ ] Identify dependencies: Phụ thuộc vào Sprint-7.1 (Warranty Management)
- [ ] Plan database schema: Thiết kế bảng warranty_claims với relationship đến warranties

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng warranty_claims trong database với các fields cần thiết
- [ ] Define relationships: Thiết lập foreign key relationship với bảng warranties
- [ ] Add indexes/constraints: Primary key, foreign key constraints, boolean field cho is_free
- [ ] Test schema integrity: Kiểm tra relationships hoạt động đúng, đảm bảo data consistency

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy model WarrantyClaim với relationship warranty
- [ ] Implement business logic: Implement claim processing logic, cost calculation, free vs paid handling
- [ ] Add validation rules: Validate claim details, repair costs, warranty validity period
- [ ] Handle errors appropriately: Xử lý validation errors, expired warranty scenarios, cost calculation errors

**4. UI Design:**
- [ ] Create wireframes: Thiết kế form yêu cầu bảo hành và danh sách claims theo warranty
- [ ] Implement interface: Tạo claim submission form và claim list view trong chi tiết bảo hành
- [ ] Add interactions: Form validation, cost calculation display, free/paid toggle, claim status updates
- [ ] Ensure responsiveness: Đảm bảo claim interface responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test claim processing logic, cost calculation, free/paid handling
- [ ] UI acceptance tests: Test claim form interactions, validation messages, cost display
- [ ] Integration tests: Test end-to-end flow từ claim submission → processing → warranty update
- [ ] Edge case scenarios: Test expired warranties, invalid claims, zero-cost repairs, large claim volumes

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: warranty claims"
- [ ] Push to remote branch
- [ ] Create pull request if applicable