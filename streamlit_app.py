import streamlit as st
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 認証情報の読み込み
credentials_dict = json.loads(st.secrets["GOOGLE_SHEETS_CREDENTIALS"])

# スコープ設定
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# サービスアカウント認証
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
client = gspread.authorize(credentials)

# スプレッドシートに接続（Secrets に追加した URL を使う）
spreadsheet = client.open_by_url(st.secrets["SPREADSHEET_URL"])
worksheet = spreadsheet.sheet1  # 1番目のシートを取得
