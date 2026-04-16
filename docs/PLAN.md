# PLAN CHI TIẾT TRIỂN KHAI
**Phần mềm Quản lý Đại Lý Xe Hơi**

---

## TỔNG QUAN

- **Tổng số chức năng**: 15 modules
- **Thời gian dự kiến**: 12 tuần (3 tháng)
- **Team size**: 3 người
- **Tech Stack**: Python 3.10+, PyQt6, SQLite, SQLAlchemy

---

## GIAI ĐOẠN 1: NỀN TẢNG (Tuần 1-2)

### Tuần 1: Thiết lập Project & Database
**Người phụ trách**: Tất cả (cùng làm)

| Ngày | Công việc | Output |
|------|-----------|--------|
| 1 | Setup project structure, Git, virtual env | Repo sẵn sàng |
| 2 | Thiết kế Database Schema (ERD) | File ERD.drawio |
| 3 | Tạo models SQLAlchemy cho 7 bảng chính | Models hoàn chỉnh |
| 4 | Setup database connection, init_db script | SQLite DB hoạt động |
| 5 | Tạo base repository pattern | CRUD base class |
| 6 | Viết unit test cho models | Test coverage >80% |
| 7 | Review & fix bugs | Code reviewed |

**Bảng database cần tạo**:
- `users` (nhân viên, quản trị)
- `cars` (thông tin xe)
- `customers` (khách hàng)
- `contracts` (hợp đồng)
- `inventory` (tồn kho)
- `warranty` (bảo hành)
- `promotions` (khuyến mãi)
- `accessories` (phụ kiện)
- `suppliers` (nhà cung cấp)
- `complaints` (khiếu nại)

### Tuần 2: Giao diện Core & Đăng nhập
**Người phụ trách**: Người 1

| Ngày | Công việc | Output |
|------|-----------|--------|
| 8 | Tạo MainWindow, Sidebar, Navigation | Layout chính |
| 9 | Login dialog, authentication service | Đăng nhập hoạt động |
| 10 | User profile, đổi mật khẩu | Quản lý tài khoản |
| 11 | Session management, timeout | Auto logout sau 30p |
| 12 | Audit logging system | Ghi log mọi thao tác |
| 13 | StyleSheet Notion theme hoàn chỉnh | UI consistent |
| 14 | Demo & review giao diện | Approved |

---

## GIAI ĐOẠN 2: MODULES CỐT LÕI (Tuần 3-7)

### Tuần 3: Quản lý Xe & Tồn kho
**Người phụ trách**: Người 2

| Ngày | Công việc | Output |
|------|-----------|--------|
| 15 | Xe service: CRUD, validation | Service layer |
| 16 | Xe view: bảng, tìm kiếm, filter | GUI hoàn chỉnh |
| 17 | Xe dialog: thêm/sửa form | Dialog Xe |
| 18 | Inventory service, cảnh báo tồn kho | Auto alert |
| 19 | Import xe từ NCC | Nhập kho |
| 20 | Unit test Xe & Inventory | Test passed |
| 21 | Review & demo | Approved |

### Tuần 4: Quản lý Khách hàng
**Người phụ trách**: Người 3

| Ngày | Công việc | Output |
|------|-----------|--------|
| 22 | Customer service: CRUD, phân loại | Service |
| 23 | Customer view: tabs, bảng, search | GUI |
| 24 | Customer detail dialog | Chi tiết KH |
| 25 | Lịch sử giao dịch của KH | History view |
| 26 | Phân loại tự động (VIP/Regular) | Auto classify |
| 27 | Unit test Customer | Test passed |
| 28 | Review & demo | Approved |

### Tuần 5: Quản lý Hợp đồng (Phần 1)
**Người phụ trách**: Người 1

| Ngày | Công việc | Output |
|------|-----------|--------|
| 29 | Contract service: tạo HĐ | Service |
| 30 | Tính toán giá trị HĐ (công thức) | Auto calculate |
| 31 | Contract view: bảng, filter | GUI |
| 32 | Contract create dialog (phức tạp) | Form HĐ |
| 33 | Trạng thái HĐ workflow | State machine |
| 34 | In HĐ PDF (ReportLab) | PDF export |
| 35 | Review & demo | Approved |

### Tuần 6: Quản lý Hợp đồng (Phần 2) & Thanh toán
**Người phụ trách**: Người 2

| Ngày | Công việc | Output |
|------|-----------|--------|
| 36 | Payment service: cọc, trả góp | Payment |
| 37 | Payment history, công nợ | Debt tracking |
| 38 | Contract detail view | Chi tiết HĐ |
| 39 | Gia hạn, chấm dứt HĐ | Extend/cancel |
| 40 | Báo cáo HĐ theo trạng thái | Reports |
| 41 | Unit test Contract & Payment | Test passed |
| 42 | Review & demo | Approved |

### Tuần 7: Quản lý Nhân viên & Phân quyền
**Người phụ trách**: Người 3

| Ngày | Công việc | Output |
|------|-----------|--------|
| 43 | Employee service: CRUD | Service |
| 44 | Role-based access control (RBAC) | Phân quyền |
| 45 | Employee view, KPI dashboard | GUI |
| 46 | KPI calculation: doanh thu, số xe | Auto KPI |
| 47 | Xếp hạng nhân viên | Ranking |
| 48 | Unit test Employee & Auth | Test passed |
| 49 | Review & demo | Approved |

---

## GIAI ĐOẠN 3: MODULES NÂNG CAO (Tuần 8-10)

### Tuần 8: Bảo hành & Bảo dưỡng
**Người phụ trách**: Người 1

