import streamlit as st
import time
import re

def kelime_akisi(metin, hiz_ms):
    """
    Cümle cümle ve kelime kelime gösterim.
    Durdurulunca kelime ekranda kalır, devam edince kaldığı yerden devam eder.
    """

    # Cümleleri ayır
    cumleler = re.split(r'(?<=[.!?]) +', metin)

    # Oturum değişkenleri
    if "cumle_index" not in st.session_state:
        st.session_state.cumle_index = 0
    if "kelime_index" not in st.session_state:
        st.session_state.kelime_index = 0
    if "son_kelime" not in st.session_state:
        st.session_state.son_kelime = ""

    alan = st.empty()

    # Akışı başlat
    while st.session_state.cumle_index < len(cumleler):
        cumle = cumleler[st.session_state.cumle_index].strip()
        kelimeler = cumle.split()

        for i in range(st.session_state.kelime_index, len(kelimeler)):
            # Durdurulduysa: kelimeyi göster ama döngüden çık
            if not st.session_state.okuma_durumu:
                st.session_state.kelime_index = i
                st.session_state.son_kelime = kelimeler[i]
                alan.markdown(
                    f"<h2 style='text-align:center; color:white; font-family:Inter;'>{kelimeler[i]}</h2>",
                    unsafe_allow_html=True
                )
                return

            # Devam ediyorsa: kelimeyi göster ve ilerle
            st.session_state.son_kelime = kelimeler[i]
            alan.markdown(
                f"<h2 style='text-align:center; color:white; font-family:Inter;'>{kelimeler[i]}</h2>",
                unsafe_allow_html=True
            )
            time.sleep(hiz_ms / 1000)

        # Cümle bitti
        st.session_state.cumle_index += 1
        st.session_state.kelime_index = 0

    # Tüm metin bittiğinde durdur (istersen sıfırlamayı kaldırabiliriz)
    st.session_state.okuma_durumu = False
    st.session_state.cumle_index = 0
    st.session_state.kelime_index = 0

    # Son kelimeyi ekranda tut
    alan.markdown(
        f"<h2 style='text-align:center; color:white; font-family:Inter;'>{st.session_state.son_kelime}</h2>",
        unsafe_allow_html=True
    )