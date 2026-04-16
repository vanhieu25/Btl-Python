# DANH SÁCH TASK - Quản lý Đại Lý Xe Hơi

> **Format**: `[STATUS] TASK-ID - Mô tả | Assignee | Due Date`
> 
> **Status**: 🔴 TODO / 🟡 IN PROGRESS / 🟢 DONE / ⚪ BACKLOG

---

## 📊 TỔNG KẾT TIẾN ĐỘ

| Giai đoạn | Tổng | 🟢 Done | 🟡 In Progress | 🔴 TODO | Tiến độ |
|-----------|------|---------|---------------|---------|---------|
| **1. Nền tảng** | 20 | 10 | 0 | 10 | **50%** |
| **2. Core** | 45 | 0 | 0 | 45 | **0%** |
| **3. Nâng cao** | 25 | 0 | 0 | 25 | **0%** |
| **4. Phụ trợ** | 11 | 0 | 0 | 11 | **0%** |
| **5. Hoàn thiện** | 12 | 0 | 0 | 12 | **0%** |
| **TỔNG** | **113** | **10** | **0** | **103** | **8.8%** |

---

## 📌 GIAI ĐOẠN 1: NỀN TẢNG (Tuần 1-2) - 50%

### ✅ Module: Database & Models - COMPLETED
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| DB-001 | Thiết kế ERD | Vẽ sơ đồ quan hệ thực thể đầy đủ 10 bảng | Tất cả | Tuần 1 - Thứ 2 | 🟢 DONE |
| DB-002 | Tạo models User | Model User với bcrypt password | Người 1 | Tuần 1 - Thứ 3 | 🟢 DONE |
| DB-003 | Tạo models Car | Model Car đầy đủ thông tin xe | Người 1 | Tuần 1 - Thứ 3 | 🟢 DONE |
| DB-004 | Tạo models Customer | Model Customer với phân loại | Người 1 | Tuần 1 - Thứ 3 | 🟢 DONE |
| DB-005 | Tạo models Contract | Model Contract liên kết Car-Customer | Người 1 | Tuần 1 - Thứ 4 | 🟢 DONE |
| DB-006 | Tạo models Warranty | Model Warranty cho bảo hành | Người 1 | Tuần 1 - Thứ 4 | 🟢 DONE |
| DB-007 | Tạo models Promotion | Model Promotion cho khuyến mãi | Người 1 | Tuần 1 - Thứ 4 | 🟢 DONE |
| DB-008 | Tạo models còn lại | Inventory, Supplier, Complaint, Accessory | Người 1 | Tuần 1 - Thứ 5 | 🟢 DONE |
| DB-009 | Database connection | Setup SQLAlchemy engine, session | Người 1 | Tuần 1 - Thứ 5 | 🟢 DONE |
| DB-010 | init_db script | Script khởi tạo database + sample data | Người 1 | Tuần 1 - Thứ 6 | 🟢 DONE |
| DB-011 | Unit test models | pytest cho tất cả models | Người 1 | Tuần 1 - Thứ 7 | 🔴 TODO |

**Files đã tạo:**
- `src/btl_python/database/connection.py` - Database connection
- `src/btl_python/models.py` - 10 SQLAlchemy models
- `src/btl_python/database/init_db.py` - Khởi tạo DB với sample data

### 🔴 Module: Authentication & Core UI - PENDING
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| AUTH-001 | Login dialog UI | PyQt6 dialog đăng nhập | Người 2 | Tuần 2 - Thứ 2 | 🔴 TODO |
| AUTH-002 | Auth service | Xác thực với bcrypt | Người 2 | Tuần 2 - Thứ 3 | 🔴 TODO |
| AUTH-003 | Session management | Timeout 30 phút | Người 2 | Tuần 2 - Thứ 4 | 🔴 TODO |
| AUTH-004 | MainWindow layout | Sidebar + Content area | Người 2 | Tuần 2 - Thứ 4 | 🔴 TODO |
| AUTH-005 | Navigation system | Chuyển đổi giữa các view | Người 2 | Tuần 2 - Thứ 5 | 🔴 TODO |
| AUTH-006 | User profile | Xem/sửa thông tin cá nhân | Người 2 | Tuần 2 - Thứ 5 | 🔴 TODO |
| AUTH-007 | Audit logging | Ghi log mọi thao tác | Người 2 | Tuần 2 - Thứ 6 | 🔴 TODO |
| AUTH-008 | Notion theme QSS | StyleSheet hoàn chỉnh | Người 2 | Tuần 2 - Thứ 6 | 🔴 TODO |
| AUTH-009 | Demo & Review | Demo toàn bộ foundation | Tất cả | Tuần 2 - Thứ 7 | 🔴 TODO |

