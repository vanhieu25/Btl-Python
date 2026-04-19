# PLAN DỰ ÁN - PHẦN MỀM QUẢN LÝ ĐẠI LÝ XE HƠI

## THÔNG TIN DỰ ÁN
- **Tên dự án**: Phần mềm quản lý đại lý xe hơi
- **Thành viên nhóm**: 
  - Nguyễn Văn Hiếu (Trưởng nhóm)
  - Lê Minh Đạt
  - Nguyễn Hữu Hải
- **Công nghệ**: Python 3.10+, PyQt6, SQLite
- **Design system**: Notion-inspired

---

## PHÂN TÍCH HIỆN TRẠNG

### ✅ ĐÃ HOÀN THÀNH
1. **Tài liệu yêu cầu**:
   - Yêu cầu chức năng chi tiết (71 chức năng)
   - Danh sách chức năng theo module
   - Thiết kế hệ thống và kiến trúc
   
2. **Demo UI**:
   - Dashboard tổng quan
   - Quản lý Xe (danh sách, thêm/sửa, tìm kiếm)
   - Quản lý Khách hàng (tabs cá nhân/doanh nghiệp)
   - Quản lý Hợp đồng (trạng thái, filter)
   - Sidebar navigation + Notion theme
   
3. **Database models**:
   - 16 bảng dữ liệu với relationships đầy đủ
   - Models cho tất cả các chức năng chính

### ⏳ CẦN PHÁT TRIỂN
1. **UI còn thiếu**:
   - Quản lý Nhân viên
   - Báo cáo thống kê
   - Bảo hành, Khuyến mãi, Phụ kiện
   - Dịch vụ hậu mãi, Marketing, Khiếu nại
   - Trả góp, Nhà cung cấp

2. **Logic nghiệp vụ**:
   - Backend controllers cho tất cả chức năng
   - Kết nối UI với database
   - Xử lý validation và business rules

3. **Tính năng bổ sung**:
   - Export PDF/Excel
   - In ấn hợp đồng
   - Hệ thống bảo mật đầy đủ

---

## PLAN CHI TIẾT THEO GIAI ĐOẠN

### GIAI ĐOẠN 1: HOÀN THIỆN CƠ SỞ (Tuần 1-2)

#### Tuần 1: Hoàn thiện UI cơ bản
| STT | Công việc | Thành viên | Deadline |
|-----|-----------|------------|----------|
| 1.1 | Tạo màn hình Quản lý Nhân viên | Hiếu | 22/04/2026 |
| 1.2 | Tạo màn hình Báo cáo thống kê | Đạt | 23/04/2026 |
| 1.3 | Tạo màn hình Bảo hành | Hải | 24/04/2026 |
| 1.4 | Tạo màn hình Khuyến mãi | Hiếu | 25/04/2026 |
| 1.5 | Tạo màn hình Phụ kiện | Đạt | 26/04/2026 |

#### Tuần 2: Hoàn thiện UI nâng cao
| STT | Công việc | Thành viên | Deadline |
|-----|-----------|------------|----------|
| 2.1 | Tạo màn hình Nhà cung cấp | Hải | 29/04/2026 |
| 2.2 | Tạo màn hình Trả góp | Hiếu | 30/04/2026 |
| 2.3 | Tạo màn hình Dịch vụ hậu mãi | Đạt | 01/05/2026 |
| 2.4 | Tạo màn hình Marketing | Hải | 02/05/2026 |
| 2.5 | Tạo màn hình Khiếu nại | Hiếu | 03/05/2026 |
| 2.6 | Review và chuẩn hóa UI | Cả nhóm | 04/05/2026 |

**Deliverables Giai đoạn 1**:
- ✅ 15/15 màn hình UI hoàn chỉnh
- ✅ Design system consistency
- ✅ Responsive layout

---

### GIAI ĐOẠN 2: PHÁT TRIỂN BACKEND (Tuần 3-5)

#### Tuần 3: Core business logic
| STT | Module | Công việc chính | Thành viên |
|-----|--------|-----------------|------------|
| 3.1 | Database | Setup kết nối, migration | Hiếu |
| 3.2 | Auth | Login, phân quyền, session | Đạt |
| 3.3 | Xe | CRUD, validation, business rules | Hải |
| 3.4 | Khách hàng | CRUD, phân loại VIP | Hiếu |

#### Tuần 4: Business modules
| STT | Module | Công việc chính | Thành viên |
|-----|--------|-----------------|------------|
| 4.1 | Hợp đồng | Tạo HĐ, tính toán giá, trạng thái | Đạt |
| 4.2 | Kho xe | Quản lý tồn kho, cảnh báo | Hải |
| 4.3 | Nhân viên | Quản lý NV, phân quyền | Hiếu |
| 4.4 | Báo cáo | Các loại báo cáo thống kê | Đạt |

#### Tuần 5: Advanced features
| STT | Module | Công việc chính | Thành viên |
|-----|--------|-----------------|------------|
| 5.1 | Bảo hành | Quản lý BH, yêu cầu BH | Hải |
| 5.2 | Khuyến mãi | Logic KM, áp dụng tự động | Hiếu |
| 5.3 | Phụ kiện | Quản lý PK, combo | Đạt |
| 5.4 | Trả góp | Tính toán trả góp, theo dõi | Hải |
| 5.5 | NCC & Hậu mãi | Nhập hàng, dịch vụ | Hiếu |
| 5.6 | Marketing & KN | Lead, khiếu nại | Đạt |

**Deliverables Giai đoạn 2**:
- ✅ 71/71 chức năng backend hoàn chỉnh
- ✅ Unit tests cho core functions
- ✅ API documentation

---

