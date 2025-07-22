# LLM Tour Buddy

Bu proje, Türkiye hakkında turistik bilgiler sunan bir yapay zeka sohbet botudur. Streamlit arayüzü ve terminal üzerinden çalışabilen iki farklı versiyonu bulunmaktadır. Proje, LangChain ve Ollama kullanılarak geliştirilmiştir.

## Özellikler

- **İnteraktif Sohbet Arayüzü:** Streamlit kullanarak kullanıcı dostu bir web arayüzü sunar.
- **Terminal Desteği:** Komut satırı üzerinden de çalışabilir.
- **Türkiye Odaklı Bilgiler:** Türkiye'nin tarihi, turistik yerleri, yerel mutfağı ve seyahat ipuçları hakkında bilgi verir.
- **Konuşma Hafızası:** Sohbet geçmişini hatırlayarak daha tutarlı cevaplar üretir.

## Kurulum

> **Not:** Bu talimatlar, `LLM-Practices` deposunu zaten klonladığınızı ve terminalinizde `LLM-tour-buddy` klasörünün içinde olduğunuzu varsaymaktadır.

1.  **Sanal Ortam Oluşturun ve Aktif Edin:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux için
    # venv\Scripts\activate  # Windows için
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ollama Kurulumu:**
    Bu proje, yerel bir dil modeli (LLM) olan Ollama'yı kullanmaktadır. Eğer sisteminizde Ollama yüklü değilse, [resmi web sitesinden](https://ollama.com/) indirip kurun.

4.  **Dil Modelini İndirin:**
    Proje `llama3.2:3b` modelini kullanmaktadır. Aşağıdaki komut ile modeli indirebilirsiniz:
    ```bash
    ollama pull llama3.2:3b
    ```

## Kullanım

### Streamlit Arayüzü

Web tabanlı arayüzü başlatmak için aşağıdaki komutu çalıştırın:

```bash
streamlit run streamlit_tourist_bot.py
```

### Terminal Uygulaması

Terminal üzerinden sohbet botunu çalıştırmak için:

```bash
python tourist_bot_terminal.py
```

Uygulamadan çıkmak için `quit` yazabilirsiniz.

## Proje Yapısı

-   `streamlit_tourist_bot.py`: Streamlit arayüzünü içeren ana dosya.
-   `tourist_bot_terminal.py`: Terminal tabanlı sohbet botu.
-   `requirements.txt`: Projenin bağımlılıklarını listeleyen dosya.
-   `README.md`: Bu dosya. 