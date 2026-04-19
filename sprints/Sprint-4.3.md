# Sprint-4.3: Purchase Orders

**1. Xác định feature:**
- [ ] Define requirements: Quản lý đơn đặt hàng từ nhà cung cấp, theo dõi lịch sử nhập hàng
- [ ] Identify dependencies: Phụ thuộc vào Sprint-4.1 (Inventory Tracking) và Sprint-10.x (Supplier Management)
- [ ] Plan database schema: Thiết kế bảng purchase_orders với relationship đến suppliers và cars

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng purchase_orders với fields cho order details, supplier_id, status
- [ ] Define relationships: Thiết lập foreign key relationships với bảng suppliers và cars
- [ ] Add indexes/constraints: Primary key, foreign key constraints, enum cho trạng thái đơn hàng
- [ ] Test schema integrity: Kiểm tra relationships hoạt động đúng, đảm bảo data consistency

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy model PurchaseOrder với relationship suppliers
- [ ] Implement business logic: Implement PO creation logic, status management, inventory update khi nhận hàng
- [ ] Add validation rules: Validate supplier existence, order quantities, status transitions
- [ ] Handle errors appropriately: Xử lý validation errors, inventory updates, workflow violations

**4. UI Design:**
- [ ] Create wireframes: Thiết kế PO management interface với form tạo đơn và danh sách theo dõi
- [ ] Implement interface: Tạo PO creation form và PO management UI với status tracking
- [ ] Add interactions: Form validation, status updates, inventory sync when receiving goods
- [ ] Ensure responsiveness: Đảm bảo PO interface responsive trên các kích thước màn hình

**5. Testing:**
- [ ] Unit tests for backend: Test PO creation logic, status management, inventory updates
- [ ] UI acceptance tests: Test PO form interactions, status display, inventory synchronization
- [ ] Integration tests: Test end-to-end flow từ PO creation → supplier interaction → inventory update
- [ ] Edge case scenarios: Test invalid suppliers, zero quantities, status transition violations

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: purchase orders"
- [ ] Push to remote branch
- [ ] Create pull request if applicable