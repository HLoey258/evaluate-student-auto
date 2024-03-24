# # Reading Excel
# EXCEL_FILE = "formb4b9.xlsx"
# TEACHER_DETAIL = "Thông tin GV"
# DETAIL = "Nội dung nhận xét"

from openpyxl import load_workbook

# book = load_workbook(EXCEL_FILE)
USERNAME = "Nope"
PASSWORD = "Nope"
# LINK
studentPortfolioLink = "https://erp.teky.edu.vn/web#view_type=list&model=student.portfolio.report&menu_id=1502&action=2189"

# FILTER ELEMENT
searchBox_XPATH = "/html/body/div[2]/div[2]/div[1]/div[3]/div[1]"

# LOGIN BOX
usernameLoginBox_XPATH = '//*[@id="login"]'
passwordLoginBox_XPATH = "/html/body/div/main/div/form/div[2]/input"
loginButton = "/html/body/div/main/div/form/div[3]/button"
