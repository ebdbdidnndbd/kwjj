import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Icon(name=ft.Icons.ANDROID, color="green", size=100),
        ft.Text("تطبيقي الأول بـ Flet", size=25, weight="bold"),
        ft.ElevatedButton("أهلاً بك يا حسين!", on_click=lambda _: print("تم الضغط!"))
    )

ft.app(target=main)
