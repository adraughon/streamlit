
import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/13evkYlWR67JFd9d77xZdbvct75Lw_POK3oa-m5G9xDU/edit?gid=0#gid=0"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)
