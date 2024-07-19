from robocorp.tasks import task
from robocorp import browser, vault
from RPA.HTTP import HTTP
from RPA.Tables import Tables

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
    for order in orders:
        return print(order["Address"])
    
    #page.fill("#ordernumber", str(orders["Order number"]))
    #page.fill("#head", orders[1])
    #page.fill("#body", orders[2])
    #page.fill("#legs", str(orders[3]))
    page.fill("#address", orders["Address"])
    page.click("text=Submit")
