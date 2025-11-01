import streamlit as st
import datetime
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.title("CBT記録アプリ（Google Sheets保存）")

# --- Secrets から認証情報とURLを取得 ---
credentials_dict = json.loads(st.secrets["GOOGLE_SHEETS_CREDENTIALS"])
spreadsheet_url = st.secrets["SPREADSHEET_URL"]

# --- Google Sheets API に接続 ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
client = gspread.authorize(credentials)
sheet = client.open_by_url(spreadsheet_url).sheet1  # 最初のシートを開く

# --- ユーザー入力フォーム ---
st.header("今日の記録")

name = st.text_input("ニックネームまたはID（任意）")
mood = st.slider("気分のスコア（0 = 最悪, 10 = 最高）", 0, 10, 5)
behavior = st.text_area("今日の行動")
reflection = st.text_area("振り返り・気づき")

# --- 送信ボタン ---
if st.button("送信"):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_row = [now, name, mood, behavior, reflection]
    sheet.append_row(new_row)
    st.success("✅ Google Sheets に記録されました！")

