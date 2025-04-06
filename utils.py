import re

def metni_temizle(metin):
    """
    Gereksiz boşlukları, satır başlarını vs. temizler.
    """
    temiz = re.sub(r'\s+', ' ', metin).strip()
    return temiz


def kelime_say(metin):
    """
    Metindeki kelime sayısını döndürür.
    """
    return len(metin.split())


def harf_say(metin):
    """
    Harf (karakter) sayısını döndürür, boşluklar hariç.
    """
    return len([c for c in metin if not c.isspace()])
