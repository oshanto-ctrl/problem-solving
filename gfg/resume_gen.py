# Fixing the encoding issue by removing all non-ASCII characters
def ascii_safe(text):
    return text.encode("ascii", "ignore").decode()

# Rewriting PDF generation with only ASCII characters
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, ascii_safe("Md. Rejoan Siddiky"), ln=True, align="C")
pdf.set_font("Arial", "", 10)
pdf.cell(0, 8, ascii_safe("East Shewrapara, Karful, Mirpur, Dhaka - 1216 | +880 1312916010 | siddikyrejoan.work@gmail.com"), ln=True, align="C")
pdf.cell(0, 8, ascii_safe("linkedin.com/in/rejoan-siddiky | github.com/oshanto-ctrl"), ln=True, align="C")
pdf.ln(5)

def section(title):
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 6, ascii_safe(title), ln=True)
    pdf.set_font("Arial", "", 10)

section("Objective")
pdf.multi_cell(0, 6, ascii_safe(
    "Motivated in computer science with strong foundations in data structures, algorithms, and web development. "
    "Aspiring Full Stack Developer eager to build scalable, efficient solutions and contribute to innovative projects."
))

section("Education")
pdf.multi_cell(0, 6, ascii_safe("BSc. in Computer Science and Engineering, Southeast University, BD (2019 - 2024)"))
pdf.multi_cell(0, 6, ascii_safe("Higher Secondary Certificate (H.S.C), Shaheed Ramiz Uddin Cantonment College, Dhaka (2016 - 2018)"))

section("Skills")
pdf.multi_cell(0, 6, ascii_safe("Programming Languages: PHP, Python, C++"))
pdf.multi_cell(0, 6, ascii_safe("Web Development: HTML5, Tailwind CSS, SQL, Git"))

section("Experience")
pdf.multi_cell(0, 6, ascii_safe("Web Developer Intern, Byapon Youth Science Magazine, Dhaka (May 2024 - Sep 2024)"))
pdf.multi_cell(0, 6, ascii_safe("- Built and maintained website components using HTML5, Tailwind CSS, Livewire, and JavaScript"))
pdf.multi_cell(0, 6, ascii_safe("- Translated Figma designs into responsive UI"))
pdf.multi_cell(0, 6, ascii_safe("- Contributed to database design and documentation"))

section("Research Experience")
pdf.multi_cell(0, 6, ascii_safe("Generative Image Samples Using GANs (2023), Southeast University, BD"))
pdf.multi_cell(0, 6, ascii_safe("Advisor: Md. Ashiqur Rahman, Assistant Professor, Dept. of CSE"))
pdf.multi_cell(0, 6, ascii_safe("Technologies: Python, Machine Learning, Image Recognition, GANs"))

section("Projects")
pdf.multi_cell(0, 6, ascii_safe("Quote Sentiment Analyzer Web App - Python, Flask, VADER (NLTK), HTML5, CSS3"))
pdf.multi_cell(0, 6, ascii_safe("OCR Web App - Python, Flask, Easy-OCR, HTML5, CSS3"))

section("Extra Curricular Activities")
pdf.multi_cell(0, 6, ascii_safe("Programming Contests: Participated in ICPC Dhaka Regional Preliminaries, intra-university contests; solved 600+ problems on online judges"))
pdf.multi_cell(0, 6, ascii_safe("Volunteer, ICPC Dhaka Regional 2019: Assisted with technical setup and contestant support"))

section("Languages")
pdf.multi_cell(0, 6, ascii_safe("English - Professional working proficiency"))
pdf.multi_cell(0, 6, ascii_safe("Bangla - Native proficiency"))

# Save final version
final_pdf_path = "/mnt/data/Rejoan_Siddiky_ATS_Resume.pdf"
pdf.output(final_pdf_path)

final_pdf_path
