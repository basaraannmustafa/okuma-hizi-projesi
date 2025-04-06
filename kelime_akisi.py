import streamlit as st
import time
import re

def kelime_akisi(metin, hiz_ms):
    """
    Cümle cümle ve kelime kelime gösterim.
    Her cümle ekranda tek satırda akar.
    Durdurulursa, kaldığı yerden devam eder.
    """

    # Cümleleri böl
    cumleler = re.split(r'(?<=[.!?]) +', metin)

    # Oturumda cümle ve kelime index'leri yoksa tanımla
    if "cumle_index" not in st.session_state:
        st.session_state.cumle_index = 0
    if "kelime_index" not in st.session_state:
        st.session_state.kelime_index = 0

    alan = st.empty()

    # Cümleleri tek tek işle
    while st.session_state.cumle_index < len(cumleler):
        cumle = cumleler[st.session_state.cumle_index].strip()
        kelimeler = cumle.split()

        # Kaldığı kelimeden başla
        for i in range(st.session_state.kelime_index, len(kelimeler)):
            if not st.session_state.okuma_durumu:
                alan.markdown(
                    f"<h2 style='text-align:center; color:white; font-family:Inter;'>{kelimeler[i]}</h2>",
                    unsafe_allow_html=True
                )
                # Durdurulursa index'i sakla ve çık
                st.session_state.kelime_index = i
                return

            alan.markdown(
                f"<h2 style='text-align:center; color:white; font-family:Inter;'>{kelimeler[i]}</h2>",
                unsafe_allow_html=True
            )
            time.sleep(hiz_ms / 1000)

        # Cümle bitti, bir sonrakine geç
        st.session_state.cumle_index += 1
        st.session_state.kelime_index = 0

    # Tüm metin bittiğinde sıfırla (veya istersen bunu kaldırabiliriz)
    st.session_state.okuma_durumu = False
    st.session_state.cumle_index = 0
    st.session_state.kelime_index = 0
