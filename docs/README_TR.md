# BarkNotificator
- [中文](/README.md)
- [English](docs/README_EN.md)
- [Türkçe](docs/README_TR.md)

Bu proje, Bark uygulaması yardımıyla bilgileri doğrudan Apple telefonlarına iletiyor
# Kullanım
## Kurulum
>pip install --upgrade barknotificator
## Demo
```python
from BarkNotificator import BarkNotificator

bark = BarkNotificator(device_token="Telefon Anahtarı")
bark.send(title="Merhaba!", content="Merhaba Dünya!")
```
![image](/docs/inform.jpg "Sonuç görüntüsü")
# Teşekkürler
- [Bark Offical](https://github.com/Finb/Bark)