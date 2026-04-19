# Sprint-3.4: Contract PDF Export

**1. Xác định feature:**
- [ ] Define requirements: Xuất hợp đồng dưới dạng PDF chuyên nghiệp với đầy đủ thông tin
- [ ] Identify dependencies: Phụ thuộc vào Sprint-3.3 (Contract Calculation) và Sprint-3.1 (Contract Management)
- [ ] Plan database schema: Thêm fields để tracking PDF export status nếu cần

**2. Database:**
- [ ] Create/migrate tables: Cập nhật bảng contracts nếu cần thêm PDF-related fields
- [ ] Define relationships: Giữ nguyên relationships hiện có với customers, cars, v.v.
- [ ] Add indexes/constraints: Thêm indexes cho PDF export tracking nếu cần
- [ ] Test schema integrity: Kiểm tra khả năng lưu trữ PDF metadata

**3. Backend Logic:**
- [ ] Create models: Cập nhật model Contract nếu cần
- [ ] Implement business logic: Implement PDF generation logic sử dụng thư viện reportlab hoặc tương đương
- [ ] Add validation rules: Validate contract data trước khi export, handle missing information
- [ ] Handle errors appropriately: Xử lý PDF generation errors, file system errors, memory issues

**4. UI Design:**
- [ ] Create wireframes: Thiết kế nút export PDF trong chi tiết hợp đồng và danh sách hợp đồng
- [ ] Implement interface: Thêm nút "🖨️ In" hoặc "📄 Export PDF" trong contract detail view
- [ ] Add interactions: PDF preview trước khi download, save dialog, error handling
- [ ] Ensure responsiveness: Đảm bảo nút export hiển thị đẹp trên mọi device

**5. Testing:**
- [ ] Unit tests for backend: Test PDF generation logic với nhiều scenarios, validate PDF content
- [ ] UI acceptance tests: Test PDF export button interactions, file download behavior
- [ ] Integration tests: Test end-to-end flow từ contract detail → PDF generation → file download
- [ ] Edge case scenarios: Test large contracts, special characters, missing data, file system permissions

**6. Git Commit:**
- [ ] Commit with descriptive message: "feat: contract PDF export"
- [ ] Push to remote branch
- [ ] Create pull request if applicable