### GIAI ĐOẠN 3: TÍCH HỢP & TEST (Tuần 6-7)

#### Tuần 6: Integration
| STT | Công việc | Mô tả | Thành viên |
|-----|-----------|-------|------------|
| 6.1 | Kết nối UI-Backend | Tất cả màn hình | Cả nhóm |
| 6.2 | Xử lý lỗi | Error handling, validation | Hiếu |
| 6.3 | Performance | Optimizations, caching | Đạt |
| 6.4 | Security | Input sanitization, auth checks | Hải |

#### Tuần 7: Testing & Bug fixing
| STT | Loại test | Mô tả | Người phụ trách |
|-----|-----------|-------|------------------|
| 7.1 | Unit tests | Test từng function | Mỗi thành viên |
| 7.2 | Integration | Test flow end-to-end | Hiếu |
| 7.3 | UI/UX test | Usability testing | Đạt |
| 7.4 | Security test | Penetration testing | Hải |
| 7.5 | Performance | Load testing (50 users) | Cả nhóm |

**Deliverables Giai đoạn 3**:
- ✅ Ứng dụng hoàn chỉnh, chạy được
- ✅ Test reports
- ✅ Bug fixes

---

### GIAI ĐOẠN 4: DEPLOYMENT & DOCUMENTATION (Tuần 8)

| STT | Công việc | Mô tả | Deadline |
|-----|-----------|-------|----------|
| 8.1 | Packaging | Tạo installer/executable | 18/05/2026 |
| 8.2 | User manual | Hướng dẫn sử dụng | 19/05/2026 |
| 8.3 | Technical docs | Tài liệu kỹ thuật | 20/05/2026 |
| 8.4 | Final demo | Chuẩn bị demo cuối kỳ | 21/05/2026 |
| 8.5 | Code review | Final code cleanup | 22/05/2026 |

**Deliverables Giai đoạn 4**:
- ✅ Ứng dụng deployable
- ✅ Complete documentation
- ✅ Final presentation

---

## CRITERIA THÀNH CÔNG

### ✅ Must-have (Bắt buộc)
- [ ] 15 module chức năng hoạt động đầy đủ
- [ ] 71 chức năng theo LIST_CHUC_NANG.md
- [ ] Giao diện người dùng thân thiện, consistent
- [ ] Database thiết kế chuẩn, relationships đúng
- [ ] Bảo mật cơ bản (login, phân quyền)
- [ ] Báo cáo thống kê hoạt động

### 🎯 Should-have (Nên có)
- [ ] Export PDF/Excel cho báo cáo
- [ ] In hợp đồng trực tiếp
- [ ] Cảnh báo email/SMS (mock)
- [ ] Backup/restore database
- [ ] Multi-language support (basic)

### 🌟 Nice-to-have (Bonus)
- [ ] Dark mode toggle
- [ ] Keyboard shortcuts
- [ ] Chart visualization (real charts)
- [ ] Mobile responsive design
- [ ] Cloud sync (mock)

---

## RISKS & MITIGATION

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Thiếu thời gian | High | Medium | Prioritize must-have features first |
| Lỗi database | High | Low | Regular backups, thorough testing |
| UI inconsistency | Medium | Medium | Design system guidelines, code review |
| Performance issues | Medium | Low | Optimize queries, pagination |
| Team coordination | Medium | Low | Daily standups, clear task assignment |

---

## RESOURCE REQUIREMENTS

### Công cụ phát triển
- **IDE**: VS Code / PyCharm
- **Version control**: Git + GitHub
- **Testing**: pytest, unittest
- **Documentation**: Markdown, diagrams.net

### Dependencies
```txt
PyQt6>=6.4.0
SQLAlchemy>=2.0.0
python-dotenv>=1.0.0
reportlab>=4.0.0  # for PDF export
openpyxl>=3.1.0   # for Excel export
```

### Môi trường
- **OS**: Windows 10/11, macOS 10.14+, Ubuntu 20.04+
- **Python**: 3.10+
- **RAM**: 4GB minimum
- **Storage**: 500MB free space

---

## TRACKING & MONITORING

### Daily standup questions
1. Hôm qua bạn làm gì?
2. Hôm nay bạn sẽ làm gì?
3. Có blocker nào không?

### Progress tracking
- **GitHub Issues**: Theo dõi từng task
- **Weekly demos**: Demo tiến độ mỗi tuần
- **Code reviews**: Pull request reviews
- **Testing coverage**: Track test coverage %

### Success metrics
- **Functionality**: 71/71 functions working
- **Code quality**: >80% test coverage
- **Performance**: <2s response time
- **Usability**: Training time ≤ 2 hours

---

## TIMELINE OVERVIEW

```
Tuần 1-2: UI Development     ████████████░░░░░░░░░░░░░░░░ (25%)
Tuần 3-5: Backend Dev       ████████████████████████░░░░ (60%)
Tuần 6-7: Testing           ████████████████████████████ (85%)
Tuần 8:   Final Delivery    ████████████████████████████ (100%)
```

**Ngày bắt đầu**: 22/04/2026  
**Ngày hoàn thành**: 22/05/2026  
**Tổng thời gian**: 4 tuần (8 weeks part-time)

---

## NEXT STEPS IMMEDIATE

1. **[Today]** Tạo branch `feature/ui-completion` 
2. **[Today]** Assign tasks cho Tuần 1 trong GitHub Issues
3. **[Tomorrow]** Daily standup đầu tiên lúc 9h sáng
4. **[This week]** Hoàn thành 5 màn hình UI đầu tiên

---

*Plan được tạo ngày: 19/04/2026*  
*Phiên bản: 1.0*  
*Người tạo: Miao 🌸*