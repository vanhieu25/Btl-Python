# Sprint-1.3: Car Search & Filter

**1. Xác định feature:**
- [ ] Define requirements: Tìm kiếm nâng cao theo nhiều tiêu chí kết hợp, lọc theo trạng thái (còn hàng/đã bán/sắp về)
- [ ] Identify dependencies: Phụ thuộc vào Sprint-1.2 (Car CRUD Operations)
- [ ] Plan database schema: Thêm indexes cho các trường tìm kiếm thường dùng

**2. Database:**
- [ ] Create/migrate tables: Cập nhật bảng cars nếu cần
- [ ] Define relationships: Sử dụng relationships đã có với contracts
- [ ] Add indexes/constraints: Thêm indexes cho các trường: brand, model, year, status để tối ưu tìm kiếm
- [ ] Test schema integrity: Kiểm tra indexes hoạt động đúng và không ảnh hưởng performance

**3. Backend Logic:**
- [ ] Create models: Cập nhật model Car nếu cần
- [ ] Implement business logic: Implement advanced search logic với multiple criteria combination
- [ ] Add validation rules: Validate search parameters, handle empty queries
- [ ] Handle errors appropriately: Xử lý search timeout, invalid search syntax

**4. UI Design:**
- [ ] Create wireframes: Thiết kế search box và filter controls
- [ ] Implement interface: Tạo search input field và filter dropdowns (trạng thái, hãng xe, năm SX, v.v.)
- [ ] Add interactions: Real-time search suggestions, filter apply/clear buttons
- [ ] Ensure responsiveness: Đảm bảo search/filter responsive trên mobile

**5. Testing:**
- [ ] Unit tests for backend: Test search logic với nhiều criteria kết hợp
- [ ] UI acceptance tests: Test search box interactions, filter selections
- [ ] Integration tests: Test end-to-end search flow từ UI → backend → database
- [ ] Edge case scenarios: Test empty results, special characters in search, performance with large dataset

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: chức năng tìm kiếm và lọc xe nâng cao"
- [ ] Push to remote branch
- [ ] Create pull request if applicable