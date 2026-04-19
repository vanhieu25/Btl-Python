# Sprint-3.2: Contract Creation

**1. Xác định feature:**
- [ ] Define requirements: Tạo hợp đồng bán xe thông qua wizard 3 bước (chọn xe → chọn KH → xác nhận)
- [ ] Identify dependencies: Phụ thuộc vào Sprint-3.1 (Contract Management), Sprint-1.x và Sprint-2.x
- [ ] Plan database schema: Sử dụng bảng contracts đã có, đảm bảo foreign key integrity

**2. Database:**
- [ ] Create/migrate tables: Cập nhật bảng contracts nếu cần thêm fields cho creation workflow
- [ ] Define relationships: Giữ nguyên relationships với customers và cars
- [ ] Add indexes/constraints: Thêm constraints để đảm bảo contract creation integrity
- [ ] Test schema integrity: Kiểm tra khả năng tạo hợp đồng mới với đầy đủ relationships

**3. Backend Logic:**
- [ ] Create models: Cập nhật model Contract nếu cần
- [ ] Implement business logic: Implement contract creation workflow, auto-generate contract code, validation logic
- [ ] Add validation rules: Validate car availability, customer existence, required fields
- [ ] Handle errors appropriately: Xử lý validation errors, stock validation, workflow interruptions

**4. UI Design:**
- [ ] Create wireframes: Thiết kế wizard 3 bước với progress indicator
- [ ] Implement interface: Tạo contract creation wizard với 3 steps (chọn xe, chọn KH, xác nhận)
- [ ] Add interactions: Step navigation, form validation, real-time preview, cancel/confirm buttons
- [ ] Ensure responsiveness: Đảm bảo wizard responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test contract creation logic, validation rules, auto-generation
- [ ] UI acceptance tests: Test wizard navigation, form interactions, validation messages
- [ ] Integration tests: Test end-to-end contract creation flow từ wizard → database
- [ ] Edge case scenarios: Test out-of-stock cars, invalid customers, workflow interruptions

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: contract creation workflow"
- [ ] Push to remote branch
- [ ] Create pull request if applicable