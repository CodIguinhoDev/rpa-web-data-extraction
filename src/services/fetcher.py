from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import pandas as pd


def get_table_data(table: WebElement) -> pd.DataFrame:
    headers: list[WebElement] = table.find_elements(By.TAG_NAME, "th")
    columns: list[str] = [header.text for header in headers]
    rows: list[WebElement] = table.find_elements(By.TAG_NAME, "tr")

    table_data: list[list[str]] = []

    for row in rows:
        cells: list[WebElement] = row.find_elements(By.TAG_NAME, "td")

        if cells:
            row_data: list[str] = [cell.text for cell in cells]
            table_data.append(row_data)

    return pd.DataFrame(table_data, columns=columns)
