# QUAN LY DIEM SINH VIEN - STREAMLIT

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="📚",
    layout="wide"
)

# 1. DU LIEU SINH VIEN
data = {
    "Ho_ten": [
        "An", "Binh", "Chi", "Dung", "Ha",
        "Lan", "Minh", "Nam", "Phuc", "Trang"
    ],
    "Chuyen_can": [8, 8.5, 7, 9, 8.5, 7.5, 9, 8, 8.5, 9.5],
    "Giua_ky":    [7.5, 8, 6.5, 9, 8, 7, 9.5, 8, 8, 9],
    "Cuoi_ky":    [8, 8.5, 7, 9.5, 8.5, 7.5, 9, 8.5, 8, 9.5]
}

df = pd.DataFrame(data)

# 2. TINH DIEM TONG KET
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
).round(2)

# 3. XEP LOAI
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 4. TIEU DE WEB APP
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 5. BANG DIEM
st.subheader("Bảng điểm 10 sinh viên")

bang_hien_thi = df.rename(columns={
    "Ho_ten": "Họ tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(bang_hien_thi, use_container_width=True)

# 6. THONG KE
diem_tb = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

c1, c2, c3, c4 = st.columns(4)

c1.metric("Điểm trung bình", f"{diem_tb:.2f}")
c2.metric("Điểm cao nhất", f"{sv_max['Tong_ket']:.2f}")
c3.metric("Điểm thấp nhất", f"{sv_min['Tong_ket']:.2f}")
c4.metric("Số sinh viên đạt", f"{so_sv_dat}/10")

st.write(
    f"Sinh viên cao nhất: **{sv_max['Ho_ten']}** "
    f"({sv_max['Tong_ket']:.2f} điểm)"
)
st.write(
    f"Sinh viên thấp nhất: **{sv_min['Ho_ten']}** "
    f"({sv_min['Tong_ket']:.2f} điểm)"
)

# 7. CHON SINH VIEN
st.subheader("Tra cứu điểm sinh viên")

ten_sv = st.selectbox(
    "Chọn một sinh viên:",
    df["Ho_ten"].tolist()
)

sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write(f"**Họ tên:** {sv['Ho_ten']}")
st.write(f"**Chuyên cần:** {sv['Chuyen_can']}")
st.write(f"**Giữa kỳ:** {sv['Giua_ky']}")
st.write(f"**Cuối kỳ:** {sv['Cuoi_ky']}")
st.write(f"**Tổng kết:** {sv['Tong_ket']:.2f}")
st.write(f"**Xếp loại:** {sv['Xep_loai']}")

# 8. BIEU DO
st.subheader("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df["Ho_ten"], df["Tong_ket"])
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Họ và tên")
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlim(0, 10)
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

# 9. THONG TIN NGUOI TAO
st.divider()
st.caption("Người tạo: Trương Đại Vệ | MSSV: 058208006518")
