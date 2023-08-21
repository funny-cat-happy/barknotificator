# BarkNotificator
- [中文](/README.md)
- [English](docs/README_EN.md)

This project pushes information directly to Apple phones with the help of the Bark app
# Usage
## Install
>pip install --upgrade barknotificator
## Demo
```python
from BarkNotificator import BarkNotificator

bark = BarkNotificator(device_token="your device token")
bark.send(title="welcome", content="hello world")
```
![image](/docs/inform.jpg "result image")
# Acknowledgment
- [Bark offical](https://github.com/Finb/Bark)