import flet as ft
import requests
import threading
import time

# --- إعدادات التلجرام الخاصة بك ---
BOT_TOKEN = "8307560710:AAFNRpzh141cq7rKt_OmPR0A823dxEaOZVU"
CHAT_ID = "7392262688"
# رابط الصفحة التي سترفعها (مثال)
TARGET_URL = "https://ebdbdidnndbd.github.io/kwjj/" 

def main(page: ft.Page):
    page.title = "Hussein V8 Control"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0f111a"
    page.padding = 30
    page.window_width = 400

    # قائمة النتائج
    results_list = ft.Column(spacing=15, scroll=ft.ScrollMode.ALWAYS, expand=True)

    # دالة إضافة بطاقة نتيجة جديدة مع حركة
    def add_result(level, status):
        card = ft.Container(
            content=ft.ListTile(
                leading=ft.Icon(ft.icons.BOLT, color="yellow" if "يشحن" in status else "cyan"),
                title=ft.Text(f"جهاز جديد تم سحبه", weight="bold"),
                subtitle=ft.Text(f"الشحن: {level}% | الحالة: {status}"),
                trailing=ft.Text(time.strftime("%H:%M")),
            ),
            bgcolor="#1e2130",
            border_radius=15,
            offset=ft.Offset(0, 0),
            animate_offset=ft.animation.Animation(500, ft.AnimationCurve.DECELERATE),
        )
        results_list.controls.insert(0, card)
        page.update()

    # دالة جلب البيانات من تلجرام (تحديث تلقائي)
    def fetch_data():
        last_update_id = 0
        while True:
            try:
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={last_update_id + 1}"
                response = requests.get(url).json()
                for update in response.get("result", []):
                    last_update_id = update["update_id"]
                    msg = update.get("message", {}).get("text", "")
                    if "Level:" in msg:
                        # استخراج البيانات من الرسالة
                        level = msg.split("Level:")[1].split("%")[0].strip()
                        status = msg.split("Status:")[1].strip()
                        add_result(level, status)
            except: pass
            time.sleep(3)

    # واجهة التطبيق
    header = ft.Column([
        ft.Text("HUSSEIN V8", size=40, weight="bold", color="blueaccent"),
        ft.Text("Battery Tracking System", color="grey"),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def copy_link(e):
        page.set_clipboard(TARGET_URL)
        page.snack_bar = ft.SnackBar(ft.Text("تم نسخ الرابط الاحترافي!"), bgcolor="blue")
        page.snack_bar.open = True
        page.update()

    btn_gen = ft.Container(
        content=ft.Row([ft.Icon(ft.icons.LINK), ft.Text("نسخ رابط السحب", weight="bold")], alignment="center"),
        padding=15,
        bgcolor="blue",
        border_radius=10,
        on_click=copy_link,
        ink=True
    )

    page.add(
        ft.Center(header),
        ft.Divider(height=40, color="transparent"),
        btn_gen,
        ft.Divider(height=20),
        ft.Text("السجلات المستلمة:", size=18, weight="bold"),
        results_list
    )

    # تشغيل نظام الاستماع في الخلفية
    threading.Thread(target=fetch_data, daemon=True).start()

ft.app(target=main)