| Ngày | Công việc | Output |
|------|-----------|--------|
| 50 | Warranty service: tạo BH, thời hạn | Service |
| 51 | Warranty alert (cảnh báo hết hạn) | Notification |
| 52 | Maintenance schedule | Lịch bảo dưỡng |
| 53 | Maintenance history | Lịch sử BD |
| 54 | Warranty claim processing | Xử lý BH |
| 55 | Unit test Warranty | Test passed |
| 56 | Review & demo | Approved |

### Tuần 9: Khuyến mãi & Phụ kiện
**Người phụ trách**: Người 2

| Ngày | Công việc | Output |
|------|-----------|--------|
| 57 | Promotion service: tạo CTKM | Service |
| 58 | Apply promotion to contract | Auto apply |
| 59 | Promotion effectiveness report | Hiệu quả KM |
| 60 | Accessory catalog | Danh mục PK |
| 61 | Accessory combo, tồn kho PK | Combo PK |
| 62 | Unit test Promotion | Test passed |
| 63 | Review & demo | Approved |

### Tuần 10: Nhà cung cấp & Trả góp
**Người phụ trách**: Người 3

| Ngày | Công việc | Output |
|------|-----------|--------|
| 64 | Supplier service: CRUD, đánh giá | Service |
| 65 | Purchase order from supplier | Đơn đặt hàng |
| 66 | Installment calculation | Tính trả góp |
| 67 | Installment tracking | Theo dõi nợ |
| 68 | Bank integration mock | Ngân hàng |
| 69 | Unit test Supplier & Installment | Test passed |
| 70 | Review & demo | Approved |

---

## GIAI ĐOẠN 4: MODULES PHỤ TRỢ (Tuần 11)

### Tuần 11: Marketing & Khiếu nại
**Người phụ trách**: Người 1 + 2

| Ngày | Công việc | Output | Người |
|------|-----------|--------|-------|
| 71 | Marketing campaign management | Chiến dịch | 1 |
| 72 | Lead management | Lead | 1 |
| 73 | Event management | Sự kiện | 1 |
| 74 | Complaint service: tiếp nhận | Khiếu nại | 2 |
| 75 | Complaint workflow | Xử lý KN | 2 |
| 76 | Customer satisfaction survey | Đánh giá | 2 |
| 77 | Review & demo | Approved | Cả team |

---

## GIAI ĐOẠN 5: BÁO CÁO & HOÀN THIỆN (Tuần 12)

### Tuần 12: Báo cáo & Testing tổng thể
**Người phụ trách**: Tất cả

| Ngày | Công việc | Output |
|------|-----------|--------|
| 78 | Dashboard báo cáo tổng hợp | Dashboard |
| 79 | Báo cáo doanh thu (charts) | Charts |
| 80 | Báo cáo tồn kho, bán hàng | Reports |
| 81 | Integration testing | System test |
| 82 | Performance testing | < 2s response |
| 83 | Bug fixing | Bugs resolved |
| 84 | Final demo & documentation | Release ready |

---

## PHÂN CÔNG CHI TIẾT

### Người 1 (Lead Dev)
- **Tuần 1**: Database, MainWindow, Login
- **Tuần 5-6**: Hợp đồng, Thanh toán
- **Tuần 8**: Bảo hành, Bảo dưỡng
- **Tuần 11**: Marketing
- **Review**: Code review toàn bộ

### Người 2 (Backend Dev)
- **Tuần 3**: Xe, Tồn kho
- **Tuần 6**: Thanh toán, Hợp đồng (tiếp)
- **Tuần 9**: Khuyến mãi, Phụ kiện
- **Tuần 11**: Khiếu nại
- **Review**: Database optimization

### Người 3 (Frontend Dev)
- **Tuần 4**: Khách hàng
- **Tuần 7**: Nhân viên, Phân quyền
- **Tuần 10**: NCC, Trả góp
- **Tuần 12**: Báo cáo, Charts
- **Review**: UI/UX consistency

---

## MILESTONE & DEADLINE

| Milestone | Ngày | Deliverable |
|-----------|------|-------------|
| M1 | Cuối tuần 2 | Database + Login hoạt động |
| M2 | Cuối tuần 7 | 7 modules core hoàn thành |
| M3 | Cuối tuần 10 | 12 modules hoàn thành |
| M4 | Cuối tuần 12 | Full system + Documentation |
| **Release** | Ngày 84 | v1.0 Production |

---

## RISK & MITIGATION

| Rủi ro | Xác suất | Giải pháp |
|--------|----------|-----------|
| Scope creep | Cao | Freeze features sau tuần 7 |
| Performance issue | Trung bình | Optimize DB indexing từ đầu |
| Team member nghỉ | Thấp | Cross-training, backup person |
| Integration bug | Trung bình | Daily integration test |

---

## CÔNG CỤ & WORKFLOW

- **Project Management**: GitHub Projects / Notion
- **Communication**: Discord daily standup
- **Version Control**: Git + GitHub (feature branch workflow)
- **Code Review**: Pull request mandatory
- **Testing**: pytest, pytest-qt
- **Documentation**: Markdown in `/docs`

---

## ĐÁNH GIÁ TIẾN ĐỘ

| Tuần | KPI | Cách đo |
|------|-----|---------|
| 1-2 | Database setup | Unit test pass |
| 3-7 | Core modules | Demo + test coverage |
| 8-10 | Advanced modules | Feature complete |
| 11 | Support modules | Integration test |
| 12 | Release ready | All tests pass |

---

**Ngày bắt đầu**: [Tuần 1]
**Ngày kết thúc dự kiến**: [Tuần 12]
**Người lập plan**: Miao
**Ngày lập**: 16/04/2026