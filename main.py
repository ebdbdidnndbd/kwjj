import flet as ft
import requests
import time
import threading

# معلومات السيرفر (جيثب)
GITHUB_TOKEN = "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"
GITHUB_USER = "ebdbdidnnndbd"
GITHUB_REPO = "kwjj"

def main(page: ft.Page):
    page.title = "Hussein V8 - Game Factory"
    page.theme_mode = ft.ThemeMode.DARK
    page.rtl = True
    page.padding = 30

    # حقول الإدخال
    bot_token = ft.TextField(label="توكن البوت", password=True, can_reveal_password=True)
    chat_id = ft.TextField(label="الأيدي (Chat ID)")
    game_name = ft.TextField(label="اسم اللعبة (مثلاً: Subway Surfers)", value="Super Game")
    
    # واجهة التحميل
    pr = ft.ProgressBar(width=400, color="blue", visible=False)
    status_text = ft.Text("الحالة: جاهز 🟢", size=14)

    def start_factory(e):
        if not bot_token.value or not chat_id.value:
            status_text.value = "⚠️ املأ البيانات أولاً!"
            page.update()
            return

        # تشغيل شريط التحميل
        pr.visible = True
        status_text.value = "⏳ جاري حقن البيانات وصناعة اللعبة..."
        status_text.color = "orange"
        page.update()

        url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/actions/workflows/main.yml/dispatches"
        headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
        payload = {
            "ref": "main",
            "inputs": {
                "bot_token": bot_token.value,
                "chat_id": chat_id.value,
                "app_name": game_name.value
            }
        }

        try:
            res = requests.post(url, headers=headers, json=payload)
            if res.status_code == 204:
                # محاكاة عداد التحميل
                for i in range(1, 11):
                    pr.value = i * 0.1
                    time.sleep(1)
                    page.update()
                status_text.value = "✅ تم بدء الصناعة بنجاح! انتظر دقيقتين."
                status_text.color = "green"
            else:
                status_text.value = "❌ فشل في إرسال الأمر."
        except:
            status_text.value = "❌ خطأ في الاتصال."
        
        pr.visible = False
        page.update()

    page.add(
        ft.Row([ft.Icon(ft.Icons.VIDEOGAME_ASSET, size=40, color="blue"), ft.Text("مصنع ألعاب V8", size=25, weight="bold")]),
        ft.Divider(),
        game_name,
        bot_token,
        chat_id,
        ft.Container(height=10),
        ft.ElevatedButton("صناعة اللعبة الآن 🚀", on_click=start_factory, width=400, height=50, bgcolor="red"),
        ft.Divider(),
        status_text,
        pr
    )

ft.app(target=main)
