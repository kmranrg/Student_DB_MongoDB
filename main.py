import flet as ft

def main(page: ft.Page):
    page.theme_mode = "light"
    page.window_width = 750
    page.window_height = 830
    page.scroll = "auto"
    page.title = "Student Database in MongoDB"
    page.window_bgcolor = "#16225e"

    def get_avatar_color(user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]
    
    def devInfo(e):
        page.snack_bar = ft.SnackBar(ft.Text(f"Designed and Developed by: Kumar Anurag | Instagram: kmranrg",text_align="center"),bgcolor="#16225e")
        page.snack_bar.open = True
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.SCHOOL,color="#ffca02",size=40),
        leading_width=60,
        title=ft.Text("SmartGurucool",color=ft.colors.WHITE),
        center_title=False,
        bgcolor="#16225e",
        actions=[
            ft.IconButton(ft.icons.NOTIFICATIONS,icon_color=ft.colors.WHITE),
            ft.IconButton(ft.icons.PERSON,icon_color=ft.colors.WHITE,on_click=devInfo),
        ],
    )

    ready_made_query_buttons = ft.Column([
        ft.Row([
            ft.ElevatedButton(
                "Get all students",
                bgcolor="#16225e",
                color="#ffca02"
            ),
            ft.ElevatedButton(
                "Students with rating more than 7",
                bgcolor="#ffca02",
                color="#16225e"
            ),
            ft.ElevatedButton(
                "Students with rating less than 4",
                bgcolor="#16225e",
                color="#ffca02"
            ),
        ],alignment=ft.MainAxisAlignment.SPACE_EVENLY),
        ft.Row([
            ft.ElevatedButton(
                "Students who joined after June 01, 1999",
                bgcolor="#ffca02",
                color="#16225e"
            ),
            ft.ElevatedButton(
                "Import Students from CSV",
                bgcolor="#16225e",
                color="#ffca02"
            ),
            ft.ElevatedButton(
                "Drop database",
                bgcolor="#ffca02",
                color="#16225e"
            ),
        ],alignment=ft.MainAxisAlignment.SPACE_EVENLY)
    ])

    query_bar = ft.TextField(label="MongoDB Query",width=600,hint_text="execute your mongodb query here...",border_radius=20,multiline=True,border_color="#16225e")
    run_query = ft.ElevatedButton("Execute",bgcolor="#16225e",color=ft.colors.WHITE,height=50)

    student_container_content = ft.Row([
        ft.Column([
            ft.Text(value='Aayush Mehta',style="titleLarge",color="#16225e"),
            ft.Text(value='aayush.mehta@smartgurucool.com',style="labelLarge"),
        ]),
        ft.CircleAvatar(
            content=ft.Text("AM",size=20,color=ft.colors.WHITE),
            bgcolor=get_avatar_color("aayush"),
            radius=30
        )
    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    student_container = ft.Container(
        content=student_container_content,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#fadf77","#ffffff"]
        ),
        padding=20,
        border_radius=20
    )

    page.add(
        ft.Image(src="banner.png"),
        ready_made_query_buttons,
        ft.Container(height=10),
        ft.Row([query_bar,run_query],alignment=ft.MainAxisAlignment.SPACE_EVENLY),
        ft.Container(height=10),
        student_container,
        student_container,
        student_container,
        student_container,
        student_container,
        student_container,
        student_container
    )

ft.app(target=main, assets_dir="assets")