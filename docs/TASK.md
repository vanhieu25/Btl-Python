# TASK LIST - MINI SPRINT FEATURES
## PHẦN MỀM QUẢN LÝ ĐẠI LÝ XE HƠI

---

## CẤU TRÚC MINI SPRINT CHO MỖI FEATURE

```
Mini Sprint Flow:
[Xác định feature] → [Database] → [Backend Logic] → [UI Design] → [Testing] → [Git Commit]
```

- **Mỗi feature** bao gồm đầy đủ: Database + Backend + UI + Test
- **Mỗi sprint** hoàn thành 1 feature nhỏ và commit vào git
- **Tập trung** vào từng feature nhỏ để đảm bảo hoàn chỉnh

---

## FEATURES CHÍNH

### 🚗 1. CAR MANAGEMENT
**Mô tả**: Quản lý thông tin xe

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-1.1 | Xác định feature: Car Management | Tạo bảng cars | Models và validators | List view cơ bản | Unit test CRUD | feat: car management initial |
| Sprint-1.2 | Xác định feature: Car CRUD Operations | Relations: cars ↔ contracts | CRUD functions | Add/Edit dialog | Integration test | feat: car CRUD operations |
| Sprint-1.3 | Xác định feature: Car Search & Filter | Indexes cho tìm kiếm | Advanced search logic | Search box + filters | UI acceptance test | feat: car search & filter |
| Sprint-1.4 | Xác định feature: Car Validation | Unique constraints | Business validation | Error messages | Edge case testing | feat: car validation logic |

### 👥 2. CUSTOMER MANAGEMENT  
**Mô tả**: Quản lý thông tin khách hàng

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-2.1 | Xác định feature: Customer Management | Tạo bảng customers | Models và validators | List view cá nhân/doanh nghiệp | Unit test CRUD | feat: customer management initial |
| Sprint-2.2 | Xác định feature: Customer CRUD Operations | Relations: customers ↔ contracts | CRUD functions | Add/Edit dialog | Integration test | feat: customer CRUD operations |
| Sprint-2.3 | Xác định feature: Customer History | History tracking fields | History retrieval logic | Transaction history tab | UI acceptance test | feat: customer history tracking |
| Sprint-2.4 | Xác định feature: Customer VIP Classification | VIP status fields | VIP classification logic | VIP badges in UI | VIP classification test | feat: customer VIP system |

### 📄 3. CONTRACT MANAGEMENT
**Mô tả**: Quản lý hợp đồng bán xe

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-3.1 | Xác định feature: Contract Management | Tạo bảng contracts | Models và validators | List view trạng thái | Unit test CRUD | feat: contract management initial |
| Sprint-3.2 | Xác định feature: Contract Creation | Foreign key relations | Creation workflow | Wizard tạo hợp đồng | Integration test | feat: contract creation workflow |
| Sprint-3.3 | Xác định feature: Contract Calculation | Calculation fields | Price calculation logic | Real-time calculator | Math operation test | feat: contract calculation |
| Sprint-3.4 | Xác định feature: Contract PDF Export | PDF storage | PDF generation logic | Export button + preview | PDF generation test | feat: contract PDF export |

### 📦 4. INVENTORY MANAGEMENT
**Mô tả**: Quản lý tồn kho xe

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-4.1 | Xác định feature: Inventory Tracking | Stock quantity fields | Stock update logic | Inventory dashboard | Unit test updates | feat: inventory tracking |
| Sprint-4.2 | Xác định feature: Stock Alerts | Alert configuration | Low stock detection | Notification system | Alert threshold test | feat: inventory alerts |
| Sprint-4.3 | Xác định feature: Purchase Orders | Purchase order tables | PO creation logic | PO management UI | Order processing test | feat: purchase orders |

### 👨‍💼 5. EMPLOYEE MANAGEMENT
**Mô tả**: Quản lý thông tin nhân viên

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-5.1 | Xác định feature: Employee Management | Tạo bảng users/employees | Models và role system | List view nhân viên | Unit test CRUD | feat: employee management |
| Sprint-5.2 | Xác định feature: Authentication | Password hashing | Login/logout logic | Login screen | Auth integration test | feat: authentication system |
| Sprint-5.3 | Xác định feature: Authorization | Role-based permissions | Permission checking | Role assignment UI | Permission test | feat: authorization system |
| Sprint-5.4 | Xác định feature: Employee KPI | KPI tracking fields | Performance calculation | KPI dashboard | Performance calculation test | feat: employee KPI |

