
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Tao du lieu 10 sinh vien
data = {
    "Ho_ten": [
        "An", "Binh", "Chi", "Dung", "Ha",
        "Lan", "Minh", "Nam", "Phuc", "Trang"
    ],
    "Chuyen_can": [8, 9, 7, 9.5, 8, 7.5, 9, 8, 8.5, 9.5],
    "Giua_ky": [7, 8.5, 6.5, 9, 7.5, 6, 8, 7.5, 8, 9],
    "Cuoi_ky": [7.5, 8, 6, 9.5, 7, 6.5, 8.5, 7, 7.5, 9]
}

df = pd.DataFrame(data)

# 2. Tinh diem tong ket
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
).round(2)

# 3. Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 4. Cau hinh trang web
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 5. Hien thi bang diem
st.header("1. Bảng điểm sinh viên")

bang = df.rename(columns={
    "Ho_ten": "Họ tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(bang, use_container_width=True)

# 6. Thong ke
st.header("2. Thống kê")

st.metric("Điểm trung bình lớp", f"{df['Tong_ket'].mean():.2f}")

sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]

col1, col2 = st.columns(2)

col1.write(
    f"**Điểm cao nhất:** {sv_max['Ho_ten']} "
    f"({sv_max['Tong_ket']:.2f})"
)

col2.write(
    f"**Điểm thấp nhất:** {sv_min['Ho_ten']} "
    f"({sv_min['Tong_ket']:.2f})"
)

st.write("**Số sinh viên đạt từ 5 điểm:**",
         int((df["Tong_ket"] >= 5).sum()))

# 7. Chon sinh vien
st.header("3. Tra cứu sinh viên")

ten = st.selectbox("Chọn sinh viên:", df["Ho_ten"].tolist())
sv = df[df["Ho_ten"] == ten].iloc[0]

st.write("**Họ tên:**", sv["Ho_ten"])
st.write("**Điểm chuyên cần:**", sv["Chuyen_can"])
st.write("**Điểm giữa kỳ:**", sv["Giua_ky"])
st.write("**Điểm cuối kỳ:**", sv["Cuoi_ky"])
st.write("**Điểm tổng kết:**", sv["Tong_ket"])
st.write("**Xếp loại:**", sv["Xep_loai"])

# 8. Ve bieu do
st.header("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 9. Thong tin nguoi tao
st.divider()
st.caption("Người tạo: Châu Kim Duy")
st.caption("MSSV: 052208012882")
