from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import gspread
import os

load_dotenv()


def authenticate_google() -> gspread.Client:
    scopes: list[str] = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    credentials: Credentials = Credentials.from_service_account_file(
        os.getenv("SHEETS_CREDENTIALS"), scopes=scopes
    )

    client: gspread.Client = gspread.authorize(credentials)

    return client
