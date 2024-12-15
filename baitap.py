import tkinter as tk
from tkinter import ttk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Thông tin nhân viên")
root.geometry("650x250")

# Thêm tiêu đề chính
title_label = tk.Label(root, text="Thông tin nhân viên", font=("Arial", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=6, pady=10, sticky="w")

# Các checkbox phía trên
chk_khachhang = tk.Checkbutton(root, text="Là khách hàng")
chk_khachhang.grid(row=0, column=1, padx=5, sticky="w")

chk_nhacungcap = tk.Checkbutton(root, text="Là nhà cung cấp")
chk_nhacungcap.grid(row=0, column=2, padx=5, sticky="w")

# Mã nhân viên
tk.Label(root, text="Mã *").grid(row=1, column=0, padx=5, sticky="w")
entry_ma = tk.Entry(root, width=15)
entry_ma.insert(0, "CTTRUNG")
entry_ma.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Tên nhân viên
tk.Label(root, text="Tên *").grid(row=1, column=2, padx=5, sticky="w")
entry_ten = tk.Entry(root, width=30)
entry_ten.insert(0, "Cao Thành Trung")
entry_ten.grid(row=1, column=3, padx=5, pady=5, sticky="w")

# Đơn vị
tk.Label(root, text="Đơn vị *").grid(row=2, column=0, padx=5, sticky="w")
combo_donvi = ttk.Combobox(root, values=["Phân xưởng que hàn", "Phân xưởng khác"])
combo_donvi.current(0)
combo_donvi.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Ngày sinh
tk.Label(root, text="Ngày sinh").grid(row=2, column=2, padx=5, sticky="w")
entry_ngaysinh = tk.Entry(root, width=15)
entry_ngaysinh.grid(row=2, column=3, padx=5, pady=5, sticky="w")

# Giới tính
tk.Label(root, text="Giới tính").grid(row=3, column=0, padx=5, sticky="w")
gender_frame = tk.Frame(root)
gender_frame.grid(row=3, column=1, sticky="w")
gender_var = tk.StringVar(value="Nam")
tk.Radiobutton(gender_frame, text="Nam", variable=gender_var, value="Nam").pack(side="left")
tk.Radiobutton(gender_frame, text="Nữ", variable=gender_var, value="Nữ").pack(side="left")

# Số CMND
tk.Label(root, text="Số CMND").grid(row=3, column=2, padx=5, sticky="w")
entry_cmnd = tk.Entry(root, width=15)
entry_cmnd.grid(row=3, column=3, padx=5, pady=5, sticky="w")

# Ngày cấp
tk.Label(root, text="Ngày cấp").grid(row=4, column=0, padx=5, sticky="w")
entry_ngaycap = tk.Entry(root, width=15)
entry_ngaycap.grid(row=4, column=1, padx=5, pady=5, sticky="w")

# Nơi cấp
tk.Label(root, text="Nơi cấp").grid(row=4, column=2, padx=5, sticky="w")
entry_noicap = tk.Entry(root, width=30)
entry_noicap.grid(row=4, column=3, padx=5, pady=5, sticky="w")

# Chức danh
tk.Label(root, text="Chức danh").grid(row=5, column=0, padx=5, sticky="w")
entry_chucdanh = tk.Entry(root, width=30)
entry_chucdanh.insert(0, "Nhân viên")
entry_chucdanh.grid(row=5, column=1, padx=5, pady=5, sticky="w")

# Chạy vòng lặp chính
root.mainloop()
