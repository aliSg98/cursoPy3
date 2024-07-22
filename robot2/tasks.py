from robocorp.tasks import task
from robocorp import browser, vault
from RPA.HTTP import HTTP
from RPA.Tables import Tables
#from RPA.Browser.Selenium import Selenium
import csv
from RPA.PDF import PDF
from PIL import Image
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
        slowmo=100,
    )
    open_robot_order_website()
    orders = get_orders()
    close_annoying_modal()    
    for order in orders:
        fill_the_form(order)
        order_number = order["Order number"]
        break
    
    pdf_file = store_receipt_as_pdf(order_number)
    screenshot = screenshot_robot(order_number)
    #embed_screenshot_to_receipt(screenshot, pdf_file)


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
        page.select_option("#head",orders['Head'])
        
        """body"""
        botones = page.locator("input[type='radio']")
        for boton in botones.all():
            """ver el valor del boton actual"""
            opcion = boton.evaluate("element => element.value")
            if opcion == orders["Body"]:
                boton.click()
                break
        
        """Legs"""
        page.fill("xpath=//input[@placeholder='Enter the part number for the legs']", orders['Legs'])
        """Address"""
        page.fill("#address", orders["Address"])

        return page.click('//*[@id="order" and @type="submit"]')
    
    except Exception as exception:
        print(f"Error al completar el formulario{exception}")

def fill_the_form2(orders):
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

def fill_the_form3(orders):    
    """orders es una lista de diccionarios"""
    page = browser.page()
    for row in orders:
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

        break

def screenshot_robot(order_number):
    """Take a screenshot of the page"""
    page = browser.page()
    screenshot = page.screenshot(path=f"output/orders{order_number}.png")
    return screenshot

def log_out():
    """Presses the 'Log out' button"""
    page = browser.page()  
    page.click("text=Log out")

def store_receipt_as_pdf(order_number):
    """Export the data to a pdf file"""
    page = browser.page()
    results_html = page.locator("#receipt").inner_html()
    pdf = PDF()
    pdf_final = pdf.html_to_pdf(results_html, "output/receipts/"+f"Orders-{order_number}.pdf")
    return pdf_final

def embed_screenshot_to_receipt(screenshot, pdf_file):
    pdf = PDF()
    pdf.open_pdf(pdf_file)
    page_count = pdf.get_number_of_pages()
    position = (10, 10)
    
    # Agregar una nueva página para la captura de pantalla
    pdf.add_page()
    page_width, page_height = pdf.get_page_size(page_count + 1)
    
    # Redimensionar la imagen para que se ajuste a la página
    image = Image.open(screenshot)
    image.thumbnail((page_width, page_height), Image.ANTIALIAS)
    resized_image_path = "output/resized_screenshot.png"
    image.save(resized_image_path)
    
    # Insertar la captura de pantalla en la última página
    pdf.add_image(resized_image_path, page_count + 1, position)
    
    # Guardar el PDF con la captura de pantalla insertada
    pdf.save_pdf(pdf_file)
    pdf.close_pdf()
    

        

    

         