---

## 📌 GIAI ĐOẠN 2: MODULES CỐT LÕI (Tuần 3-7) - 0%

### Module: Quản lý Xe (Car Management)
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| CAR-001 | Car service layer | CRUD operations, validation | Người 2 | Tuần 3 - Thứ 2 | 🔴 TODO |
| CAR-002 | Car list view | Bảng xe với search/filter | Người 2 | Tuần 3 - Thứ 3 | 🔴 TODO |
| CAR-003 | Add car dialog | Form thêm xe mới | Người 2 | Tuần 3 - Thứ 3 | 🔴 TODO |
| CAR-004 | Edit car dialog | Form sửa thông tin xe | Người 2 | Tuần 3 - Thứ 4 | 🔴 TODO |
| CAR-005 | Inventory alert | Cảnh báo tồn kho thấp | Người 2 | Tuần 3 - Thứ 4 | 🔴 TODO |
| CAR-006 | Import from supplier | Nhập xe từ NCC | Người 2 | Tuần 3 - Thứ 5 | 🔴 TODO |
| CAR-007 | Car detail view | Xem chi tiết xe | Người 2 | Tuần 3 - Thứ 5 | 🔴 TODO |
| CAR-008 | Unit test | pytest coverage >80% | Người 2 | Tuần 3 - Thứ 6 | 🔴 TODO |
| CAR-009 | Demo & Review | Demo module Xe | Người 2 | Tuần 3 - Thứ 7 | 🔴 TODO |

### Module: Quản lý Khách hàng (Customer Management)
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| CUS-001 | Customer service | CRUD, phân loại | Người 3 | Tuần 4 - Thứ 2 | 🔴 TODO |
| CUS-002 | Customer list view | Tabs Cá nhân/Doanh nghiệp | Người 3 | Tuần 4 - Thứ 3 | 🔴 TODO |
| CUS-003 | Add customer dialog | Form thêm KH | Người 3 | Tuần 4 - Thứ 3 | 🔴 TODO |
| CUS-004 | Customer detail | Xem chi tiết + lịch sử | Người 3 | Tuần 4 - Thứ 4 | 🔴 TODO |
| CUS-005 | Auto classification | VIP/Regular auto detect | Người 3 | Tuần 4 - Thứ 4 | 🔴 TODO |
| CUS-006 | Search & Filter | Tìm theo tên, SĐT, email | Người 3 | Tuần 4 - Thứ 5 | 🔴 TODO |
| CUS-007 | Customer statistics | Tổng giá trị mua hàng | Người 3 | Tuần 4 - Thứ 5 | 🔴 TODO |
| CUS-008 | Unit test | pytest | Người 3 | Tuần 4 - Thứ 6 | 🔴 TODO |
| CUS-009 | Demo & Review | Demo module KH | Người 3 | Tuần 4 - Thứ 7 | 🔴 TODO |

### Module: Quản lý Hợp đồng (Contract Management) - Phần 1
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| CONT-001 | Contract service | Tạo HĐ, tính giá trị | Người 1 | Tuần 5 - Thứ 2 | 🔴 TODO |
| CONT-002 | Price calculation | Công thức tính giá | Người 1 | Tuần 5 - Thứ 3 | 🔴 TODO |
| CONT-003 | Contract list view | Bảng HĐ với filter | Người 1 | Tuần 5 - Thứ 3 | 🔴 TODO |
| CONT-004 | Create contract dialog | Form tạo HĐ phức tạp | Người 1 | Tuần 5 - Thứ 4 | 🔴 TODO |
| CONT-005 | Contract status workflow | Mới → Đã TT → Đã giao | Người 1 | Tuần 5 - Thứ 5 | 🔴 TODO |
| CONT-006 | PDF export | In HĐ với ReportLab | Người 1 | Tuần 5 - Thứ 5 | 🔴 TODO |
| CONT-007 | Contract preview | Xem trước khi lưu | Người 1 | Tuần 5 - Thứ 6 | 🔴 TODO |
| CONT-008 | Unit test | pytest | Người 1 | Tuần 5 - Thứ 6 | 🔴 TODO |
| CONT-009 | Demo & Review | Demo tạo HĐ | Người 1 | Tuần 5 - Thứ 7 | 🔴 TODO |

