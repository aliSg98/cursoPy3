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

    archivo = "orders.csv"
    """Read csv"""
    orders_list = []
    with open(archivo, 'r') as csvfichero:
                orders = csv.DictReader(csvfichero)                
                for row in orders:
                    orders_list.append(row)

    return orders_list

def close_annoying_modal():
    page = browser.page()
    page.click("button:text('OK')")
    

def fill_the_form(orders):
    """Fills in the orders data and click the 'Submit' button"""
    page = browser.page()
    page.select_option("#head",orders[0]['Head'])
    botones = page.locator("input[type='radio']")
    
    for boton in botones.all():
         opcion = boton.evaluate("element => element.value")
         if opcion == orders[0]["Body"]:
              boton.click()
     
    
    page.fill("xpath=//input[@placeholder='Enter the part number for the legs']", orders[0]['Legs'])
    page.fill("#address", orders[0]["Address"])
    page.click("text=order")
