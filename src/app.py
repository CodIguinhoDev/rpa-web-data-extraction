from services.fetcher import get_table_data
from utils.browser import open_browser, navigate_to, wait_element
from services.spreadsheet import save_to_sheet
from selenium.webdriver.common.by import By


def run() -> None:
    try:
        browser = open_browser()
        navigate_to(browser, "https://rpachallengeocr.azurewebsites.net/")
        table = wait_element(browser, (By.ID, "tableSandbox"))
        data = get_table_data(table)
        save_to_sheet(data)
        print("Dados enviados para a planilha com sucesso!")

    except Exception as error:
        print("Algo deu errado", error)
