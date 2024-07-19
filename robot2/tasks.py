from robocorp.tasks import task
from robocorp import browser, vault
from RPA.HTTP import HTTP
from RPA.Tables import Tables
#from RPA.Browser.Selenium import Selenium
import csv
#from selenium import webdriver
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By

@task
def order_robots_from_RobotSpareBin():
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
    browser.configure(
        slowmo=1000,
    )
    open_robot_order_website()
    orders = get_orders()
    close_annoying_modal()
    fill_the_form(orders)


def open_robot_order_website():
    """Navigates to the given URL"""
    browser.goto("https://robotsparebinindustries.com/#/robot-order")


def get_orders():
    """Downloads csv file from the given URL"""
    http = HTTP()
    http.download(url="https://robotsparebinindustries.com/orders.csv", overwrite=True)
    """Read csv"""
    library = Tables()
    orders_csv = library.read_table_from_csv(
        "orders.csv", columns=["Order number", "Head", "Body", "Legs", "Address"]
    )
    orders = []
    for order in orders_csv:
        orders.append(order)

    return orders

def close_annoying_modal():
    page = browser.page()
    page.click("button:text('OK')")
    

def fill_the_form(orders):
    """Fills in the orders data and click the 'Submit' button"""
    page = browser.page()
    xpath_head = "//select[@id='head']]"
    page.select_option(xpath_head,values=orders["Head"])
    #browser.input_text(head,orders["Head"])
    #head = page.find_element(By.XPATH,"//*[@id="head"]"))
    #head.select_by_value(orders["Head"])
    #page.fill("#head", orders["Head"])
    #page.fill("#body", orders[2])
    #page.fill("#legs", str(orders[3]))
    xpath_address = "//select[@id='address']"
    page.fill("#address", orders["Address"])
    #page.click("text=Submit")
