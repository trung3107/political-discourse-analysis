# BƯỚC 1: Khởi động công cụ
library(dplyr)

# BƯỚC 2: Chạy hệ thống đo lường toàn diện (Thêm biên Min/Max)
bang_so_sanh_toan_dien <- df %>%
  group_by(GioiTinh) %>%
  summarise(
    So_Luong_Mau = n(),
    
    # --- Module: Khảo sát trục Kỳ Trị ---
    Trung_Binh_Ky_Tri = mean(Rate_KyTri, na.rm = TRUE),
    Do_Lech_Chuan_Ky_Tri = sd(Rate_KyTri, na.rm = TRUE),
    Min_Ky_Tri = min(Rate_KyTri, na.rm = TRUE),
    Max_Ky_Tri = max(Rate_KyTri, na.rm = TRUE),
    
    # --- Module: Khảo sát trục An Sinh ---
    Trung_Binh_An_Sinh = mean(Rate_AnSinh, na.rm = TRUE),
    Do_Lech_Chuan_An_Sinh = sd(Rate_AnSinh, na.rm = TRUE),
    Min_An_Sinh = min(Rate_AnSinh, na.rm = TRUE),
    Max_An_Sinh = max(Rate_AnSinh, na.rm = TRUE)
  )

# BƯỚC 3: Mở bảng tổng soát
View(bang_so_sanh_toan_dien)



# BƯỚC 1 & 2: Vận hành cỗ máy đo lường như cũ
library(dplyr)

bang_so_sanh_toan_dien <- df %>%
  group_by(GioiTinh) %>%
  summarise(
    So_Luong_Mau = n(),
    
    Trung_Binh_Ky_Tri = mean(Rate_KyTri, na.rm = TRUE),
    Do_Lech_Chuan_Ky_Tri = sd(Rate_KyTri, na.rm = TRUE),
    Min_Ky_Tri = min(Rate_KyTri, na.rm = TRUE),
    Max_Ky_Tri = max(Rate_KyTri, na.rm = TRUE),
    
    Trung_Binh_An_Sinh = mean(Rate_AnSinh, na.rm = TRUE),
    Do_Lech_Chuan_An_Sinh = sd(Rate_AnSinh, na.rm = TRUE),
    Min_An_Sinh = min(Rate_AnSinh, na.rm = TRUE),
    Max_An_Sinh = max(Rate_AnSinh, na.rm = TRUE)
  )

# BƯỚC 3: Xuất thẳng báo cáo ra màn hình Console
print(bang_so_sanh_toan_dien)

# (Lưu ý: Trong phòng mô phỏng R, bạn thậm chí chỉ cần gõ tên biến 
# rồi nhấn Enter/Run là máy sẽ tự hiểu lệnh in ra console)
# bang_so_sanh_toan_dien


# BƯỚC 1: Đảm bảo công cụ đồ họa đang mở
library(ggplot2)

# BƯỚC 2: Kết xuất bản đồ phân bố nguyên bản
ggplot(data = df, aes(x = GioiTinh, y = Rate_KyTri, fill = GioiTinh)) +
  
  # Module Sóng: Đổ màu nhẹ để phân tách nhóm, tắt đường viền (color = NA)
  geom_violin(alpha = 0.5, trim = FALSE, color = NA) +
  
  # Module Hạt: Tăng độ rõ nét của từng dữ liệu thô
  geom_jitter(width = 0.1, alpha = 0.6, color = "black", size = 1.2) +
  
  # Module Giao diện: Chuẩn hóa nhãn dán
  labs(
    title = "Cấu trúc Nguyên bản: Mật độ Điểm Kỳ Trị theo Giới Tính",
    x = "Hệ Giới Tính",
    y = "Mức độ Kỳ Trị"
  ) +
  
  # Module Tối giản: Loại bỏ nhiễu
  theme_minimal() +
  theme(
    legend.position = "none",
    plot.title = element_text(face = "bold", size = 14)
  )