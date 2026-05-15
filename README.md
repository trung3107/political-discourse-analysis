# DỮ LIỆU VÀ PHƯƠNG PHÁP NGHIÊN CỨU
Phân tích diễn ngôn của các đại biểu trúng cử 
# Phân tích Diễn ngôn của các Đại biểu trúng cử 

---

### 1. Dữ liệu nghiên cứu (Data Input)

Dữ liệu được trích xuất từ văn bản **“Chương trình hành động”** của 32 ứng cử viên trúng cử Đại biểu Quốc hội khóa XV thuộc TP. Hà Nội (bầu cử năm 2026). Đây là thể loại văn bản chính trị có tính cô đọng cao; là nơi các ứng cử viên trình bày ưu tiên chính sách và thông điệp trung tâm trước cử tri.

**Cơ cấu mẫu khảo sát (N = 32):**
* **Nam:** 21 đại biểu.
* **Nữ:** 11 đại biểu (chiếm 34.4%, tương đối sát với tỷ lệ nữ đại biểu toàn quốc cùng nhiệm kỳ).
* **Đại diện thể chế:** Đa dạng từ lãnh đạo trung ương, cán bộ quản lý địa phương, đại diện tổ chức chính trị – xã hội đến chuyên gia (giáo dục, y tế, kinh tế, quản trị công). Sự đa dạng này cho phép đối chiếu đồng thời ảnh hưởng của giới tính và vị thế quyền lực lên ngôn ngữ chính trị.

### 2. Xử lý dữ liệu (Feature Engineering)

Nghiên cứu tiến hành phân tích định lượng thông qua việc đo lường tần suất từ khóa theo hai trường từ vựng vĩ mô:

* **Nhóm An sinh / Vi mô:** "y tế", "chăm sóc sức khỏe", "bệnh viện", "bảo hiểm y tế", "giáo dục", "học sinh", "sinh viên", "trẻ em", "trường học", "an sinh xã hội", "người lao động", "hộ nghèo", "việc làm", "thu nhập", "phụ nữ", "bình đẳng giới", "gia đình", "trẻ em gái".
* **Nhóm Kỹ trị / Vĩ mô:** "tăng trưởng", "kinh tế", "đầu tư", "doanh nghiệp", "chính sách", "quản lý", "cải cách", "pháp luật", "hạ tầng", "giao thông", "đô thị", "quy hoạch".

**Chuẩn hóa biến số:**
Do độ dài văn bản không đồng đều, hệ thống loại bỏ sai lệch đếm thô bằng cách tính mật độ từ khóa trên 1.000 từ:

> Rate = (Số từ khóa / Tổng số từ của văn bản) * 1000

Quá trình này định hình hai biến số liên tục:
* `Rate_KyTri`: Mật độ từ khóa kỹ trị (‰)
* `Rate_AnSinh`: Mật độ từ khóa an sinh (‰)

Dữ liệu chuẩn hóa được phân tích bằng Thống kê mô tả (Mean, SD, Min, Max) để nhận diện quy luật phân bổ và độ phân tán nội bộ. Thống kê mô tả đóng vai trò la bàn để phát hiện xu hướng, tạo tiền đề cho phân tích diễn ngôn phê phán.

### 3. Chọn mẫu Phân tích diễn ngôn (Purposive Sampling)

Nếu thống kê mô tả cung cấp bức tranh toàn cảnh, thì **Phân tích Diễn ngôn Phê phán (CDA)** đi sâu vào bản chất cấu trúc quyền lực. Hệ thống sử dụng chiến lược *chọn mẫu có chủ đích theo biến thiên tối đa*, trích xuất các điểm cực trị và ngoại lệ từ dữ liệu định lượng thành 4 nhóm điển hình:

* **Nhóm A – Nữ có mật độ an sinh cao (Đại diện: Lê Kim Anh, Dương Minh Ánh):**
  Nhấn mạnh các vấn đề xã hội và nhóm yếu thế. Phép thử: Họ đang tái hiện khuôn mẫu giới tính truyền thống hay định hình một diễn ngôn mới?
* **Nhóm B – Nữ có diễn ngôn kỹ trị nổi trội (Đại diện: Nguyễn Phương Thủy, Nguyễn Thị Tuyến):**
  Mật độ từ an sinh tiệm cận 0. Phép thử: Sự vắng bóng này có phải là kết quả của việc chuẩn hóa ngôn ngữ để thích nghi với thể chế?
* **Nhóm C – Nam có điểm đột phá an sinh (Đại diện: Nguyễn Lân Hiếu):**
  Trường hợp ngoại lệ (Outlier). Phép thử: Liệu chuyên môn nghề nghiệp có sức nặng áp đảo giới tính sinh học trong việc lựa chọn từ vựng?
* **Nhóm D – Nam đại diện chuẩn kỹ trị (Đại diện: Tô Lâm):**
  Đóng vai trò nhóm đối chứng (Control group) chuẩn mực của quyền lực kỹ trị. Phép thử: Các nhóm khác (đặc biệt Nhóm B) có đang mô phỏng lại cùng một hệ quy chiếu ngôn ngữ này không?

Chiến lược này đảm bảo các kết luận từ CDA được neo chặt vào các bằng chứng toán học (Data-driven), loại bỏ hoàn toàn sự cảm tính trong quá trình phân tích.