### 📊 6. REPORTING SYSTEM
**Mô tả**: Hệ thống báo cáo thống kê

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-6.1 | Xác định feature: Revenue Reports | Report calculation fields | Revenue aggregation | Revenue chart UI | Report accuracy test | feat: revenue reports |
| Sprint-6.2 | Xác định feature: Top Cars Report | Car sales analytics | Top selling calculation | Top cars chart | Sales calculation test | feat: top cars report |
| Sprint-6.3 | Xác định feature: Employee Performance | Performance metrics | Employee stats | Performance dashboard | Metrics calculation test | feat: employee performance |
| Sprint-6.4 | Xác định feature: VIP Customer Report | VIP criteria fields | VIP identification | VIP customer list | VIP classification test | feat: VIP customer report |

### 🔧 7. WARRANTY MANAGEMENT
**Mô tả**: Quản lý bảo hành

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-7.1 | Xác định feature: Warranty Management | Tạo bảng warranties | Models và validators | Warranty list view | Unit test CRUD | feat: warranty management |
| Sprint-7.2 | Xác định feature: Warranty Claims | Claims tracking | Claim processing | Claim submission UI | Claim workflow test | feat: warranty claims |
| Sprint-7.3 | Xác định feature: Warranty Alerts | Expiration tracking | Expiration detection | Alert notifications | Expiration calculation test | feat: warranty alerts |

### 🎁 8. PROMOTION MANAGEMENT
**Mô tả**: Quản lý khuyến mãi

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-8.1 | Xác định feature: Promotion Management | Tạo bảng promotions | Models và validators | Promotion list UI | Unit test CRUD | feat: promotion management |
| Sprint-8.2 | Xác định feature: Promotion Application | Auto-application logic | Discount calculation | Auto-apply in contracts | Discount calculation test | feat: promotion application |
| Sprint-8.3 | Xác định feature: Promotion Effectiveness | Tracking fields | Effectiveness calculation | Effectiveness reports | ROI calculation test | feat: promotion effectiveness |

### 🎒 9. ACCESSORY MANAGEMENT
**Mô tả**: Quản lý phụ kiện

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-9.1 | Xác định feature: Accessory Catalog | Tạo bảng accessories | Models và inventory | Catalog list UI | Unit test CRUD | feat: accessory catalog |
| Sprint-9.2 | Xác định feature: Combo Pricing | Combo definitions | Pricing logic | Combo selection UI | Price calculation test | feat: combo pricing |
| Sprint-9.3 | Xác định feature: Accessory in Contracts | Relations: accessories ↔ contracts | Add to contract logic | Add accessories dialog | Contract integration test | feat: accessories in contracts |

### 🏭 10. SUPPLIER MANAGEMENT
**Mô tả**: Quản lý nhà cung cấp

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-10.1 | Xác định feature: Supplier Management | Tạo bảng suppliers | Models và rating | Supplier list UI | Unit test CRUD | feat: supplier management |
| Sprint-10.2 | Xác định feature: Purchase Orders | Purchase order system | Order processing | PO creation UI | Order workflow test | feat: purchase orders |
| Sprint-10.3 | Xác định feature: Supplier Rating | Rating fields | Rating calculation | Rating display UI | Rating calculation test | feat: supplier rating |

### 💳 11. INSTALLMENT MANAGEMENT
**Mô tả**: Quản lý trả góp

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-11.1 | Xác định feature: Installment Calculation | Payment schedule | Calculation logic | Payment calculator | Math operation test | feat: installment calculation |
| Sprint-11.2 | Xác định feature: Payment Tracking | Payment tracking | Tracking system | Payment history UI | Tracking accuracy test | feat: payment tracking |
| Sprint-11.3 | Xác định feature: Payment Alerts | Alert triggers | Late payment detection | Alert notifications | Alert threshold test | feat: payment alerts |

