from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Import Variable
from defineVariable import XPATH_TeacherName, XPATH_TeacherCode
from defineVariable import (
    XPATH_NEXTBUTTON,
    XPATH_SUBMITBUTTON,
    XPATH_DATE_REPORT,
    XPATH_DROPDOWN_CENTER_CODE,
    XPATH_DROPDOWN_REPORT_CODE,
    XPATH_DATE_START,
)

from defineVariable import formb4b9

from defineVariable import (
    TEACHER_NAME,
    TEACHER_CODE,
    REPORT_CODE,
    DAY_REPORT,
    DAY_START,
)

from defineVariable import raw_data

#  Setting chrome driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


# Submit Form
def submitForm(xpath_form):
    submit_button = driver.find_element(By.XPATH, xpath_form)
    sleep(3)
    submit_button.click()


# Fill Teacher Name + code and center
def fillConstrantField(teacher_name, teacher_code, center_code):
    driver.find_element(By.XPATH, XPATH_TeacherName).send_keys(teacher_name)
    driver.find_element(By.XPATH, XPATH_TeacherCode).send_keys(teacher_code)
    # Center code
    dropdown = driver.find_element(By.XPATH, XPATH_DROPDOWN_CENTER_CODE)
    dropdown.click()
    sleep(2)
    option_xpath = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[{center_code}]"
    option = driver.find_element(By.XPATH, option_xpath)
    option.click()


def selectReportCode(report_code, xpath_field):
    dropdown = driver.find_element(By.XPATH, xpath_field)
    dropdown.click()
    sleep(2)
    option_xpath = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[2]/div[{report_code}]"
    option = driver.find_element(By.XPATH, option_xpath)
    option.click()
    sleep(1)


def selectDate(day_report, xpath_field):
    date_field = driver.find_element(By.XPATH, xpath_field).send_keys(day_report)
    # date_field.send_keys(day_report)


def autofillingForm1():
    form_index = 4
    for index, row in enumerate(raw_data, start=0):
        sleep(4)
        driver.get(formb4b9)
        sleep(6)
        fillConstrantField(TEACHER_NAME, TEACHER_CODE, 8)
        sleep(2)
        selectDate(DAY_START, XPATH_DATE_START)
        selectDate(DAY_REPORT, XPATH_DATE_REPORT)
        sleep(2)
        selectReportCode(REPORT_CODE, XPATH_DROPDOWN_REPORT_CODE)
        for jndex, elements in enumerate(row, start=0):
            if jndex <= 1:
                xpath = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[{form_index}]/div/div/div[2]/div/div[1]/div/div[1]/input"
                input_field = driver.find_element(By.XPATH, xpath)
                input_field.send_keys(str(raw_data[index][jndex]))
                form_index += 1
                print(form_index)
            if jndex == 1:
                submitForm(XPATH_NEXTBUTTON)
                sleep(3)
                flag = True
            if jndex > 1 and flag == True:
                sleep(1)
                xpath = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[{form_index-4}]/div/div/div[2]/div/div[1]/div[2]/textarea"
                input_field = driver.find_element(By.XPATH, xpath)
                input_field.send_keys(str(raw_data[index][jndex]))
                form_index += 1

            if form_index == 10:
                form_index = 4
                submitForm(XPATH_SUBMITBUTTON)
                break


autofillingForm1()
