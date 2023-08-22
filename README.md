# BarkNotificator
- [中文](/README.md)
- [English](docs/README_EN.md)
- [Türkçe](docs/README_TR.md)


此项目可以借助Bark直接向苹果手机推送信息
# 使用方法
## 安装
>pip install --upgrade barknotificator
## 示例
```python
from BarkNotificator import BarkNotificator

bark = BarkNotificator(device_token="your device token")
bark.send(title="welcome", content="hello world")
```
![image](/docs/inform.jpg "结果图片")
# 感谢
- [Bark官方](https://github.com/Finb/Bark)
