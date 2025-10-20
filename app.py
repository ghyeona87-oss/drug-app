import streamlit as st
import pandas as pd

# CSV 파일 불러오기
data = pd.read_csv("drug_data.csv")

st.title("💊 약물·식품 상호작용 알리미")

# 사용자 입력
drug_name = st.text_input("복용 중인 약 이름을 입력하세요:")

if drug_name:
    result = data[data['drug_name'] == drug_name]

    if not result.empty:
        ingredient = result.iloc[0]['ingredient']
        foods = result.iloc[0]['avoid_foods']
        drugs = result.iloc[0]['avoid_drugs']

        st.subheader(f"성분: {ingredient}")
        st.write(f"⚠️ 함께 복용하면 안 되는 음식: **{foods}**")
        st.write(f"⚠️ 함께 복용하면 안 되는 약: **{drugs}**")
    else:
        st.warning("데이터베이스에 해당 약이 없습니다.")
