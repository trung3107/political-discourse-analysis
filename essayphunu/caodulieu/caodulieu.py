import pdfplumber
import pandas as pd
import re
import os

# ==========================================
# 1. BỘ TỪ ĐIỂN MÃ HÓA (CODEBOOK)
# ==========================================
CODEBOOK = {
    "AnSinh": [
        "y tế", "chăm sóc sức khỏe", "bệnh viện", "bảo hiểm y tế",
        "giáo dục", "học sinh", "sinh viên", "trẻ em", "trường học",
        "an sinh xã hội", "người lao động", "hộ nghèo", "việc làm", "thu nhập",
        "phụ nữ", "bình đẳng giới", "gia đình", "trẻ em gái"
    ],
    "KyTri": [
        "tăng trưởng", "kinh tế", "đầu tư", "doanh nghiệp",
        "chính sách", "quản lý", "cải cách", "pháp luật",
        "hạ tầng", "giao thông", "đô thị", "quy hoạch"
    ]
}


# ==========================================
# 2. ĐỘNG CƠ BÓC TÁCH PDF
# ==========================================
def process_local_pdf(file_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            # Rút trích chữ từ tất cả các trang
            full_text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])

        clean_text = " ".join(full_text.lower().split())
        total_words = len(clean_text.split())

        # Bẫy lỗi: File rỗng hoặc File Scan (PDF ảnh)
        if total_words == 0:
            print(f"  -> [CẢNH BÁO] File {file_path} không có văn bản (Khả năng là PDF Scan).")
            return None

        results = {"Total_Words": total_words}
        for category, keywords in CODEBOOK.items():
            count = 0
            for word in keywords:
                count += len(re.findall(r'\b' + re.escape(word) + r'\b', clean_text))

            results[f"Count_{category}"] = count
            results[f"Rate_{category}"] = round((count / total_words) * 1000, 2)

        results["GDS_Score"] = results["Rate_AnSinh"] - results["Rate_KyTri"]
        return results, full_text

    except FileNotFoundError:
        print(f"  -> [LỖI] Không tìm thấy file: {file_path}")
        return None
    except Exception as e:
        print(f"  -> [LỖI HỆ THỐNG] Sự cố đọc file {file_path}: {e}")
        return None


# ==========================================
# 3. ĐỊNH TUYẾN DỮ LIỆU
# ==========================================
thu_muc_hien_tai = os.path.dirname(os.path.abspath(__file__))

