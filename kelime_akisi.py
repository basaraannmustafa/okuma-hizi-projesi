import streamlit as st
import time
import re

def kelime_akisi(metin, hiz_ms):
    """
    Cümle cümle ve kelime kelime gösterim.
    Her cümle ekranda tek satırda akar.
    Durdurulursa, kaldığı yerden devam eder ve durduğu kelime ekranda kalır.
    """

    # Cümleleri böl
    cumleler = re.split(r'(?<=[.!?]) +', metin)

    # Oturumda cümle ve kelime index'leri yoksa tanımla
    if "cumle_index" not in st.session_state:
        st.session_state.cumle_index = 0
    if "kelime_index" not in st.session_state:
        st.session_state.kelime_index = 0
    if "son_kelime" not in st.session_state:
        st.session_state.son_kelime = ""

    alan = st.empty()

    # Her durumda son gösterilen kelimeyi göster
    if st.session_state.son_kelime:
        alan.markdown(
            f"<h2 style='text-align:center; color:white; font-family:Inter;'>{st.session_state.son_kelime}</h2>",
            unsafe_allow_html=True
        )

    # Okuma aktif değilse sadece gösterim yap, ilerleme
    if not st.session_state.okuma_durumu:
        return

    # Akışı başlat
    while st.session_state.cumle_index < len(cumleler):
        cumle = cumleler[st.session_state.cumle_index].strip()
        kelimeler = cumle.split()

        for i in range(st.session_state.kelime_index, len(kelimeler)):
            if not st.session_state.okuma_durumu:
                st.session_state.kelime_index = i
                st.session_state.son_kelime = kelimeler[i]
                alan.markdown(
                    f"<h2 style='text-align:center; color:white; font-family:Inter;'>{kelimeler[i]}</h2>",
                    unsafe_allow_html=True
                )
                return

            st.session_state.son_kelime = kelimeler[i]
            alan.markdown(
                f"<h2 style='text-align:center; color:white; font-family:Inter;'>{kelimeler[i]}</h2>",
                unsafe_allow_html=True
            )
            time.sleep(hiz_ms / 1000)

        # Cümle bittiğinde bir sonrakine geç
        st.session_state.cumle_index += 1
        st.session_state.kelime_index = 0

    # Metin bittiğinde okuma durumu kapatılır ama son kelime ekranda kalır
    st.session_state.okuma_durumu = False