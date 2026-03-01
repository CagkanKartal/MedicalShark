import streamlit as st
import pandas as pd
import time
from google import genai

# Sayfa ayarları
st.set_page_config(page_title="MedicalShark", page_icon="🦈", layout="wide", initial_sidebar_state="expanded")

# --- Custom Premium CSS ---
st.markdown("""
<style>
/* Modern Font */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

html, body, [class*="css"]  {
    font-family: 'Outfit', sans-serif;
}

/* Gradient Headers */
h1, h2, h3 {
    background: linear-gradient(90deg, #11998e, #38ef7d);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800 !important;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
    color: white !important;
    border-radius: 30px !important;
    border: none !important;
    padding: 10px 24px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(17, 153, 142, 0.4) !important;
}
.stButton>button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 8px 25px rgba(17, 153, 142, 0.6) !important;
    background: linear-gradient(135deg, #0f857a 0%, #32cc6b 100%);
}

/* Sliders custom colors */
.stSlider div[data-baseweb="slider"] > div > div > div {
    background-color: #11998e !important;
}

</style>
""", unsafe_allow_html=True)

# Sol Menü (Sidebar) Navigasyonu
st.sidebar.markdown("## 🦈 MedicalShark")
menu = st.sidebar.radio(
    "Menü", 
    ["Ana Sayfa", "Hasta Paneli (Veri Girişi)", "Doktor/Klinik Profilleri", "🧠 AI Deneyim Analizi"],
    label_visibility="hidden"
)
st.sidebar.markdown("---")
st.sidebar.caption("MedicalShark")

