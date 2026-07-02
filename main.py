from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import requests

class IPSorguUygulamasi(App):
    def build(self):
        # Ana dikey yerleşim planı
        self.ana_duzen = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Başlık
        self.ana_duzen.add_widget(Label(text="CRIMSON IP TRACKER v1.0", font_size=24, size_hint_y=None, height=50))
        
        # IP Giriş Alanı
        self.ip_giris = TextInput(hint_text="Sorgulanacak IP Adresini Girin...", multiline=False, size_hint_y=None, height=50)
        self.ana_duzen.add_widget(self.ip_giris)
        
        # Sorgula Butonu
        self.buton = Button(text="IP KONUMUNU BUL", background_color=(1, 0, 0, 1), size_hint_y=None, height=60)
        self.buton.bind(on_press=self.sorgula)
        self.ana_duzen.add_widget(self.buton)
        
        # Sonuçların kaydırılabilir olması için ScrollView
        self.kaydirici = ScrollView()
        self.sonuc_etiketi = Label(text="Sonuçlar burada görünecek...", halign="left", valign="top", text_size=(400, None))
        self.kaydirici.add_widget(self.sonuc_etiketi)
        
        self.ana_duzen.add_widget(self.kaydirici)
        return self.ana_duzen

    def sorgula(self, instance):
        hedef_ip = self.ip_giris.text.strip()
        url = f"http://ip-api.com/json/{hedef_ip}?lang=tr"
        
        try:
            cevap = requests.get(url, timeout=5).json()
            if cevap.get("status") == "fail":
                self.sonuc_etiketi.text = "[X] Hata: Geçersiz IP adresi!"
            else:
                rapor = (
                    f"🌐 IP: {cevap.get('query')}\n"
                    f"🏳️ Ülke: {cevap.get('country')}\n"
                    f"📍 Şehir: {cevap.get('city')}\n"
                    f"🏢 ISP: {cevap.get('isp')}\n"
                    f"🧭 Enlem: {cevap.get('lat')}\n"
                    f"🧭 Boylam: {cevap.get('lon')}\n\n"
                    f"🗺️ Google Haritalar Linki:\n"
                    f"https://www.google.com/maps/?q={cevap.get('lat')},{cevap.get('lon')}"
                )
                self.sonuc_etiketi.text = rapor
        except:
            self.sonuc_etiketi.text = "[X] Bağlantı Hatası! İnternetinizi kontrol edin."

if __name__ == "__main__":
    IPSorguUygulamasi().run()