### Module: Thanh toán & Hợp đồng (Phần 2)
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| PAY-001 | Payment service | Tiền cọc, thanh toán | Người 2 | Tuần 6 - Thứ 2 | 🔴 TODO |
| PAY-002 | Payment history | Lịch sử thanh toán | Người 2 | Tuần 6 - Thứ 3 | 🔴 TODO |
| PAY-003 | Debt tracking | Công nợ khách hàng | Người 2 | Tuần 6 - Thứ 3 | 🔴 TODO |
| PAY-004 | Contract detail view | Chi tiết HĐ đầy đủ | Người 2 | Tuần 6 - Thứ 4 | 🔴 TODO |
| PAY-005 | Contract extension | Gia hạn HĐ | Người 2 | Tuần 6 - Thứ 4 | 🔴 TODO |
| PAY-006 | Contract cancellation | Hủy HĐ | Người 2 | Tuần 6 - Thứ 5 | 🔴 TODO |
| PAY-007 | Contract reports | Báo cáo HĐ theo status | Người 2 | Tuần 6 - Thứ 5 | 🔴 TODO |
| PAY-008 | Unit test | pytest | Người 2 | Tuần 6 - Thứ 6 | 🔴 TODO |
| PAY-009 | Demo & Review | Demo thanh toán | Người 2 | Tuần 6 - Thứ 7 | 🔴 TODO |

### Module: Quản lý Nhân viên (Employee Management)
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| EMP-001 | Employee service | CRUD nhân viên | Người 3 | Tuần 7 - Thứ 2 | 🔴 TODO |
| EMP-002 | RBAC system | Phân quyền chi tiết | Người 3 | Tuần 7 - Thứ 3 | 🔴 TODO |
| EMP-003 | Employee list view | Bảng + phân quyền | Người 3 | Tuần 7 - Thứ 3 | 🔴 TODO |
| EMP-004 | KPI calculation | Doanh thu, số xe bán | Người 3 | Tuần 7 - Thứ 4 | 🔴 TODO |
| EMP-005 | KPI dashboard | Biểu đồ KPI | Người 3 | Tuần 7 - Thứ 4 | 🔴 TODO |
| EMP-006 | Employee ranking | Xếp hạng nhân viên | Người 3 | Tuần 7 - Thứ 5 | 🔴 TODO |
| EMP-007 | My profile view | Nhân viên xem thông tin mình | Người 3 | Tuần 7 - Thứ 5 | 🔴 TODO |
| EMP-008 | Unit test | pytest | Người 3 | Tuần 7 - Thứ 6 | 🔴 TODO |
| EMP-009 | Demo & Review | Demo nhân viên | Người 3 | Tuần 7 - Thứ 7 | 🔴 TODO |

---

## 📌 GIAI ĐOẠN 3: MODULES NÂNG CAO (Tuần 8-10) - 0%

### Module: Bảo hành (Warranty)
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| WAR-001 | Warranty service | Tạo BH, thời hạn | Người 1 | Tuần 8 - Thứ 2 | 🔴 TODO |
| WAR-002 | Warranty alert | Cảnh báo sắp hết hạn | Người 1 | Tuần 8 - Thứ 3 | 🔴 TODO |
| WAR-003 | Warranty claim | Tiếp nhận yêu cầu BH | Người 1 | Tuần 8 - Thứ 3 | 🔴 TODO |
| WAR-004 | Maintenance schedule | Lịch bảo dưỡng | Người 1 | Tuần 8 - Thứ 4 | 🔴 TODO |
| WAR-005 | Maintenance history | Lịch sử BD | Người 1 | Tuần 8 - Thứ 4 | 🔴 TODO |
| WAR-006 | Warranty cost report | Chi phí BH | Người 1 | Tuần 8 - Thứ 5 | 🔴 TODO |
| WAR-007 | Unit test | pytest | Người 1 | Tuần 8 - Thứ 6 | 🔴 TODO |
| WAR-008 | Demo & Review | Demo BH | Người 1 | Tuần 8 - Thứ 7 | 🔴 TODO |