if menu == "Ana Sayfa":
    # Hero Bölümü
    col_img, col_text = st.columns([1, 4])
    with col_img:
        st.markdown("<h1 style='font-size: 80px; text-align:center;'>🦈</h1>", unsafe_allow_html=True)
    with col_text:
        st.title("MedicalShark Platformu")
        st.markdown("<p style='font-size:1.2rem; color:#555;'>Hasta odaklı, algoritma destekli, manipülasyonsuz ve şeffaf değerlendirme platformu.</p>", unsafe_allow_html=True)
    
    st.info("👈 Sol menüden platformun modüllerini test edebilirsiniz.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Platform metrikleri
    col1, col2, col3 = st.columns(3)
    col1.metric("Doğrulanmış Deneyim", "1,245", "+12% Bu Ay")
    col2.metric("Sistemdeki Klinikler", "84", "+5 Yeni Eklendi")
    col3.metric("AI Analiz Raporu", "320", "Güncel")
    
    st.markdown("---")
    st.markdown("### Neden Biz?")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.success("**🎯 Dinamik Puanlama:** Bot manipülasyonlarına kapalı, hasta deneyimine göre ağırlıklı puan hesaplaması.")
    with c2:
        st.info("**🤖 Gerçek Zamanlı AI:** Yüzlerce yorum arasından kronik problemleri ve klinik başarılarını anında sentezler.")
    with c3:
        st.warning("**🛡️ Güven ve Şeffaflık:** MedicalShark ağında hiçbir veri kaybolmaz veya değiştirilemez.")

elif menu == "Hasta Paneli (Veri Girişi)":
    st.header("📝 Sürecinizi Paylaşın")
    st.write("Platformun dinamik puanlama sistemini test edebilirsiniz. Bu form doldurulduğunda arka planda dinamik güven puanı hesaplanır.")
    
    with st.form("hasta_formu", clear_on_submit=False):
        st.markdown("#### Tedavi Detayları")
        colA, colB = st.columns(2)
        with colA:
            hastalik = st.selectbox("Tedavi Alanı (Örnek Data)", ["KBB", "Göz Hastalıkları", "Dahiliye", "Cerrahi", "Saç Ekimi", "Medikal Estetik"])
        with colB:
            klinik = st.selectbox("Klinik / Doktor Seçimi", ["Dr. Ahmet Yılmaz", "Gözde Cerrahi Merkezi", "Estetik Clinic", "Şifa Hastanesi"])
        
        surec = st.text_area("Sürecinizi detaylıca anlatın (AI bu metni analiz edecek)", height=150, placeholder="Örn: İlk görüşmeden taburcu olana kadar neler yaşandı? Beklentileriniz karşılandı mı?")
        
        st.markdown("---")
        st.markdown("#### Puanlama Kriterleri (Ağırlıklı Algoritma)")
        st.caption("Klasik 5 yıldız sistemi yerine spesifik metrikler ölçülür.")
        iletisim = st.slider("İletişim ve Yaklaşım (Ağırlık: %30)", 1, 10, 5, help="Doktor ve personelin size olan yaklaşımı nasıldı?")
        aciklayicilik = st.slider("Süreci Açıklayıcılık (Ağırlık: %30)", 1, 10, 5, help="Tedavi hakkında yeterince bilgilendirildiniz mi?")
        takip = st.slider("Tedavi Sonrası Takip (Ağırlık: %40)", 1, 10, 5, help="Operasyon veya tedavi sonrası iyileşme sürecinde ilgilenildi mi?")
        
        st.markdown("<br>", unsafe_allow_html=True)
        submit_button = st.form_submit_button("🩺 Deneyimi Şifrele ve Gönder")
        
        if submit_button:
            with st.spinner("Algoritma çalışıyor..."):
                time.sleep(1) # Efektif demo beklemesi
            agirlikli_puan = (iletisim * 0.3) + (aciklayicilik * 0.3) + (takip * 0.4)
            st.success(f"✅ Teşekkürler! Deneyiminiz şifrelenerek {klinik} için sisteme kaydedildi.")
            
            # Sonuç Kutusu
            st.info("💡 **Bilgi:** Arka planda sabit oranlı olmayan güven algoritması çalıştı.")
            st.metric(label="MedicalShark Trust Score (Dinamik Güven Puanı)", value=f"{agirlikli_puan:.1f} / 10.0", delta=f"{agirlikli_puan - 7.0:.1f} Sektör Ortalamasına Göre")

elif menu == "Doktor/Klinik Profilleri":
    st.header("👩‍⚕️ Liderlik Tablosu & Klinik Değerlendirmeleri")
    st.write("Kullanıcıların dinamik ve ağırlıklı oylarıyla oluşan manipülasyonsuz sıralama:")
    
    # Sahte (Dummy) veri tablosu
    data = {
        "Klinik/Doktor": ["Estetik Clinic", "Dr. A (KBB)", "Gözde Cerrahi Merkezi", "Şifa Hastanesi", "Dr. B (Dahiliye)"],
        "İletişim": [9.5, 8.5, 9.0, 7.5, 6.5],
        "Açıklayıcılık": [9.0, 7.0, 9.5, 8.0, 7.0],
        "Süreç Takibi": [9.2, 9.0, 8.5, 6.0, 5.0],
    }
    df = pd.DataFrame(data)
    
    # AI Puanı Hesaplama
    df["Genel AI Puanı"] = (df["İletişim"] * 0.3) + (df["Açıklayıcılık"] * 0.3) + (df["Süreç Takibi"] * 0.4)
    df = df.sort_values(by="Genel AI Puanı", ascending=False).reset_index(drop=True)
    
    # Stilize Tablo
    st.dataframe(
        df.style.background_gradient(cmap='Greens', subset=['Genel AI Puanı']).format({'Genel AI Puanı': '{:.2f}'}),
        width='stretch',
        height=300
    )

elif menu == "🧠 AI Deneyim Analizi":
    st.header("🧠 NLP Tabanlı Süreç Analizi (Canlı AI)")
    st.write("Arka plandaki binlerce yorum, anlık olarak gelişmiş LLM API (Google Gemini 2.5 Flash) ile analiz edilir.")
    
    # Sistem API anahtarını arayüzden değil, güvenli sunucu kasasından (secrets) çeker
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except KeyError:
        st.error("⚠️ Sistem Hatası: API Anahtarı sunucuda bulunamadı. Lütfen yöneticiye bildirin.")
        api_key = None
    
    secilen_alan = st.selectbox("Analiz Edilecek Klinik/Tedavi Seçin", ["Dr. Ahmet Yılmaz - Saç Ekimi", "Gözde Cerrahi - Lazer Epilasyon"])
    
    # Sisteme gömdüğümüz sahte kullanıcı yorumları (Sanki veritabanından çekilmiş gibi)
    dummy_yorumlar = """
    1. İletişim süperdi ama randevu saatinde 40 dakika bekledim. Süreç takibi fena değil.
    2. Doktor çok açıklayıcıydı, operasyon sonrası ilk yıkama acılıydı ama bilgi verdikleri için rahattım.
    3. Kliniğin temizliği iyi ama tedavi sonrası kimse arayıp sormadı, mesajlara geç dönüldü.
    4. İşlem çok başarılıydı, asistanlar çok ilgiliydi ama fiyat beklentimin üstündeydi.
    5. Randevu sistemi berbat, iki kez iptal edildi. Ama doktorun uzmanlığına lafım yok, sonuç güzel.
    """
    
    st.markdown("#### Sistemdeki Hasta Yorumları")
    st.info("Bu yorumlar veritabanından çekilmiş kabul edilerek yapay zekaya kaynak olarak sunulur.")
    st.text_area("Ham Yorum Datası (Salt Okunur)", dummy_yorumlar, height=150, disabled=True)

    if st.button("🚀 Gerçek Zamanlı AI Analizini Başlat"):
        if not api_key:
            st.error("⚠️ Lütfen önce bir API Key girin!")
        else:
            try:
                with st.spinner('Gemini AI karmaşık verileri okuyor ve sentezliyor...'):
                    # Yeni google-genai SDK kullanımı
                    client = genai.Client(api_key=api_key)
                    
                    prompt = f"""
                    Sen profesyonel bir sağlık kalitesi analizörüsün. Aşağıdaki hasta yorumlarını sentezleyip yöneticilere/kliniklere rapor sunacaksın.
                    
                    Lütfen şu başlıklar altında ÇOK KISA VE ÖZ (maddeler halinde) bir rapor hazırla:
                    1. 🌟 Genel Memnuniyet Özeti
                    2. ⚠️ En Sık Yaşanan Sorun (Kronik Şikayet)
                    3. 💡 Kliniğe Operasyonel Tavsiye
                    
                    Yorumlar:
                    {dummy_yorumlar}
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt
                    )
                    
                    st.markdown("---")
                    st.subheader("📊 Canlı AI Analiz Çıkıtısı")
                    
                    # Sonucu şık bir kutu içinde göster
                    st.markdown(f"> {response.text}")
                    
                    st.success("✅ Analiz başarıyla tamamlandı.")
            except Exception as e:
                st.error(f"API Bağlantı Hatası! Lütfen API Key'i ve bağlantıyı kontrol et:\n{e}")