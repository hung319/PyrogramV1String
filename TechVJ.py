
from pyrogram import Client

api_id = 6897064
api_hash = "206c2035a8dc342ab70421ea4094ac49"

try:
    os.remove("techvj.session")
except:
    pass

with Client("techvj", api_id=api_id, api_hash=api_hash) as app:
    session = f"**🥀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 » 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 💞**\n\n`{app.export_session_string()}`\n\n**💥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲: [H4RS] ✨**"
    app.send_message("me", session, disable_web_page_preview=True)

print(f"✅ String Session Has 🌟 Been Sent\nTo Your 🔥 Saved Message ✨ ...")

try:
    os.remove("techvj.session")
except:
    pass
