import requests  # Web sayfasını talep etmek için
from bs4 import BeautifulSoup as bs  # Web sayfasının içeriğini analiz etmek için
import time  # Zaman işlemleri için
import random  # Rastgele sayı üretmek için
import pandas as pd  # Veri analizi için kullanılacak pandas kütüphanesi

# Boş listeler oluştur
fiyat = []  # Fiyatları saklamak için
m_2a = []  # Metrekareleri saklamak için

# 1'den 115'e kadar olan sayıları döngü
for i in range(1, 115):
    # Web sayfasının URL'si
    adres = f'https://www.hepsiemlak.com/muratpasa-satilik/daire?page={i}'

    # Tarayıcı gibi davranmak için kullanıcı ajanı başlığı
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        # Diğer user-agent bilgileri
    ]
    baslik = {
        'User-Agent': random.choice(user_agents)  # Rastgele bir user-agent
    }

    # Web sayfasını talep et ve yanıtı
    sayfa = requests.get(adres, headers=baslik)

    # BeautifulSoup nesnesi oluşturarak sayfa içeriğini analiz
    soup = bs(sayfa.content, 'lxml')
    fiyatlar = soup.find_all('span', {'class': 'list-view-price'})  # Fiyatları içeren HTML etiketleri
    m_2 = soup.find_all('span', {'class': 'celly squareMeter list-view-size'})  # Metrekareleri içeren HTML etiketleri

    # Bekleme süresi ekleyerek bot gibi algılanmanın önüne geçmek için
    time.sleep((random.randint(3, 7)))

    # Fiyatları ve metrekareleri alarak listelere
    for i in range(len(fiyatlar)):
        # Fiyatları işle ve listeye ekle
        fiyat_metni = fiyatlar[i].text.strip()  # Metnin başındaki ve sonundaki boşlukları temizleme
        fiyat_metni = fiyat_metni.replace('.', '')  # Noktaları kaldırma
        fiyat_metni = fiyat_metni.replace('TL', '')  # "TL" kelimesini kaldırma
        fiyat.append(int(fiyat_metni))

        # Metrekareleri işle ve listeye ekleme
        m2_metni = m_2[i].text.strip()  # Metnin başındaki ve sonundaki boşlukları temizleme
        m2_metni = m2_metni.replace(' m²', '')  # " m²" kelimesini kaldırma
        m_2a.append(int(m2_metni))

# Pandas DataFrame oluşturma
data = pd.DataFrame(list(zip(fiyat, m_2a)), columns=['Fiyat', 'M2'])

# Sayısal değerleri düzgün bir formata getirme
pd.options.display.float_format = '{:,.2f}'.format


print(data.describe())
data.to_excel("antalya_muratpasa.xlsx")