### Module: Khuyến mãi & Phụ kiện (Promotion & Accessory)
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| PROMO-001 | Promotion service | Tạo CTKM | Người 2 | Tuần 9 - Thứ 2 | 🔴 TODO |
| PROMO-002 | Promotion types | Giảm giá, tặng PK, trả góp | Người 2 | Tuần 9 - Thứ 3 | 🔴 TODO |
| PROMO-003 | Apply promotion | Auto apply khi tạo HĐ | Người 2 | Tuần 9 - Thứ 3 | 🔴 TODO |
| PROMO-004 | Promotion report | Hiệu quả CTKM | Người 2 | Tuần 9 - Thứ 4 | 🔴 TODO |
| ACC-001 | Accessory catalog | Danh mục PK | Người 2 | Tuần 9 - Thứ 4 | 🔴 TODO |
| ACC-002 | Accessory combo | Combo PK ưu đãi | Người 2 | Tuần 9 - Thứ 5 | 🔴 TODO |
| ACC-003 | Accessory inventory | Tồn kho PK | Người 2 | Tuần 9 - Thứ 5 | 🔴 TODO |
| PROMO-005 | Unit test | pytest | Người 2 | Tuần 9 - Thứ 6 | 🔴 TODO |
| PROMO-006 | Demo & Review | Demo KM | Người 2 | Tuần 9 - Thứ 7 | 🔴 TODO |

### Module: Nhà cung cấp & Trả góp (Supplier & Installment)
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| SUP-001 | Supplier service | CRUD NCC | Người 3 | Tuần 10 - Thứ 2 | 🔴 TODO |
| SUP-002 | Supplier evaluation | Đánh giá NCC | Người 3 | Tuần 10 - Thứ 3 | 🔴 TODO |
| SUP-003 | Purchase order | Đơn đặt hàng | Người 3 | Tuần 10 - Thứ 3 | 🔴 TODO |
| INST-001 | Installment calculation | Tính toán trả góp | Người 3 | Tuần 10 - Thứ 4 | 🔴 TODO |
| INST-002 | Bank integration mock | Mock ngân hàng | Người 3 | Tuần 10 - Thứ 4 | 🔴 TODO |
| INST-003 | Installment tracking | Theo dõi nợ | Người 3 | Tuần 10 - Thứ 5 | 🔴 TODO |
| INST-004 | Overdue alert | Cảnh báo chậm trả | Người 3 | Tuần 10 - Thứ 5 | 🔴 TODO |
| SUP-004 | Unit test | pytest | Người 3 | Tuần 10 - Thứ 6 | 🔴 TODO |
| SUP-005 | Demo & Review | Demo NCC & Trả góp | Người 3 | Tuần 10 - Thứ 7 | 🔴 TODO |

---

## 📌 GIAI ĐOẠN 4: MODULES PHỤ TRỢ (Tuần 11) - 0%

### Module: Marketing
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| MKT-001 | Campaign management | Tạo chiến dịch | Người 1 | Tuần 11 - Thứ 2 | 🔴 TODO |
| MKT-002 | Lead management | Quản lý lead | Người 1 | Tuần 11 - Thứ 3 | 🔴 TODO |
| MKT-003 | Event management | Tổ chức sự kiện | Người 1 | Tuần 11 - Thứ 4 | 🔴 TODO |
| MKT-004 | Campaign effectiveness | Đo hiệu quả | Người 1 | Tuần 11 - Thứ 5 | 🔴 TODO |
| MKT-005 | Unit test | pytest | Người 1 | Tuần 11 - Thứ 6 | 🔴 TODO |

