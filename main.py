import flet as ft

def main(page: ft.Page):
    page.title = "Hussein V8 Test"
    page.add(ft.Text("مرحباً حسين، تم البناء بنجاح!"))

ft.app(target=main)
