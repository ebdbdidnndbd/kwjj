import flet as ft
import requests

# ==========================================
# تم دمج معلوماتك بنجاح بواسطة الذكاء الاصطناعي
# ==========================================
APP_PASSWORD = "1234"
GITHUB_TOKEN = "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"
GITHUB_USER = "ebdbdidnndbd"
GITHUB_REPO = "kwjj"

def main(page: ft.Page):
    page.title = "نظام حسين المغلق"
    page.theme_mode = ft.ThemeMode.DARK
    page.rtl = True
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def show_control_panel():
        page.controls.clear()
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.horizontal_alignment = ft.CrossAxisAlignment.START

        status_text = ft.Text("الحالة: النظام متصل وجاهز 🟢", color="blue", size=16, weight="bold")
        link_text = ft.TextField(label="رابط التطبيق المستهدف (APK)", read_only=True, visible=False, suffix_icon=ft.Icons.COPY)

        def trigger_build(e):
            headers = {"Accept": "application/vnd.github.v3+json", "Authorization": f"token {GITHUB_TOKEN}"}
            url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/actions/workflows/main.yml/dispatches"
            data = {"ref": "main"}
            
            status_text.value = "⏳ جاري إرسال أمر التصنيع للسيرفر..."
            status_text.color = "orange"
            link_text.visible = False
            page.update()
            
            try:
                res = requests.post(url, headers=headers, json=data)
                if res.status_code == 204:
                    status_text.value = "✅ السيرفر استلم الأمر! جاري صناعة التطبيق (انتظر دقيقتين)."
                    status_text.color = "green"
                else:
                    status_text.value = f"❌ خطأ: السيرفر رفض الأمر. تأكد من صحة التوكن."
                    status_text.color = "red"
            except Exception as ex:
                status_text.value = "❌ خطأ في الاتصال بالإنترنت!"
                status_text.color = "red"
            page.update()

        def get_link(e):
            headers = {"Accept": "application/vnd.github.v3+json", "Authorization": f"token {GITHUB_TOKEN}"}
            url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/releases/latest"
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
            ft.Row([ft.Icon(ft.Icons.ADMIN_PANEL_SETTINGS, size=40, color="blue"), ft.Text("لوحة تحكم C2", size=28, weight="bold")]),
            ft.Divider(),
            ft.Text(f"👤 متصل بسيرفر: {GITHUB_USER}/{GITHUB_REPO}", color="grey", size=14),
            ft.Container(height=20),
            ft.ElevatedButton("1. اصنع التطبيق المستهدف 🚀", on_click=trigger_build, bgcolor="red", color="white", width=400, height=50),
            ft.Container(height=10),
            ft.ElevatedButton("2. جلب رابط التحميل 📥", on_click=get_link, bgcolor="green", color="white", width=400, height=50),
            ft.Divider(),
            status_text,
            link_text
        )
        page.update()

    def check_password(e):
        if pass_input.value == APP_PASSWORD:
            show_control_panel()
        else:
            error_text.value = "❌ كلمة المرور غير صحيحة!"
            page.update()

    pass_input = ft.TextField(label="أدخل كلمة المرور لفتح التطبيق", password=True, can_reveal_password=True, text_align=ft.TextAlign.CENTER, width=300)
    error_text = ft.Text("", color="red", size=16)
    login_btn = ft.ElevatedButton("تسجيل الدخول 🔐", on_click=check_password, bgcolor="blue", color="white", width=200, height=45)

    page.add(
        ft.Icon(ft.Icons.LOCK, size=80, color="blue"),
        ft.Text("نظام حسين المغلق", size=24, weight="bold"),
        ft.Text("النظام محمي، يرجى إدخال رمز المرور.", color="grey", size=14),
        ft.Container(height=20),
        pass_input,
        login_btn,
        error_text
    )

ft.app(target=main)