### Module: Khiếu nại (Complaint)
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| COMP-001 | Complaint service | Tiếp nhận KN | Người 2 | Tuần 11 - Thứ 2 | 🔴 TODO |
| COMP-002 | Complaint workflow | Xử lý KN | Người 2 | Tuần 11 - Thứ 3 | 🔴 TODO |
| COMP-003 | Assignment | Phân công xử lý | Người 2 | Tuần 11 - Thứ 4 | 🔴 TODO |
| COMP-004 | Satisfaction survey | Đánh giá hài lòng | Người 2 | Tuần 11 - Thứ 5 | 🔴 TODO |
| COMP-005 | Complaint report | Thống kê KN | Người 2 | Tuần 11 - Thứ 6 | 🔴 TODO |
| COMP-006 | Unit test | pytest | Người 2 | Tuần 11 - Thứ 6 | 🔴 TODO |

### Milestone: Review Tuần 11
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| REV-001 | Integration check | Kiểm tra tích hợp | Tất cả | Tuần 11 - Thứ 7 | 🔴 TODO |

---

## 📌 GIAI ĐOẠN 5: BÁO CÁO & HOÀN THIỆN (Tuần 12) - 0%

### Module: Dashboard & Báo cáo
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| DASH-001 | Dashboard UI | Giao diện tổng quan | Người 3 | Tuần 12 - Thứ 2 | 🔴 TODO |
| DASH-002 | Revenue charts | Biểu đồ doanh thu | Người 3 | Tuần 12 - Thứ 3 | 🔴 TODO |
| DASH-003 | Inventory reports | Báo cáo tồn kho | Người 3 | Tuần 12 - Thứ 3 | 🔴 TODO |
| DASH-004 | Sales reports | Báo cáo bán hàng | Người 3 | Tuần 12 - Thứ 4 | 🔴 TODO |
| DASH-005 | Export Excel/PDF | Xuất báo cáo | Người 3 | Tuần 12 - Thứ 4 | 🔴 TODO |

### Testing & Release
| ID | Task | Mô tả | Assignee | Due | Status |
|----|------|-------|----------|-----|--------|
| TEST-001 | Integration testing | Test toàn bộ hệ thống | Tất cả | Tuần 12 - Thứ 5 | 🔴 TODO |
| TEST-002 | Performance testing | < 2s response time | Tất cả | Tuần 12 - Thứ 5 | 🔴 TODO |
| TEST-003 | Bug fixing | Sửa lỗi phát hiện | Tất cả | Tuần 12 - Thứ 6 | 🔴 TODO |
| DOC-001 | User manual | Hướng dẫn sử dụng | Người 1 | Tuần 12 - Thứ 6 | 🔴 TODO |
| DOC-002 | API documentation | Tài liệu API | Người 2 | Tuần 12 - Thứ 6 | 🔴 TODO |
| REL-001 | Final demo | Demo release | Tất cả | Tuần 12 - Thứ 7 | 🔴 TODO |
| REL-002 | v1.0 Release | Tag release | Tất cả | Tuần 12 - Thứ 7 | 🔴 TODO |

---

## 📝 HƯỚNG DẪN SỬ DỤNG

### Cập nhật task status:
```markdown
# Khi hoàn thành task
- Đổi 🔴 -> 🟢
- Ghi ngày hoàn thành
- Commit message: "feat: TASK-ID - mô tả"

# Khi đang làm
- Đổi 🔴 -> 🟡
- Ghi tên người đang làm

# Khi phát hiện bug
- Tạo task BUG-XXX
- Reference đến task gốc
- Priority: HIGH
```

### Workflow:
1. Chọn task từ danh sách
2. Đổi status thành 🟡 IN PROGRESS
3. Tạo branch: `git checkout -b feature/TASK-ID`
4. Code & commit
5. Tạo Pull Request
6. Review & Merge
7. Đổi status thành 🟢 DONE

---

## 📈 LỊCH SỬ CẬP NHẬT

| Ngày | Cập nhật | Người |
|------|----------|-------|
| 16/04/2026 | Hoàn thành Database setup (10/10 tasks) | Miao |
| 16/04/2026 | Tạo file TASK.md ban đầu | Miao |

---

**Ngày tạo**: 16/04/2026
**Lần cập nhật cuối**: 16/04/2026
**Người tạo**: Miao
**Phiên bản**: 2.0