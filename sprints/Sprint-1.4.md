# Sprint-1.4: Car Validation

**1. Xác định feature:**
- [ ] Define requirements: Validate business rules cho thông tin xe (unique constraints, business validation)
- [ ] Identify dependencies: Phụ thuộc vào Sprint-1.3 (Car Search & Filter)
- [ ] Plan database schema: Thêm unique constraints và validation rules vào schema

**2. Database:**
- [ ] Create/migrate tables: Cập nhật bảng cars với unique constraints
- [ ] Define relationships: Giữ nguyên relationships hiện có
- [ ] Add indexes/constraints: Unique constraint cho mã xe, validate giá bán > 0, tồn kho >= 0
- [ ] Test schema integrity: Kiểm tra constraints ngăn chặn invalid data

**3. Backend Logic:**
- [ ] Create models: Cập nhật model Car với validation rules
- [ ] Implement business logic: Implement business validation logic (giá bán phải dương, tồn kho không âm, v.v.)
- [ ] Add validation rules: Custom validators cho các trường đặc biệt
- [ ] Handle errors appropriately: Hiển thị error messages rõ ràng cho từng loại validation failure

**4. UI Design:**
- [ ] Create wireframes: Thiết kế error message display trong form
- [ ] Implement interface: Hiển thị error messages gần các field tương ứng
- [ ] Add interactions: Real-time validation feedback khi user nhập liệu
- [ ] Ensure responsiveness: Đảm bảo error messages hiển thị đẹp trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test tất cả validation rules với valid/invalid inputs
- [ ] UI acceptance tests: Test hiển thị error messages, form behavior khi có lỗi
- [ ] Integration tests: Test end-to-end validation flow từ UI → backend → database
- [ ] Edge case scenarios: Test boundary values, special characters, SQL injection attempts

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: car validation logic"
- [ ] Push to remote branch
- [ ] Create pull request if applicable