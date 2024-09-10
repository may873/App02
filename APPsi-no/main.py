import flet as ft


def main(page: ft.Page):
    page.title="¿Me perdonas?"
    page.bgcolor="pink"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER 
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    lbl1=ft.Text("¿Me perdonas?",
                style=ft.TextStyle(size=40,weight="blod"))
    img1=ft.Image(src="triste.png",width=200,height=200)
    btnSi=ft.ElevatedButton("Si",
                            color="black",
                            width=100,
                            height=50
                            )
    btnNo=ft.ElevatedButton("No",
                            color="red",
                            width=100,
                            height=50
                            )
    def no(e):
        btnSi.width+=30
        btnNo.height+=10
        page.update()
        
    def si(e):
        img1.src="feliz.png"
        page.update()
        
    btnNo.on_click=no
    btnSi.on_click=si
    page.add(
        ft.Column(
            [
                lbl1,
                img1,
                ft.Row(
                    [btnSi,btnNo],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )



ft.app(main)
