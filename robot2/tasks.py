from robocorp.tasks import task
from robocorp import browser, vault
from RPA.HTTP import HTTP
from RPA.Tables import Tables
import csv
from RPA.PDF import PDF
from RPA.Archive import Archive
import sys

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
    for order in orders:
        fill_the_form(order)
        order_number = order["Order number"]
        break
    store_receipt_as_pdf(order_number)
    screenshot_robot(order_number)
    pdf_file = store_receipt_as_pdf(order_number)
    screenshot = screenshot_robot(order_number)
    embed_screenshot_to_receipt(screenshot, pdf_file)
    archive_receipts()


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
    page.screenshot(path=f"output/receipts/orders{order_number}.png")
    screenshot = f"output/receipts/orders{order_number}.png"
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
    pdf.html_to_pdf(results_html, "output/receipts/"+f"Orders-{order_number}.pdf")
    pdf_final = "output/receipts/"+f"Orders-{order_number}.pdf"
    return pdf_final

def embed_screenshot_to_receipt(screenshot, pdf_file):
    pdf = PDF()
    pdf.open_pdf(pdf_file)
    pdf.add_watermark_image_to_pdf(
        image_path = screenshot,
        source_path = pdf_file,
        output_path="output/receipts/Orders_embed.pdf"

    )
    pdf.close_all_pdfs()

def archive_receipts():
    archive = Archive()
    path_archives = 'C:/Users/nasudre/Desktop/Transactics/Cursos/python/Core Python 3 Getting Started/Repo git/cursoPy3/robot2/output/receipts'
    #zip_name = 'C:\Users\nasudre\Desktop\Transactics\Cursos\python\Core Python 3 Getting Started\Repo git\cursoPy3\robot2\output\receipts\orders.zip'
    #if not os.path.exists(path_archives):
    #files = [os.path.join(path_archives, file) for file in os.listdir(path_archives) if file.endswith(('.pdf', '.png', '.jpg'))]
    #if not files:
    #print(f"No hay archivos {path_archives}.")
    #print(f"El directorio {path_archives} no existe.")
    #else:
    # Crear el archivo ZIP con los recibos PDF
    archive.archive_folder_with_zip(path_archives, 'orders.zip')
    


        

    

         
