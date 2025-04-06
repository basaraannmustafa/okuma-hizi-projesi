import streamlit as st
from pdf_isleyici import pdf_yukle_ve_bol
from kelime_akisi import kelime_akisi
from utils import metni_temizle, kelime_say

# Streamlit Sayfa Ayarları
st.set_page_config(page_title="Okuma Hızı Uygulaması", layout="centered", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    @font-face {
        font-family: 'Inter';
        src: url('Inter-Regular.ttf');
    }

    body, .stApp {
        background-color: black;
        color: white;
        font-family: 'Inter', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📖 Okuma Hızı Sabitleyici")

# Oturum durumları
if "sayfalar" not in st.session_state:
    st.session_state.sayfalar = []
if "aktif_sayfa" not in st.session_state:
    st.session_state.aktif_sayfa = 0

# PDF Yükleme
yuklenen_pdf = st.file_uploader("Bir PDF dosyası seçin", type=["pdf"])
if yuklenen_pdf:
    st.session_state.sayfalar = pdf_yukle_ve_bol(yuklenen_pdf)
    st.success(f"{len(st.session_state.sayfalar)} sayfa başarıyla yüklendi.")

# Sayfa Seçimi
if st.session_state.sayfalar:
    toplam = len(st.session_state.sayfalar)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("⬅️ Geri", use_container_width=True):
            st.session_state.aktif_sayfa = max(0, st.session_state.aktif_sayfa - 1)
    with col3:
        if st.button("İleri ➡️", use_container_width=True):
            st.session_state.aktif_sayfa = min(toplam - 1, st.session_state.aktif_sayfa + 1)

    st.markdown(f"**Sayfa {st.session_state.aktif_sayfa + 1} / {toplam}**")
    st.markdown("---")
    
    metin = metni_temizle(st.session_state.sayfalar[st.session_state.aktif_sayfa])

    st.markdown(metin)

    st.markdown(f"📝 Kelime Sayısı: **{kelime_say(metin)}**")

    hiz = st.slider("Kelime başına gösterim süresi (ms)", min_value=100, max_value=2000, step=100, value=500)

    if st.button("▶️ Başlat", use_container_width=True):
        kelime_akisi(metin, hiz)