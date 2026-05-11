import streamlit as st
import pandas as pd
import numpy as np
import calendar
import datetime

st.title("2026년 3월 수면기록")
st.caption("10강 실습 과제")

st.header("소개")
st.write("이 대시보드는 본인의 3월 수면 기록에 관한 내용입니다.")

year = 2026
month = 3
_, last_day = calendar.monthrange(year, month)
march_dates = [datetime.date(year, month, day) for day in range(1, last_day + 1)]

# [데이터]
st.header("데이터")
data = {
    "항목": march_dates,
    "값": [4.0, 0.0, 8.2, 4.5, 7.0, 5.5, 6.25, 8.5, 5.3, 10.2, 5.0, 8.6, 2.75, 10.0, 6.17, 3.0, None, 4.0, None, 4.8, 11.25, 4.67, 5.25, 7.8, None, 7.0, 4.8, None, 6.8, None, 6.5]
}
df = pd.DataFrame(data)
st.dataframe(df)

# [위젯 + 위젯-화면 연동]
st.header("설정")
선택 = st.selectbox("항목을 선택하세요", df["항목"])   # ← 위젯 추가
선택값 = df[df["항목"] == 선택]["값"].values[0]
st.metric(label=선택.strftime("%Y-%m-%d"), value=선택값)                    # ← 위젯 값에 따라 화면 변경

# [차트]
st.header("차트")
st.bar_chart(df.set_index("항목"))
