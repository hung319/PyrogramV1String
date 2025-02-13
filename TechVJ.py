import os
from pyrogram import Client

api_id = 6897064
api_hash = "206c2035a8dc342ab70421ea4094ac49"

# Danh sách các data center Telegram
data_centers = {
    1: "149.154.175.50:443",  # DC1 (Moscow)
    2: "149.154.167.51:443",  # DC2 (St. Petersburg)
    3: "149.154.175.100:443", # DC3 (Amsterdam)
    4: "149.154.167.91:443",  # DC4 (Miami)
    5: "149.154.171.5:443"    # DC5 (Singapore)
}

# Cho phép người dùng chọn Data Center
print("Chọn Data Center:")
for dc_id, address in data_centers.items():
    print(f"{dc_id}: {address}")

try:
    dc_choice = int(input("Nhập số tương ứng với Data Center: "))
    if dc_choice not in data_centers:
        raise ValueError("Chọn một giá trị hợp lệ từ danh sách.")
except ValueError as e:
    print(f"Lỗi: {e}. Sử dụng mặc định DC1.")
    dc_choice = 1

proxy_address = data_centers[dc_choice]
ip, port = proxy_address.split(":")

# Xóa session cũ nếu tồn tại
try:
    os.remove("techvj.session")
except FileNotFoundError:
    pass

# Tạo client với proxy
with Client(
    "techvj",
    api_id=api_id,
    api_hash=api_hash,
    proxy={"hostname": ip, "port": int(port), "scheme": "socks5"}
) as app:
    session = f"**🥀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 » 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 💞**\n\n`{app.export_session_string()}`\n\n**💥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲: [H4RS] ✨**"
    app.send_message("me", session, disable_web_page_preview=True)

print(f"✅ String Session Has 🌟 Been Sent\nTo Your 🔥 Saved Message ✨ ...")

# Xóa session sau khi sử dụng
try:
    os.remove("techvj.session")
except FileNotFoundError:
    pass
