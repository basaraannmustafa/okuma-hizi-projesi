import streamlit as st
import time

def kelime_akisi(metin, hiz_ms):
    """
    Verilen metni kelime kelime Streamlit arayüzünde gösterir.
    hiz_ms: kelime başına gösterim süresi (milisaniye)
    """
    kelimeler = metin.split()
    alan = st.empty()

    for kelime in kelimeler:
        alan.markdown(
            f"<h1 style='text-align:center; color:white; font-family:Inter;'>{kelime}</h1>",
            unsafe_allow_html=True
        )
        time.sleep(hiz_ms / 1000.0)