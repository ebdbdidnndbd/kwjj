import flet as ft
import requests

# معلوماتك مدمجة وجاهزة
APP_PASSWORD = "1234"
GITHUB_TOKEN = "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"
GITHUB_USER = "ebdbdidnnndbd"
GITHUB_REPO = "kwjj"

def main(page: ft.Page):
    page.title = "Hussein C2 Controller"
    page.theme_mode = ft.ThemeMode.DARK
    page.rtl = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def show_panel():
        page.controls.clear()
        status = ft.Text("النظام متصل بالسيرفر 🟢", color="green", weight="bold")
        link_field = ft.TextField(label="رابط التحميل المباشر", read_only=True, visible=False)

        def start_factory(e):
            status.value = "⏳ جاري إرسال أمر التصنيع..."
            page.update()
            url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/actions/workflows/main.yml/dispatches"
            headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
            res = requests.post(url, headers=headers, json={"ref": "main"})
            if res.status_code == 204:
                status.value = "✅ المصنع بدأ العمل! انتظر دقيقتين."
            else:
                status.value = "❌ فشل الاتصال بالسيرفر."
            page.update()

        def fetch_link(e):
            url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/releases/latest"
            res = requests.get(url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
            if res.status_code == 200:
                assets = res.json().get("assets", [])
                if assets:
                    link_field.value = assets[0]["browser_download_url"]
                    link_field.visible = True
                    status.value = "🎉 تم جلب الرابط بنجاح!"
            page.update()

        page.add(
            ft.Text("لوحة تحكم حسين - أندرويد", size=25, weight="bold"),
            ft.Divider(),
            ft.ElevatedButton("1. تشغيل مصنع التطبيقات 🚀", on_click=start_factory, width=400, height=50, bgcolor="red"),
            ft.ElevatedButton("2. جلب رابط الـ APK 📥", on_click=fetch_link, width=400, height=50, bgcolor="green"),
            status, link_field
        )
        page.update()

    def login(e):
        if pwd.value == APP_PASSWORD: show_panel()
        else: page.snack_bar = ft.SnackBar(ft.Text("خطأ!")); page.snack_bar.open = True; page.update()

    pwd = ft.TextField(label="رمز الدخول السري", password=True, can_reveal_password=True)
    page.add(ft.Icon(ft.Icons.SECURITY, size=50), ft.Text("نظام التحكم المشفر"), pwd, ft.ElevatedButton("دخول", on_click=login))

ft.app(target=main)