### 🛠️ 12. AFTER-SALES SERVICES
**Mô tả**: Dịch vụ hậu mãi

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-12.1 | Xác định feature: Maintenance Scheduling | Schedule tracking | Scheduling logic | Schedule calendar UI | Scheduling test | feat: maintenance scheduling |
| Sprint-12.2 | Xác định feature: Service Requests | Request tracking | Request processing | Service request UI | Request workflow test | feat: service requests |

### 📣 13. MARKETING MANAGEMENT
**Mô tả**: Quản lý marketing

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-13.1 | Xác định feature: Marketing Campaigns | Campaign tracking | Campaign management | Campaign dashboard | Campaign workflow test | feat: marketing campaigns |
| Sprint-13.2 | Xác định feature: Lead Management | Lead tracking | Lead processing | Lead management UI | Lead workflow test | feat: lead management |

### ⚠️ 14. COMPLAINT MANAGEMENT
**Mô tả**: Quản lý khiếu nại

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-14.1 | Xác định feature: Complaint Management | Tạo bảng complaints | Models và workflow | Complaint list UI | Unit test CRUD | feat: complaint management |
| Sprint-14.2 | Xác định feature: Complaint Processing | Assignment logic | Processing workflow | Processing UI | Workflow test | feat: complaint processing |
| Sprint-14.3 | Xác định feature: Resolution Tracking | Resolution tracking | Status updates | Resolution tracking | Resolution workflow test | feat: resolution tracking |

### 🔐 15. SECURITY SYSTEM
**Mô tả**: Hệ thống bảo mật

| Sprint | Công việc | Database | Backend | UI | Test | Git Commit |
|--------|-----------|----------|---------|----|------|------------|
| Sprint-15.1 | Xác định feature: Session Management | Session tracking | Session handling | Session timeout | Security test | feat: session management |
| Sprint-15.2 | Xác định feature: Activity Logging | Audit logs | Logging system | Log viewer UI | Logging test | feat: activity logging |
| Sprint-15.3 | Xác định feature: Data Encryption | Encrypted fields | Encryption logic | Secure data handling | Encryption test | feat: data encryption |

---

## MINI SPRINT TEMPLATE

### Sprint-[XX.X]: [Tên Feature]

**1. Xác định feature:**
- [ ] Define requirements
- [ ] Identify dependencies
- [ ] Plan database schema

**2. Database:**
- [ ] Create/migrate tables
- [ ] Define relationships
- [ ] Add indexes/constraints
- [ ] Test schema integrity

**3. Backend Logic:**
- [ ] Create models
- [ ] Implement business logic
- [ ] Add validation rules
- [ ] Handle errors appropriately

**4. UI Design:**
- [ ] Create wireframes
- [ ] Implement interface
- [ ] Add interactions
- [ ] Ensure responsiveness

**5. Testing:**
- [ ] Unit tests for backend
- [ ] UI acceptance tests
- [ ] Integration tests
- [ ] Edge case scenarios

**6. Git Commit:**
- [ ] Commit with descriptive message
- [ ] Push to remote branch
- [ ] Create pull request if applicable

---

## TỔNG SỐ SPRINT: 48

| Module | Số Sprint | Ghi chú |
|--------|-----------|---------|
| Car Management | 4 | Core feature |
| Customer Management | 4 | Core feature |
| Contract Management | 4 | Core feature |
| Inventory Management | 3 | High priority |
| Employee Management | 4 | Core feature |
| Reporting System | 4 | High priority |
| Warranty Management | 3 | Medium priority |
| Promotion Management | 3 | Medium priority |
| Accessory Management | 3 | Medium priority |
| Supplier Management | 3 | Medium priority |
| Installment Management | 3 | Medium priority |
| After-sales Services | 2 | Low priority |
| Marketing Management | 2 | Low priority |
| Complaint Management | 3 | Medium priority |
| Security System | 3 | High priority |

**Tổng cộng**: 48 mini sprints
**Ước lượng thời gian**: 48-96 ngày làm việc (tùy độ phức tạp mỗi sprint)

---

*File task mini sprint được tạo ngày: 19/04/2026*  
*Phiên bản: 1.0*  
*Người tạo: Miao 🌸*