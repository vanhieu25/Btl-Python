# PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG  
**Phần mềm quản lý đại lý xe hơi**

## 1. PHÂN TÍCH YÊU CẦU

### 1.1 Actors hệ thống
- **Quản trị viên**: Quản lý toàn bộ hệ thống, nhân viên, cấu hình
- **Nhân viên bán hàng**: Quản lý xe, khách hàng, tạo hợp đồng
- **Nhân viên kho**: Quản lý tồn kho, nhập xe mới
- **Khách hàng**: Xem thông tin xe (chế độ công khai)

### 1.2 Use Cases chính
- UC1: Quản lý thông tin xe
- UC2: Quản lý thông tin khách hàng  
- UC3: Quản lý nhân viên và phân quyền
- UC4: Tạo và quản lý hợp đồng bán xe
- UC5: Quản lý tồn kho xe
- UC6: Xem báo cáo thống kê
- UC7: Đăng nhập/đăng xuất hệ thống

## 2. SƠ ĐỒ USE CASE

### 2.1 Mô tả Use Case Diagram
```
@startuml
left to right direction
actor "Quản trị viên" as admin
actor "Nhân viên bán hàng" as sales
actor "Nhân viên kho" as warehouse
actor "Khách hàng" as customer

rectangle "Hệ thống quản lý đại lý xe hơi" {
  admin -- (Quản lý nhân viên)
  admin -- (Xem báo cáo thống kê)
  admin -- (Cấu hình hệ thống)
  
  sales -- (Quản lý thông tin xe)
  sales -- (Quản lý thông tin khách hàng)
  sales -- (Tạo hợp đồng bán xe)
  sales -- (Xem báo cáo cá nhân)
  
  warehouse -- (Quản lý tồn kho)
  warehouse -- (Nhập xe mới)
  
  customer -- (Xem thông tin xe)
  
  (Tạo hợp đồng bán xe) .> (Quản lý tồn kho) : include
  (Tạo hợp đồng bán xe) .> (Quản lý thông tin khách hàng) : include
  (Quản lý thông tin xe) .> (Quản lý tồn kho) : include
}
@enduml
```

## 3. SƠ ĐỒ LỚP (CLASS DIAGRAM)

### 3.1 Các lớp chính
- **User**: Base class cho Employee và Customer
- **Employee**: Kế thừa User, có vai_trò, sđt, email
- **Customer**: Kế thừa User, có phân_loại, lịch_sử_giao_dịch
- **Car**: mã_xe, hãng, dòng_xe, năm_sx, màu_sắc, giá_bán
- **Contract**: mã_hợp_đồng, xe, khách_hàng, nhân_viên, giá_trị, trạng_thái
- **Inventory**: xe, số_lượng, ngày_cập_nhật
- **AuditLog**: người_dùng, hành_động, thời_gian

### 3.2 Mô tả Class Diagram
```
@startuml
class User {
  +id: int
  +họ_tên: str
  +email: str
}

class Employee {
  +vai_trò: str
  +sđt: str
}

class Customer {
  +phân_loại: str
  +lịch_sử_giao_dịch: list
}

class Car {
  +mã_xe: str
  +hãng: str
  +dòng_xe: str
  +năm_sx: int
  +màu_sắc: str
  +giá_bán: float
}

class Contract {
  +mã_hợp_đồng: str
  +giá_trị: float
  +trạng_thái: str
}

class Inventory {
  +số_lượng: int
  +ngày_cập_nhật: datetime
}

class AuditLog {
  +hành_động: str
  +thời_gian: datetime
}

User <|-- Employee
User <|-- Customer
Employee "1" -- "0..*" Contract : tạo >
Customer "1" -- "0..*" Contract : mua >
Car "1" -- "0..*" Contract : bán >
Car "1" -- "1" Inventory : quản lý >
User "1" -- "0..*" AuditLog : thực hiện >
@enduml
```

## 4. SƠ ĐỒ TUẦN TỰ (SEQUENCE DIAGRAM)

### 4.1 Use Case: Tạo hợp đồng bán xe
```
@startuml
actor "Nhân viên bán hàng" as sales
participant "ContractController" as controller
participant "CarModel" as car
participant "CustomerModel" as customer
participant "InventoryModel" as inventory
participant "Database" as db

sales -> controller: create_contract(car_id, customer_id, employee_id)
controller -> car: get_car_info(car_id)
car -> db: SELECT * FROM cars WHERE id = car_id
db --> car: car_data
car --> controller: car_info

controller -> customer: get_customer_info(customer_id)
customer -> db: SELECT * FROM customers WHERE id = customer_id
db --> customer: customer_data
customer --> controller: customer_info

controller -> inventory: update_inventory(car_id, -1)
inventory -> db: UPDATE inventory SET quantity = quantity - 1 WHERE car_id = car_id
db --> inventory: success
inventory --> controller: updated

controller -> db: INSERT INTO contracts (...)
db --> controller: contract_id

controller --> sales: Hợp đồng đã được tạo thành công!
@enduml
```

