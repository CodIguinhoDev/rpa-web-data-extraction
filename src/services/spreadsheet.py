from services.google_auth import authenticate_google
import pandas as pd
import gspread


def save_to_sheet(dataframe: pd.DataFrame) -> None:
    client: gspread.Client = authenticate_google()

    spreadsheet: gspread.Spreadsheet = client.open("rpa-challenge")
    worksheet: gspread.Worksheet = spreadsheet.sheet1
    dataframe = dataframe.fillna("")

    values: list[pd.DataFrame] = [
        dataframe.columns.tolist()
    ] + dataframe.values.tolist()

    worksheet.clear()
    worksheet.update(values)
