import flet as ft
import subprocess, urllib.parse, datetime

def main(page: ft.Page):
    page.title = "RANI AI - Personal Assistant"
    page.bgcolor = "#050A18"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    status_text = ft.Text("RANI Ready hai Ram Mohan Boss!", color="#00F0FF", size=18, weight="bold")
    chat_box = ft.Text("Niche mic dabakar ya likhkar hukm dein...", color="white", size=15, text_align=ft.TextAlign.CENTER)
    cmd_input = ft.TextField(hint_text="Yahan apna command likhein...", bgcolor="#101B33", color="white", border_color="#00F0FF")

    def run_command(e):
        q = cmd_input.value.strip().lower()
        if not q:
            return
        cmd_input.value = ""
        if "youtube" in q:
            search = q.replace("youtube", "").replace("kholo", "").replace("open", "").strip()
            url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(search)}" if search else "https://www.youtube.com"
            page.launch_url(url)
            chat_box.value = f"RANI: YouTube par {search if search else 'home'} khol diya hai Boss!"
        elif "instagram" in q or "reel" in q:
            page.launch_url("https://www.instagram.com/reels/")
            chat_box.value = "RANI: Instagram Reels chalu kar rahi hoon Boss!"
        elif "amazon" in q:
            item = q.replace("amazon", "").replace("par", "").replace("dikhao", "").strip()
            page.launch_url(f"https://www.amazon.in/s?k={urllib.parse.quote(item)}")
            chat_box.value = f"RANI: Amazon par {item} dikha rahi hoon!"
        elif "time" in q:
            now = datetime.datetime.now().strftime("%I:%M %p")
            chat_box.value = f"RANI: Boss, abhi {now} ho rahe hain."
        else:
            chat_box.value = f"RANI: Ji Boss, '{q}' par kaam ho raha hai!"
        page.update()

    avatar = ft.Container(
        content=ft.Icon(ft.Icons.GRAPHIC_EQ, size=70, color="#00F0FF"),
        width=140, height=140,
        border_radius=70,
        bgcolor="#0B1938",
        border=ft.border.all(3, "#00F0FF"),
        alignment=ft.alignment.center
    )

    send_btn = ft.ElevatedButton("Hukm Bhejein", on_click=run_command, bgcolor="#00F0FF", color="black")

    page.add(
        status_text,
        ft.Container(height=20),
        avatar,
        ft.Container(height=20),
        chat_box,
        ft.Container(height=20),
        cmd_input,
        send_btn
    )

ft.app(target=main)
