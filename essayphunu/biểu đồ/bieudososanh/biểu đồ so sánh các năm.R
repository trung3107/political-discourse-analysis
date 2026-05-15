# Tải thư viện lõi
library(ggplot2)
library(dplyr)

# 1. Khởi tạo không gian dữ liệu (Kết hợp dữ liệu lịch sử và 3 khóa mới)
data <- data.frame(
  NhiemKy = c("1987-1992", "1992-1997", "1997-2002", 
              "2002-2007", "2007-2011", "2011-2016", "2016-2021", "2021-2026", "2026-2031"),
  TyLe = c(17.74, 18.48, 26.22, 
           27.31, 25.76, 24.40, 26.81, 30.26, 30.00)
)

# Đảm bảo trục X giữ đúng thứ tự thời gian (không bị R tự động xếp theo alphabet)
data$NhiemKy <- factor(data$NhiemKy, levels = data$NhiemKy)

# 2. Xây dựng mô hình trực quan
ggplot(data, aes(x = NhiemKy, y = TyLe, group = 1)) +
  # Vẽ quỹ đạo (Line) và các điểm nút (Points)
  geom_line(color = "saddlebrown", size = 1) +
  geom_point(color = "darkblue", shape = 18, size = 4) +
  
  # Gắn nhãn dữ liệu thực tế tại các điểm nút
  geom_text(aes(label = sprintf("%.2f%%", TyLe)), 
            vjust = -1, hjust = 0.5, size = 3.5, color = "black") +
  
  # Cấu hình thang đo trục Y (0% - 35%)
  scale_y_continuous(limits = c(0, 35), 
                     breaks = seq(0, 35, by = 5),
                     labels = function(x) paste0(x, "%")) +
  
  # Gắn nhãn hệ thống
  labs(
       x = "Nhiệm kỳ",
       y = "Tỷ lệ") +
  
  # Tối ưu hóa giao diện (Theme) tương đồng với biểu đồ gốc
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold", size = 14),
    axis.text.x = element_text(angle = 45, hjust = 1, size = 10),
    panel.background = element_rect(fill = "lightcyan", color = NA),
    panel.grid.major = element_line(color = "darkgray", linetype = "dashed"),
    panel.grid.minor = element_blank()
  )

# Lệnh kết xuất hình ảnh chuẩn học thuật
ggsave(
  filename = "BieuDo_TyLeNuDaiBieu.png", # Tên file xuất ra
  plot = last_plot(),                    # Gọi lại biểu đồ vừa vẽ xong
  width = 6.5,                           # Chiều rộng 6.5 inches (Khớp với lề chuẩn A4 trong Word)
  height = 4.0,                          # Chiều cao 4 inches (Tỷ lệ hài hòa, không chiếm trọn trang)
  units = "in",                          # Đơn vị đo
  dpi = 300,                             # Mật độ điểm ảnh 300 DPI (Chuẩn in ấn sắc nét tuyệt đối)
  bg = "white"                           # Fix lỗi nền trong suốt (transparent) khi dán vào Word
)

getwd()
