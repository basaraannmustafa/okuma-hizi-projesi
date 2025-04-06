import streamlit as st
import time

def kelime_akisi(metin, hiz_ms):
    """
    Metni cümle cümle gösterir, her cümlede bir duraklama olur.
    hiz_ms: 1 kelime başına milisaniye (hız)
    """
    cumleler = metin.split(". ")
    alan = st.empty()

    for cumle in cumleler:
        if not st.session_state.okuma_durumu:
            break  # durdurulduysa çık

        kelime_sayisi = len(cumle.split())
        toplam_sure = kelime_sayisi * hiz_ms / 1000.0  # saniyeye çevir

        alan.markdown(
            f"<h2 style='color:white; font-family:Inter; text-align:center;'>{cumle.strip()}.</h2>",
            unsafe_allow_html=True
        )
        time.sleep(toplam_sure)