## 5. SƠ ĐỒ TRẠNG THÁI (STATE DIAGRAM)

### 5.1 Trạng thái hợp đồng
```
@startuml
[*] --> Mới_tạo
Mới_tạo --> Đã_thanh_toán : thanh_toán()
Đã_thanh_toán --> Đã_giao_xe : giao_xe()
Đã_giao_xe --> [*]
Mới_tạo --> Hủy : hủy_hợp_đồng()
Hủy --> [*]
@enduml
```

### 5.2 Trạng thái tồn kho xe
```
@startuml
[*] --> Còn_hàng
Còn_hàng --> Sắp_hết : tồn_kho <= mức_cảnh_báo
Sắp_hết --> Còn_hàng : nhập_xe_mới()
Còn_hàng --> Hết_hàng : tồn_kho = 0
Hết_hàng --> Còn_hàng : nhập_xe_mới()
@enduml
```

## 6. SƠ ĐỒ HOẠT ĐỘNG (ACTIVITY DIAGRAM)

### 6.1 Hoạt động quản lý xe
```
@startuml
start
:Hiển thị menu quản lý xe;
if (Lựa chọn?) then (Thêm xe)
  :Nhập thông tin xe;
  :Validate dữ liệu;
  if (Hợp lệ?) then (Có)
    :Lưu vào database;
    :Cập nhật tồn kho;
  else (Không)
    :Hiển thị lỗi;
  endif
elseif (Sửa xe)
  :Chọn xe cần sửa;
  :Hiển thị thông tin hiện tại;
  :Nhập thông tin mới;
  :Cập nhật database;
elseif (Xóa xe)
  :Chọn xe cần xóa;
  if (Có hợp đồng liên quan?) then (Có)
    :Không cho phép xóa;
  else (Không)
    :Xóa khỏi database;
    :Cập nhật tồn kho;
  endif
elseif (Tìm kiếm xe)
  :Nhập tiêu chí tìm kiếm;
  :Truy vấn database;
  :Hiển thị kết quả;
endif
stop
@enduml
```

## 7. PHÂN TÍCH KIẾN TRÚC

### 7.1 Kiến trúc MVC
- **Model**: Các lớp dữ liệu (Car, Customer, Contract, v.v.)
- **View**: Giao diện console hiển thị menu và kết quả
- **Controller**: Xử lý logic nghiệp vụ, điều phối Model và View

### 7.2 Luồng dữ liệu
1. Người dùng tương tác với View (console)
2. View gọi Controller với tham số đầu vào
3. Controller xử lý logic, gọi Model nếu cần
4. Model truy cập Database để lấy/lưu dữ liệu
5. Controller trả kết quả về View để hiển thị

### 7.3 Xử lý lỗi
- **Validation input**: Kiểm tra dữ liệu đầu vào tại Controller
- **Database errors**: Xử lý exception khi truy vấn database
- **Business rules**: Kiểm tra quy tắc nghiệp vụ (ví dụ: không xóa xe có hợp đồng)

## 8. YÊU CẦU PHI CHỨC NĂNG TRONG THIẾT KẾ

### 8.1 Hiệu năng
- **Indexing**: Tạo index cho các trường thường tìm kiếm (mã_xe, họ_tên, v.v.)
- **Pagination**: Hiển thị danh sách với phân trang (mỗi trang 20 items)
- **Caching**: Cache dữ liệu thường dùng (danh sách xe, khách hàng)

### 8.2 Bảo mật
- **Input sanitization**: Làm sạch input để tránh SQL injection
- **Password hashing**: Mã hóa mật khẩu bằng bcrypt
- **Session management**: Timeout session sau 30 phút

### 8.3 Khả năng mở rộng
- **Modular design**: Mỗi module độc lập, dễ thêm tính năng mới
- **Configuration**: Các tham số hệ thống có thể cấu hình
- **Database abstraction**: Dễ dàng chuyển sang database khác

## 9. CÔNG CỤ ĐỀ XUẤT

### 9.1 Tạo sơ đồ UML
- **PlantUML**: Viết mã text, render thành hình ảnh
- **Draw.io**: Công cụ vẽ sơ đồ online miễn phí
- **Lucidchart**: Công cụ chuyên nghiệp cho diagram

### 9.2 Triển khai
- **Python**: Ngôn ngữ chính
- **SQLite**: Database ban đầu
- **pytest**: Testing framework
- **reportlab**: Export PDF cho hợp đồng