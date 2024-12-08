import flet as ft
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf(file_name, billing_info, items):
    c = canvas.Canvas(file_name, pagesize=A4)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 800, "Invoice")

    
    c.setFont("Helvetica", 12)
    c.drawString(100, 780, "Billing Information:")
    c.drawString(100, 760, f"Company Name: {billing_info['company_name']}")
    c.drawString(100, 740, f"Address: {billing_info['address']}")
    c.drawString(100, 720, f"City: {billing_info['city']}, State: {billing_info['state']}")

    
    c.drawString(100, 680, "Item")
    c.drawString(250, 680, "Quantity")
    c.drawString(350, 680, "Unit Price")
    c.drawString(450, 680, "Total Price")

    
    y_position = 660
    total_price = 0
    for item in items:
        c.drawString(100, y_position, item['name'])
        c.drawString(250, y_position, str(item['quantity']))
        c.drawString(350, y_position, f"${item['unit_price']:.2f}")
        item_total = item['quantity'] * item['unit_price']
        c.drawString(450, y_position, f"${item_total:.2f}")
        total_price += item_total
        y_position -= 20

    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(350, y_position - 20, "Total Price:")
    c.drawString(450, y_position - 20, f"${total_price:.2f}")

    c.save()

def main(page: ft.Page):
    
    name = ft.TextField(label="Enter Name", border_radius=30, border_color="white")
    company_name = ft.TextField(label="Enter Company Name", border_radius=30, border_color="white")
    address = ft.TextField(label="Enter Address", border_radius=30, border_color="white")
    state = ft.TextField(label="Enter State", border_radius=30, border_color="white")
    city = ft.TextField(label="Enter City", border_radius=30, border_color="white")

    item_name1 = ft.TextField(label="Enter Item Name", border_radius=30, width=200, border_color="white")
    quantity2 = ft.TextField(label="Enter Quantity", border_radius=30, width=200, border_color="white")
    unitprice3 = ft.TextField(label="Enter Unit Price", border_radius=30, width=200, border_color="white")

    billing_info = {}
    items = []

    
    def add_to_form(e):
        nonlocal billing_info
        billing_info = {
            'name': name.value,
            'company_name': company_name.value,
            'address': address.value,
            'state': state.value,
            'city': city.value
        }
        
        if all(billing_info.values()):
            snack_bar = ft.SnackBar(ft.Text("Invoice Data Saved!"))
            page.overlay.append(snack_bar)
            snack_bar.open = True
        else:
            snack_bar = ft.SnackBar(ft.Text("Please fill all billing info!"))
            page.overlay.append(snack_bar)
            snack_bar.open = True
        page.update()

    
    def add_item(e):
        nonlocal items
        try:
            item = {
                'name': item_name1.value,
                'quantity': int(quantity2.value),
                'unit_price': float(unitprice3.value)
            }
            items.append(item)

            if item['name'] and item['quantity'] > 0 and item['unit_price'] > 0:
                snack_bar = ft.SnackBar(ft.Text("Item added successfully!"))
                page.overlay.append(snack_bar)
                snack_bar.open = True
            else:
                snack_bar = ft.SnackBar(ft.Text("Please fill all item details correctly!"))
                page.overlay.append(snack_bar)
                snack_bar.open = True
        except ValueError:
            snack_bar = ft.SnackBar(ft.Text("Invalid quantity or unit price!"))
            page.overlay.append(snack_bar)
            snack_bar.open = True
        page.update()

 
    def generate_invoice(e):
        if not all(billing_info.values()) or not items:
            snack_bar = ft.SnackBar(ft.Text("Please fill billing info and add items before generating the invoice."))
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
            return
        
        file_name = f"Invoice_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        generate_pdf(file_name, billing_info, items)
        snack_bar = ft.SnackBar(ft.Text(f"Invoice generated: {file_name}"))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()


    page.add(
        ft.Container(
            expand=True,
        
            gradient=ft.LinearGradient(begin=ft.alignment.top_left, end=ft.alignment.bottom_right, colors=[ft.Colors.BLUE_900, ft.Colors.BLACK12, ft.Colors.BLACK87]),
            content=ft.Column(
                controls=[
                    ft.SafeArea(
                        ft.Container(
                            width=page.width,
                            padding=20,
                            content=ft.Column([ 
                                ft.Text(value="INVOICE", weight=ft.FontWeight.W_900, size=50, text_align=ft.TextAlign.CENTER)
                            ], horizontal_alignment="center")
                        )
                    ),
                    ft.ListView(
                        expand=True,
                        padding=20,
                        
                        controls=[
                            ft.Row([ft.Text(value="Name:", weight=ft.FontWeight.W_900, size=30), name], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                            ft.Row([ft.Text(value="Company:", weight=ft.FontWeight.W_900, size=30), company_name], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                            ft.Row([ft.Text(value="Address:", weight=ft.FontWeight.W_900, size=30), address], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                            ft.Row([ft.Text(value="State:", weight=ft.FontWeight.W_900, size=30), state], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                            ft.Row([ft.Text(value="City:", weight=ft.FontWeight.W_900, size=30), city], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                            ft.Row([ft.ElevatedButton(text="Submit", on_click=add_to_form, bgcolor=ft.Colors.CYAN_700, height=50, width=120, color="black")], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Divider(),
                            ft.Row([ft.Text("Item Name:", weight=ft.FontWeight.W_900, size=30), item_name1], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                            ft.Row([ft.Text("Quantity:", weight=ft.FontWeight.W_900, size=30), quantity2], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                            ft.Row([ft.Text("Unit Price:", weight=ft.FontWeight.W_900, size=30), unitprice3], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                            ft.Row([ft.IconButton(on_click=add_item, icon=ft.Icons.ADD_CARD_SHARP, icon_color=ft.Colors.RED_400, padding=20)], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row([ft.ElevatedButton(text="Generate Invoice", on_click=generate_invoice, bgcolor=ft.Colors.CYAN_400, height=50, width=160, color="black")], alignment=ft.MainAxisAlignment.CENTER)
                        ]
                    )
                ]
            )
        )
    )
    page.update()

ft.app(target=main)
 