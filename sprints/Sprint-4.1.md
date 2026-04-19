# Sprint-4.1: Inventory Tracking

**1. Xác định feature:**
- [ ] Define requirements: Theo dõi số lượng tồn kho xe và cập nhật tự động khi có hợp đồng mới
- [ ] Identify dependencies: Phụ thuộc vào Sprint-1.x (Car Management) và Sprint-3.x (Contract Management)
- [ ] Plan database schema: Thiết kế hệ thống tracking tồn kho với stock_quantity field và inventory logs

**2. Database:**
- [ ] Create/migrate tables: Cập nhật bảng cars với stock_quantity field, tạo bảng inventory_logs nếu cần
- [ ] Define relationships: Thiết lập relationship giữa cars và inventory logs
- [ ] Add indexes/constraints: Thêm constraints để đảm bảo stock_quantity >= 0, indexes cho inventory tracking
- [ ] Test schema integrity: Kiểm tra khả năng tracking tồn kho và lịch sử thay đổi

**3. Backend Logic:**
- [ ] Create models: Cập nhật model Car với stock_quantity, tạo model InventoryLog nếu cần
- [ ] Implement business logic: Implement stock update logic tự động khi tạo/hủy hợp đồng
- [ ] Add validation rules: Validate stock quantity không âm, handle out-of-stock scenarios
- [ ] Handle errors appropriately: Xử lý lỗi stock updates, đảm bảo data consistency

**4. UI Design:**
- [ ] Create wireframes: Thiết kế inventory dashboard hiển thị tồn kho theo xe
- [ ] Implement interface: Tạo inventory dashboard với cards hiển thị stock levels, low stock warnings
- [ ] Add interactions: Real-time stock updates, refresh inventory data, view stock history
- [ ] Ensure responsiveness: Đảm bảo dashboard responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test stock update logic, validation rules, edge cases (zero stock, negative scenarios)
- [ ] UI acceptance tests: Test inventory dashboard display, real-time updates, warning indicators
- [ ] Integration tests: Test end-to-end flow từ contract creation → stock update → UI refresh
- [ ] Edge case scenarios: Test concurrent updates, large inventory datasets, race conditions

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: inventory tracking"
- [ ] Push to remote branch
- [ ] Create pull request if applicable