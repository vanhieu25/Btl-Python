# Sprint-10.2: Purchase Orders

**1. Xác định feature:**
- [ ] Define requirements: Tạo và quản lý đơn đặt hàng xe/phụ kiện từ nhà cung cấp với theo dõi trạng thái
- [ ] Identify dependencies: Phụ thuộc vào Sprint-10.1 (Supplier Management) và Sprint-4.3 (Purchase Orders - Inventory)
- [ ] Plan database schema: Sử dụng bảng purchase_orders đã có, đảm bảo relationship với suppliers

**2. Database:**
- [ ] Create/migrate tables: Sử dụng bảng purchase_orders hiện có từ Sprint-4.3
- [ ] Define relationships: Giữ nguyên relationship với bảng suppliers
- [ ] Add indexes/constraints: Đảm bảo foreign key constraints hoạt động đúng với supplier_id
- [ ] Test schema integrity: Kiểm tra khả năng tạo và quản lý đơn đặt hàng từ nhà cung cấp

**3. Backend Logic:**
- [ ] Create models: Sử dụng model PurchaseOrder hiện có từ Sprint-4.3
- [ ] Implement business logic: Implement PO creation logic từ supplier management, status workflow management
- [ ] Add validation rules: Validate supplier selection, order items, quantities, and total amounts
- [ ] Handle errors appropriately: Xử lý validation errors, supplier availability, inventory updates

**4. UI Design:**
- [ ] Create wireframes: Thiết kế form tạo đơn đặt hàng từ chi tiết nhà cung cấp
- [ ] Implement interface: Tạo PO creation interface trong supplier detail view, PO management dashboard
- [ ] Add interactions: Supplier pre-selection, item selection, quantity inputs, status updates, total calculation
- [ ] Ensure responsiveness: Đảm bảo PO interface responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test PO creation logic, status management, supplier validation
- [ ] UI acceptance tests: Test PO form interactions, supplier pre-selection, status display
- [ ] Integration tests: Test end-to-end flow từ supplier selection → PO creation → inventory impact
- [ ] Edge case scenarios: Test invalid suppliers, zero quantities, cancelled orders, inventory synchronization

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: purchase orders"
- [ ] Push to remote branch
- [ ] Create pull request if applicable