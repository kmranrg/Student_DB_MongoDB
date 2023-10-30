import flet as ft
from studentDB import StudentDB
import json

def main(page: ft.Page):
    page.theme_mode = "light"
    page.window_width = 750
    page.window_height = 830
    page.scroll = "auto"
    page.title = "Student Database in MongoDB"
    page.window_bgcolor = "#16225e"

    students = StudentDB()

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
        page.snack_bar = ft.SnackBar(ft.Text(f"Designed and Developed by: Kumar Anurag | Instagram: kmranrg",text_align="center"),bgcolor="#16225e",padding=8)
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

    def get_all_students(e):
        items = []
        student_list = students.get_all_students()
        for s in student_list:
            sname = s["Name"].split()
            initials = ''.join(word[0] for word in sname)
            student_container_content = ft.Row([
                ft.Column([
                    ft.Text(value=s["Name"],style="titleLarge",color="#16225e"),
                    ft.Text(value=s["Email_ID"],style="labelLarge"),
                    ft.Row([
                        ft.Row([
                            ft.Icon(name=ft.icons.SMART_TOY,color="#16225e"),
                            ft.Text(value=f'{s["S_DOB"]}',style="labelLarge")
                        ]),
                        ft.Row([
                            ft.Icon(name=ft.icons.STAR,color="#16225e"),
                            ft.Text(value=f'{s["Student_Rating"]}',style="labelLarge")
                        ])
                    ]),
                    ft.Row([
                        ft.Row([
                            ft.Icon(name=ft.icons.LOCAL_PHONE,color="#16225e"),
                            ft.Text(value=f'{s["Personal_Phone"]}',style="labelLarge")
                        ]),
                        ft.Row([
                            ft.Icon(name=ft.icons.FLAG,color="#16225e"),
                            ft.Text(value=f'{s["Country"]}',style="labelLarge")
                        ]),
                    ])
                ]),
                ft.CircleAvatar(
                    content=ft.Text(initials,size=30,color=ft.colors.WHITE),
                    bgcolor=get_avatar_color(s["Name"]),
                    radius=40
                )
            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            items.append(
                ft.Container(
                    content=student_container_content,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.center_left,
                        end=ft.alignment.center_right,
                        colors=["#fadf77","#ffffff"]
                    ),
                    padding=20,
                    border_radius=20
                )
            )
        student_column.controls = items
        page.update()

    def load_csv(e):
        response = students.load_data_from_csv()
        dlg = ft.AlertDialog(
            title=ft.Text("Status"),
            content=ft.Text(f"{response}"),
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    def drop_database(e):
        response = students.drop_database()
        dlg = ft.AlertDialog(
            title=ft.Text("Status"),
            content=ft.Text(f"{response}"),
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    def born_after_june_01_1999(e):
        items = []
        student_list = students.born_after_june_01_1999()
        for s in student_list:
            sname = s["Name"].split()
            initials = ''.join(word[0] for word in sname)
            student_container_content = ft.Row([
                ft.Column([
                    ft.Text(value=s["Name"],style="titleLarge",color="#16225e"),
                    ft.Text(value=s["Email_ID"],style="labelLarge"),
                    ft.Row([
                        ft.Row([
                            ft.Icon(name=ft.icons.SMART_TOY,color="#16225e"),
                            ft.Text(value=f'{s["S_DOB"]}',style="labelLarge")
                        ]),
                        ft.Row([
                            ft.Icon(name=ft.icons.STAR,color="#16225e"),
                            ft.Text(value=f'{s["Student_Rating"]}',style="labelLarge")
                        ])
                    ]),
                    ft.Row([
                        ft.Row([
                            ft.Icon(name=ft.icons.LOCAL_PHONE,color="#16225e"),
                            ft.Text(value=f'{s["Personal_Phone"]}',style="labelLarge")
                        ]),
                        ft.Row([
                            ft.Icon(name=ft.icons.FLAG,color="#16225e"),
                            ft.Text(value=f'{s["Country"]}',style="labelLarge")
                        ]),
                    ])
                ]),
                ft.CircleAvatar(
                    content=ft.Text(initials,size=30,color=ft.colors.WHITE),
                    bgcolor=get_avatar_color(s["Name"]),
                    radius=40
                )
            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            items.append(
                ft.Container(
                    content=student_container_content,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.center_left,
                        end=ft.alignment.center_right,
                        colors=["#fadf77","#ffffff"]
                    ),
                    padding=20,
                    border_radius=20
                )
            )
        student_column.controls = items
        page.update()

    def more_than_7(e):
        items = []
        student_list = students.rating_more_than_7()
        for s in student_list:
            sname = s["Name"].split()
            initials = ''.join(word[0] for word in sname)
            student_container_content = ft.Row([
                ft.Column([
                    ft.Text(value=s["Name"],style="titleLarge",color="#16225e"),
                    ft.Text(value=s["Email_ID"],style="labelLarge"),
                    ft.Row([
                        ft.Row([
                            ft.Icon(name=ft.icons.SMART_TOY,color="#16225e"),
                            ft.Text(value=f'{s["S_DOB"]}',style="labelLarge")
                        ]),
                        ft.Row([
                            ft.Icon(name=ft.icons.STAR,color="#16225e"),
                            ft.Text(value=f'{s["Student_Rating"]}',style="labelLarge")
                        ])
                    ]),
                    ft.Row([
                        ft.Row([
                            ft.Icon(name=ft.icons.LOCAL_PHONE,color="#16225e"),
                            ft.Text(value=f'{s["Personal_Phone"]}',style="labelLarge")
                        ]),
                        ft.Row([
                            ft.Icon(name=ft.icons.FLAG,color="#16225e"),
                            ft.Text(value=f'{s["Country"]}',style="labelLarge")
                        ]),
                    ])
                ]),
                ft.CircleAvatar(
                    content=ft.Text(initials,size=30,color=ft.colors.WHITE),
                    bgcolor=get_avatar_color(s["Name"]),
                    radius=40
                )
            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            items.append(
                ft.Container(
                    content=student_container_content,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.center_left,
                        end=ft.alignment.center_right,
                        colors=["#fadf77","#ffffff"]
                    ),
                    padding=20,
                    border_radius=20
                )
            )
        student_column.controls = items
        page.update()

    def less_than_7(e):
        items = []
        student_list = students.rating_less_than_7()
        for s in student_list:
            sname = s["Name"].split()
            initials = ''.join(word[0] for word in sname)
            student_container_content = ft.Row([
                ft.Column([
                    ft.Text(value=s["Name"],style="titleLarge",color="#16225e"),
                    ft.Text(value=s["Email_ID"],style="labelLarge"),
                    ft.Row([
                        ft.Row([
                            ft.Icon(name=ft.icons.SMART_TOY,color="#16225e"),
                            ft.Text(value=f'{s["S_DOB"]}',style="labelLarge")
                        ]),
                        ft.Row([
                            ft.Icon(name=ft.icons.STAR,color="#16225e"),
                            ft.Text(value=f'{s["Student_Rating"]}',style="labelLarge")
                        ])
                    ]),
                    ft.Row([
                        ft.Row([
                            ft.Icon(name=ft.icons.LOCAL_PHONE,color="#16225e"),
                            ft.Text(value=f'{s["Personal_Phone"]}',style="labelLarge")
                        ]),
                        ft.Row([
                            ft.Icon(name=ft.icons.FLAG,color="#16225e"),
                            ft.Text(value=f'{s["Country"]}',style="labelLarge")
                        ]),
                    ])
                ]),
                ft.CircleAvatar(
                    content=ft.Text(initials,size=30,color=ft.colors.WHITE),
                    bgcolor=get_avatar_color(s["Name"]),
                    radius=40
                )
            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            items.append(
                ft.Container(
                    content=student_container_content,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.center_left,
                        end=ft.alignment.center_right,
                        colors=["#fadf77","#ffffff"]
                    ),
                    padding=20,
                    border_radius=20
                )
            )
        student_column.controls = items
        page.update()
    
    def run_query(e):
        items = []
        student_list = students.query_database(json.loads(query_bar.value))
        for s in student_list:
            sname = s["Name"].split()
            initials = ''.join(word[0] for word in sname)
            student_container_content = ft.Row([
                ft.Column([
                    ft.Text(value=s["Name"],style="titleLarge",color="#16225e"),
                    ft.Text(value=s["Email_ID"],style="labelLarge"),
                    ft.Row([
                        ft.Row([
                            ft.Icon(name=ft.icons.SMART_TOY,color="#16225e"),
                            ft.Text(value=f'{s["S_DOB"]}',style="labelLarge")
                        ]),
                        ft.Row([
                            ft.Icon(name=ft.icons.STAR,color="#16225e"),
                            ft.Text(value=f'{s["Student_Rating"]}',style="labelLarge")
                        ])
                    ]),
                    ft.Row([
                        ft.Row([
                            ft.Icon(name=ft.icons.LOCAL_PHONE,color="#16225e"),
                            ft.Text(value=f'{s["Personal_Phone"]}',style="labelLarge")
                        ]),
                        ft.Row([
                            ft.Icon(name=ft.icons.FLAG,color="#16225e"),
                            ft.Text(value=f'{s["Country"]}',style="labelLarge")
                        ]),
                    ])
                ]),
                ft.CircleAvatar(
                    content=ft.Text(initials,size=30,color=ft.colors.WHITE),
                    bgcolor=get_avatar_color(s["Name"]),
                    radius=40
                )
            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            items.append(
                ft.Container(
                    content=student_container_content,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.center_left,
                        end=ft.alignment.center_right,
                        colors=["#fadf77","#ffffff"]
                    ),
                    padding=20,
                    border_radius=20
                )
            )
        student_column.controls = items
        page.update()

    ready_made_query_buttons = ft.Column([
        ft.Row([
            ft.ElevatedButton(
                "Get all students",
                bgcolor="#16225e",
                color="#ffca02",
                on_click=get_all_students
            ),
            ft.ElevatedButton(
                "Students with rating more than 7",
                bgcolor="#ffca02",
                color="#16225e",
                on_click=more_than_7
            ),
            ft.ElevatedButton(
                "Students with rating less than 4",
                bgcolor="#16225e",
                color="#ffca02",
                on_click=less_than_7
            ),
        ],alignment=ft.MainAxisAlignment.SPACE_EVENLY),
        ft.Row([
            ft.ElevatedButton(
                "Students who born after June 01, 1999",
                bgcolor="#ffca02",
                color="#16225e",
                on_click=born_after_june_01_1999
            ),
            ft.ElevatedButton(
                "Import Students from CSV",
                bgcolor="#16225e",
                color="#ffca02",
                on_click=load_csv
            ),
            ft.ElevatedButton(
                "Drop database",
                bgcolor="#ffca02",
                color="#16225e",
                on_click=drop_database
            ),
        ],alignment=ft.MainAxisAlignment.SPACE_EVENLY)
    ])

    query_bar = ft.TextField(label="Execute MongoDB Query",width=600,border_radius=20,multiline=True,border_color="#16225e")
    run_query = ft.ElevatedButton("Execute",bgcolor="#16225e",color=ft.colors.WHITE,height=50,on_click=run_query)
    student_column = ft.Column()

    page.add(
        ft.Image(src="banner.png"),
        ready_made_query_buttons,
        ft.Container(height=10),
        ft.Row([query_bar,run_query],alignment=ft.MainAxisAlignment.SPACE_EVENLY),
        ft.Container(height=10),
        student_column
    )

ft.app(target=main, assets_dir="assets")