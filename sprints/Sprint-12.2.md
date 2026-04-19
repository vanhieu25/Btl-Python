# Sprint-12.2: Service Requests

**1. Xác định feature:**
- [ ] Define requirements: Quản lý yêu cầu dịch vụ cứu hộ và các dịch vụ hậu mãi khác từ khách hàng
- [ ] Identify dependencies: Phụ thuộc vào Sprint-12.1 (Maintenance Scheduling) và Sprint-2.x (Customer Management)
- [ ] Plan database schema: Thiết kế bảng service_requests với relationship đến customers và loại dịch vụ

**2. Database:**
- [ ] Create/migrate tables: Tạo bảng service_requests trong database với các fields cần thiết
- [ ] Define relationships: Thiết lập foreign key relationship với bảng customers
- [ ] Add indexes/constraints: Primary key, foreign key constraints, enum cho loại dịch vụ (cứu hộ, bảo dưỡng, v.v.)
- [ ] Test schema integrity: Kiểm tra relationships hoạt động đúng, đảm bảo data consistency

**3. Backend Logic:**
- [ ] Create models: Tạo SQLAlchemy model ServiceRequest với relationship đến Customer
- [ ] Implement business logic: Implement service request processing logic, priority handling, status management
- [ ] Add validation rules: Validate service request details, handle emergency vs normal requests, ensure customer validity
- [ ] Handle errors appropriately: Xử lý validation errors, priority conflicts, processing workflow errors

**4. UI Design:**
- [ ] Create wireframes: Thiết kế form yêu cầu dịch vụ và dashboard quản lý yêu cầu
- [ ] Implement interface: Tạo service request form với loại dịch vụ selection, priority indicators, và request details
- [ ] Add interactions: Service type selection, priority auto-detection, real-time status updates, customer contact info pre-fill
- [ ] Ensure responsiveness: Đảm bảo service request interface responsive trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test service request processing logic với nhiều scenarios, validate priority handling
- [ ] UI acceptance tests: Test request form interactions, priority indicators, status display
- [ ] Integration tests: Test end-to-end flow từ request submission → processing → status updates
- [ ] Edge case scenarios: Test emergency requests, invalid customer data, high volume requests, system performance

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: service requests"
- [ ] Push to remote branch
- [ ] Create pull request if applicable