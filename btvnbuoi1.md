# BÀI TẬP VỀ NHÀ - BUỔI 1

**Trả lời:**  
Python là ngôn ngữ thông dịch (Interpreted language). Chính xác hơn, quy trình thực thi của Python là sự kết hợp giữa cả **biên dịch** và **thông dịch**.

**Tại sao?**
* **Quy trình dịch mã nguồn:** Khi chạy một chương trình Python, mã nguồn (`.py`) đầu tiên sẽ được **biên dịch** tự động thành một dạng mã trung gian gọi là **Bytecode** (`.pyc`).
* **Quy trình thực thi:** Sau đó, trình thông dịch của Python (Python Virtual Machine - PVM) sẽ đọc từng dòng Bytecode này và **thông dịch** trực tiếp thành mã máy (Machine code) để phần cứng máy tính hiểu và thực thi ngay lúc đó (Runtime).
* **Đặc trưng:** Vì quá trình chạy thực tế diễn ra bằng cách đọc và dịch từng dòng lệnh ở Runtime, Python mang đầy đủ tính chất của một ngôn ngữ thông dịch: dễ debug, độc lập nền tảng nhưng tốc độ thực thi sẽ chậm hơn các ngôn ngữ biên dịch thuần túy (như C/C++).

---

## Bài 2: Liệt kê các kiến thức cơ bản trong Python

### 1. Các kiểu dữ liệu cơ bản trong Python

* **Kiểu số (Numeric):** 
  * `int`: Kiểu số nguyên (Ví dụ: `5`, `-10`)
  * `float`: Kiểu số thực/số thập phân (Ví dụ: `3.14`, `-0.5`)
  * `complex`: Kiểu số phức (Ví dụ: `1 + 2j`)

* **Kiểu chuỗi (Sequence):**
  * `str`: Kiểu chuỗi ký tự/văn bản (string) (Ví dụ: `"Hello"`, `'Python'`)
  * `list`: Danh sách các phần tử, có thể thay đổi (Ví dụ: `[1, 2, "Python"]`)
  * `tuple`: Danh sách các phần tử cố định, không thể thay đổi sau khi tạo (Ví dụ: `(1, 2, 3)`)

* **Kiểu tập hợp (Set):**
  * `set`: Tập hợp các phần tử không trùng lặp và không có thứ tự (Ví dụ: `{1, 2, 3}`)

* **Kiểu ánh xạ (Mapping):**
  * `dict`: Kiểu từ điển, lưu trữ dữ liệu dưới dạng cặp `key: value` (Ví dụ: `{"name": "Anh", "age": 20}`)

* **Kiểu logic (Boolean):**
  * `bool`: Chỉ nhận một trong hai giá trị `True` hoặc `False`.

### 2. Các toán tử trong Python
* **Toán tử số học:** `+` (cộng), `-` (trừ), `*` (nhân), `/` (chia lấy số thực), `//` (chia lấy nguyên), `%` (chia lấy dư), `**` (mũ/lũy thừa).
* **Toán tử so sánh:** `==` (bằng), `!=` (khác), `>` (lớn hơn), `<` (nhỏ hơn), `>=` (lớn hơn hoặc bằng), `<=` (nhỏ hơn hoặc bằng).
* **Toán tử logic:** `and` (và), `or` (hoặc), `not` (phủ định).
* **Toán tử gán:** `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.
* **Toán tử nhận dạng (Identity):** `is` (là), `is not` (không phải là) — dùng để kiểm tra xem hai biến có cùng trỏ vào một đối tượng hay không.
* **Toán tử thành viên (Membership):** `in` (thuộc), `not in` (không thuộc) — dùng để kiểm tra một phần tử có nằm trong tập hợp/chuỗi/list hay không.

### 3. Mệnh đề điều kiện và vòng lặp
* **Mệnh đề điều kiện:** Dùng để rẽ nhánh chương trình dựa trên điều kiện logic.
  * Cú pháp gồm các từ khóa: `if`, `elif` (else if), và `else`.
* **Vòng lặp:** Dùng để lặp đi lặp lại một khối lệnh.
  * Vòng lặp `for`: Dùng để duyệt qua các phần tử của một tập hợp (list, tuple, chuỗi) hoặc lặp với số lần biết trước (kết hợp hàm `range()`).
  * Vòng lặp `while`: Lặp lại khối lệnh liên tục khi mà điều kiện kiểm tra còn đúng (`True`).

### 4. Kiểu dữ liệu True, False
* `True` và `False` là hai giá trị duy nhất thuộc kiểu dữ liệu Boolean (`bool`).
* **Lưu ý cú pháp:** Trong Python, hai từ khóa này bắt buộc phải **viết hoa chữ cái đầu** (`True`, `False`), viết thường (`true`, `false`) sẽ bị báo lỗi cú pháp.
* Chúng thường là kết quả trả về của các phép toán so sánh hoặc các biểu thức logic và đóng vai trò làm điều kiện quyết định cho mệnh đề điều kiện (`if...else`) hoặc vòng lặp (`while`).