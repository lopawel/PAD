import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime
import time

st.title("Streamlit - PAD 6")

page = st.sidebar.selectbox('Wybierz zakladkę: ', ['Ankieta', 'Staty'])

if page == 'Staty':

    st.header('Staty')
    data = st.file_uploader("Wczytaj plik: ", type=['csv'])

    if data is not None:

        with st.spinner("..."):
            time.sleep(3)

        df = pd.read_csv(data)
        st.dataframe(df.head())
        status = st.radio("Wybierz wykres: ", ("Słupkowy", "Liniowy"))

        if status == "Słupkowy":
            columns = df.columns.to_list()
            plot_data = df[columns[1]]
            st.bar_chart(plot_data)

        else:
            columns = df.columns.to_list()
            plot_data = df[columns[1]]
            st.line_chart(plot_data)

else:
    st.header('Ankieta')
    firstname = st.text_input("Wprowadź imię: ", "...")
    lastname = st.text_input("Wprowadź nazwisko: ", "...")

    if st.button("Podsumuj: "):
        result = "Twoje dane zostaly zapisane do kwestionariusza: " + firstname.title() + " " + lastname.title()
        st.success(result)