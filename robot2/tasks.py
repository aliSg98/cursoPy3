from robocorp.tasks import task
from robocorp import browser, vault
from RPA.HTTP import HTTP
from RPA.Tables import Tables
#from RPA.Browser.Selenium import Selenium
import csv
from RPA.PDF import PDF
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
    store_receipt_as_pdf(orders[1]['Order number'])
    screenshot_robot(orders[1]['Order number'])


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
    try:
        """orders es una lista de diccionarios"""
        page = browser.page()
        #page.select_option("#head",orders[1]['Head'])
        for row in orders:
            """head"""
            page.select_option("#head",row['Head'])
            break
        
        """body"""
        botones = page.locator("input[type='radio']")
        for boton in botones.all():
            """ver el valor del boton actual"""
            opcion = boton.evaluate("element => element.value")
            for row in orders:
                if opcion == row["Body"]:
                    boton.click()
            break
        
        #for boton in botones.all():
            """ver el valor del boton actual"""
        #    opcion = boton.evaluate("element => element.value")
        #     if opcion == orders[1]["Body"]:
        #          boton.click()
        #          break
        
        """Legs"""
        for row in orders:
            page.fill("xpath=//input[@placeholder='Enter the part number for the legs']", row['Legs'])
            break
        #page.fill("xpath=//input[@placeholder='Enter the part number for the legs']", orders[1]['Legs'])
        """Address"""
        for row in orders:
            page.fill("#address", row["Address"])
            break
        #Si el try es correcto:
        return page.click("text=order")
    
    except Exception as exception:
         print(f"Error al completar el formulario{exception}")

def fill_the_form2(orders):
    try:
        """orders es una lista de diccionarios"""
        page = browser.page()
        page.select_option("#head",orders[1]['Head'])
        
        """body"""
        botones = page.locator("input[type='radio']")
        for boton in botones.all():
            """ver el valor del boton actual"""
            opcion = boton.evaluate("element => element.value")
            if opcion == orders[1]["Body"]:
                  boton.click()
                  break
        
        """Legs"""
        page.fill("xpath=//input[@placeholder='Enter the part number for the legs']", orders[1]['Legs'])
        """Address"""
        page.fill("#address", orders[1]["Address"])
        
        #Si el try es correcto:
        return page.click("text=order")
    
    except Exception as exception:
         print(f"Error al completar el formulario{exception}")

def screenshot_robot(order_number):
    """Take a screenshot of the page"""
    page = browser.page()
    page.screenshot(path="output/orders_summary.png")

def log_out():
    """Presses the 'Log out' button"""
    page = browser.page()  
    page.click("text=Log out")

def store_receipt_as_pdf(order_number):
    """Export the data to a pdf file"""
    page = browser.page()
    results_html = page.locator("#model-info").inner_html()
    pdf = PDF()
    #pdf.html_to_pdf(results_html, "output/receipts/"+f"Order-number:{order_number}.pdf")
    pdf.html_to_pdf(results_html, "output/receipts/Order.pdf")

    

         