danh_sach_db = [
    {"Ten": "Đại biểu DƯƠNG MINH ÁNH", "GioiTinh": "Nữ", "File_Name": os.path.join(thu_muc_hien_tai, "5.pdf")},
    {"Ten": "Đại biểu TÔ LÂM", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "1.pdf")},
    {"Ten": "Đại biểu NGUYỄN HOÀNG TRƯỜNG", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "3.pdf")},
    {"Ten": "Đại biểu LƯU NAM TIẾN", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "2.pdf")},
    {"Ten": "Đại biểu TRẦN VIỆT ANH", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "4.pdf")},
    {"Ten": "Đại biểu HUỲNH QUYẾT THẮNG", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "6.pdf")},
    {"Ten": "Đại biểu LÊ KIM ANH", "GioiTinh": "Nữ ", "File_Name": os.path.join(thu_muc_hien_tai, "7.pdf")},
    {"Ten": "Đại biểu NGUYỄN THỊ HỒNG CHƯƠNG", "GioiTinh": "Nữ", "File_Name": os.path.join(thu_muc_hien_tai, "8.pdf")},
    {"Ten": "Đại biểu NGUYỄN LÂN HIẾU", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "9.pdf")},
    {"Ten": "Đại biểu PHÙNG THỊ HỒNG HÀ", "GioiTinh": "Nữ", "File_Name": os.path.join(thu_muc_hien_tai, "10.pdf")},
    {"Ten": "Đại biểu HỒ SỸ HÙNG", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "11.pdf")},
    {"Ten": "Đại biểu NGUYỄN XUÂN KỲ", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "12.pdf")},
    {"Ten": "Đại biểu LÊ HỒNG HÀ", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "13.pdf")},
    {"Ten": "Đại biểu TRẦN THỊ NHỊ HÀ", "GioiTinh": "Nữ", "File_Name": os.path.join(thu_muc_hien_tai, "14.pdf")},
    {"Ten": "Đại biểu BÙI HOÀI SƠN", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "15.pdf")},
    {"Ten": "Đại biểu TRẦN THANH HÀ", "GioiTinh": "Nữ", "File_Name": os.path.join(thu_muc_hien_tai, "16.pdf")},
    {"Ten": "Đại biểu DƯƠNG ĐỨC HẢI", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "17.pdf")},
    {"Ten": "Đại biểu ĐẶNG MINH CHÂU (HÒA THƯỢNG THÍCH BẢO NGHIÊM", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "18.pdf")},
    {"Ten": "Đại biểu NGUYỄN THỊ THU DUNG", "GioiTinh": "Nữ", "File_Name": os.path.join(thu_muc_hien_tai, "19.pdf")},
    {"Ten": "Đại biểu HOÀNG MINH SƠN", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "20.pdf")},
    {"Ten": "Đại biểu NGUYỄN NGỌC VIỆT", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "21.pdf")},
    {"Ten": "Đại biểu NGUYỄN THỊ LAN", "GioiTinh": "Nữ", "File_Name": os.path.join(thu_muc_hien_tai, "22.pdf")},
    {"Ten": "Đại biểu NGUYỄN PHƯƠNG THỦY", "GioiTinh": "Nữ", "File_Name": os.path.join(thu_muc_hien_tai, "23.pdf")},
    {"Ten": "Đại biểu TÔ HUY VŨ", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "24.pdf")},
    {"Ten": "Đại biểu NGUYỄN VĂN THẮNG", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "25.pdf")},
    {"Ten": "Đại biểu TẠ ĐÌNH THI", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "26.pdf")},
    {"Ten": "Đại biểu NGUYỄN THỊ TUYẾN", "GioiTinh": "Nữ", "File_Name": os.path.join(thu_muc_hien_tai, "27.pdf")},
    {"Ten": "Đại biểu NGUYỄN DUY NGỌC", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "28.pdf")},
    {"Ten": "Đại biểu LÂM THỊ PHƯƠNG THANH", "GioiTinh": "Nữ", "File_Name": os.path.join(thu_muc_hien_tai, "29.pdf")},
    {"Ten": "Đại biểu LÊ NHẬT THÀNH", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "30.pdf")},
    {"Ten": "Đại biểu ĐỖ ĐỨC HỒNG HÀ", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "31.pdf")},
    {"Ten": "Đại biểu NGUYỄN KIM SƠN", "GioiTinh": "Nam", "File_Name": os.path.join(thu_muc_hien_tai, "32.pdf")},
]

# ==========================================
# 4. VẬN HÀNH & XUẤT KHỐI DỮ LIỆU
# ==========================================
print("--- KHỞI ĐỘNG CỖ MÁY PDF ---")
final_data = []

for db in danh_sach_db:
    print(f">> Đang phân tích tọa độ: {db['Ten']}...")
    output = process_local_pdf(db['File_Name'])

    if output:
        stats, raw_text = output
        entry = {**db, **stats}
        entry["Full_Text"] = raw_text
        final_data.append(entry)

if final_data:
    file_excel = os.path.join(thu_muc_hien_tai, "Ket_Qua_GDS_Final.xlsx")
    df = pd.DataFrame(final_data)
    df.to_excel(file_excel, index=False)
    print(f"\n[TRẠNG THÁI: THÀNH CÔNG] Dữ liệu đã được đóng gói tại: {file_excel}")
else:
    print("\n[TRẠNG THÁI: THẤT BẠI] Không thu thập được dữ liệu. Kiểm tra lại định dạng PDF.")
