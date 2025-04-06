import streamlit as st
import time
import re

def kelime_akisi(metin, hiz_ms, alan):
    """
    Cümle cümle ve kelime kelime gösterim.
    Durdurulursa kaldığı yerden devam eder ve kelime ekranda kalır.
    """

    # Cümleleri böl
    cumleler = re.split(r'(?<=[.!?]) +', metin)

    # Oturum değişkenleri
    if "cumle_index" not in st.session_state:
        st.session_state.cumle_index = 0
    if "kelime_index" not in st.session_state:
        st.session_state.kelime_index = 0
    if "son_kelime" not in st.session_state:
        st.session_state.son_kelime = ""

    # Ekrana son kelimeyi her durumda bas
    if st.session_state.son_kelime:
        alan.markdown(
            f"<h2 style='text-align:center; color:white; font-family:Inter;'>{st.session_state.son_kelime}</h2>",
            unsafe_allow_html=True
        )

    # Eğer okuma durumu aktif değilse, sadece son kelime gösterilsin
    if not st.session_state.okuma_durumu:
        return

    # Akışı başlat
    while st.session_state.cumle_index < len(cumleler):
        cumle = cumleler[st.session_state.cumle_index].strip()
        kelimeler = cumle.split()

        for i in range(st.session_state.kelime_index, len(kelimeler)):
            st.session_state.son_kelime = kelimeler[i]  # her adımda kaydet

            # Eğer durdurulmuşsa, sadece dur ve return
            if not st.session_state.okuma_durumu:
                st.session_state.kelime_index = i
                return

            alan.markdown(
                f"<h2 style='text-align:center; color:white; font-family:Inter;'>{kelimeler[i]}</h2>",
                unsafe_allow_html=True
            )
            time.sleep(hiz_ms / 1000)

        # Cümle bittiğinde ilerle
        st.session_state.cumle_index += 1
        st.session_state.kelime_index = 0

    st.session_state.okuma_durumu = False
