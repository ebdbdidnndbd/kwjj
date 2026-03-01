import flet as ft

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "تطبيق حسين"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # عناصر الواجهة
    title_text = ft.Text("تم بناء التطبيق بنجاح! 🎉", size=25, color="green", weight="bold")
    status_text = ft.Text("هذا أول تطبيق يشتغل بدون مشاكل", size=18)
    
    def on_click(e):
        status_text.value = "أهلاً بك يا بطل في عالم البرمجة!"
        status_text.color = "blue"
        page.update()

    btn = ft.ElevatedButton("اضغط هنا للتجربة", on_click=on_click, icon=ft.Icons.CHECK_CIRCLE)
    
    # إضافة العناصر للشاشة
    page.add(title_text, status_text, btn)

ft.app(target=main)
