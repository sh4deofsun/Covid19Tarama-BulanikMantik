from datetime import time
import streamlit as st
from numpy import linspace
from pyit2fls import IT2FLS
from app.helper.mf import MF
from app.helper.calc_risk import Risk
def main ():
    st.title('Covid-19 Tarama')

    cough = st.slider('Oksurme yoğunluğu:', 0.0, 9.9, 0.0)

    fever = st.slider('Ateş yoğunluğu:', 0.0, 9.9, 0.0)

    breath_diff = st.slider('Nefes alma zorlugu:', 0.0, 9.9, 0.0)

    age = st.slider('Yasiniz:', 1, 100, 25)

    polluted = st.checkbox('Hava kirliligi olan bir yerde mi yasiyorsun?')

    hypertension = st.checkbox('Hiper Tansiyonun var mi?')

    diabetes = st.checkbox('Diyabet hastasi misin?')

    cardiovascular = st.checkbox('Kardiovaskuler bir sorun yasiyor musun?')

    respiratory = st.checkbox('Solunum ile ilgili bir hastaligin var mi?')

    immune = st.checkbox('Bagisiklik sistemin zayif mi?')

    calculate_risk = st.button('Hesapla ')

    if(calculate_risk is True):
        additional_risks = (age,polluted,hypertension,diabetes,cardiovascular,respiratory,immune)
        add_result = Risk.calc_additional_risks_score(*additional_risks)
        
        myIT2FLS = IT2FLS()
        MF.add_input_veriable(myIT2FLS)
        MF.add_rule(myIT2FLS)
        risk = MF.evaluate(myIT2FLS,cough,fever,breath_diff,add_result)

        st.subheader(f"Covid-19 olama ihtimalin %{risk}")

