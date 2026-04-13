from fpdf import FPDF, Align
pdf = FPDF(orientation='P', unit='mm', format=(210, 297))
pdf.add_page()

pdf.image("shirtificate.png", x=Align.C, y=50, w=100)
pdf.set_font("Arial", size=35)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(0, 10)
pdf.cell(0, 10, txt="CS50 Shirtificate", ln=True, align = "C")

pdf.set_font("Arial", size=16)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, 90)
name = input("Name:")
pdf.cell(0, 10, txt=(f"{name} took CS50"), ln=True, align = "C")

pdf.output("shirtificate.pdf")
