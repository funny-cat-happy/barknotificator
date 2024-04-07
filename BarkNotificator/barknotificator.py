import jwt
import httpx
import time
import os
from .exception import BarkNotificatorException


class BarkNotificator:
    _key: str
    _token: str = None
    _headers: dict
    _token_ttl: int
    _last_token_time: int
    _team_id: str
    _auth_key_id: str
    _device_token: str
    _ringtone: str

    def __init__(
        self,
        device_token: str,
        key_file_path: str = "default",
        token_ttl: int = 30 * 60,
        team_id: str = "5U8LBRXG3A",
        auth_key_id: str = "LH4T9V5U4R",
    ):
        """this class will configure the settings for bark notification.

        Args:
            device_token (str): your device token, you can get it from your bark app.
            key_file_path (str, optional): Apple push certificate. Defaults to the certificate carried by the package.
            token_ttl (int, optional): token valid time.Preferably within 30 to 60 minutes. Defaults to 30 minutes.
            team_id (str, optional): app team id. Defaults to "5U8LBRXG3A".
            auth_key_id (str, optional): app key id. Defaults to "LH4T9V5U4R".
        """

        key_file_path = (
            os.path.join(os.path.dirname(__file__), "key.p8")
            if key_file_path == "default"
            else key_file_path
        )
        with open(key_file_path, "r") as f:
            self._key = f.read()
        self._headers = {
            "host": "api.push.apple.com",
            "apns-topic": "me.fin.bark",
            "apns-push-type": "alert",
        }
        self._device_token = device_token
        self._token_ttl = token_ttl
        self._auth_key_id = auth_key_id
        self._team_id = team_id

    def send(
        self,
        content: str,
        title: str,
        target_url: str = None,
        ringtone: str = "bell.caf",
        category: str = None,
        icon_url: str = None,
    ):
        """this method will send a message to your device.

        Args:
            content (str): the content of the message to be sent.
            title (str): the title of the message to be sent.
            target_url (str, optional): the URL to jump to after clicking on the pop-up window. Defaults to None.
            ringtone (str, optional): ringtone. Defaults to "bell.caf".if you don't want to ring, set it to None.
            category (str, optional): category. Defaults to None.
            icon_url (str, optional): icon url. Defaults to None.
        Raises:
            BarkNotificatorException: _description_
        """
        now = int(time.time())
        if self._token is None or self._token_ttl < now - self._last_token_time:
            self.refresh_token()
        message = {
            "aps": {
                "mutable-content": 1,
                "alert": {
                    "title": title,
                    "body": content,
                },
            },
        }
        if ringtone is not None:
            message["aps"]["sound"] = ringtone
        if target_url is not None:
            message["url"] = target_url
        if category is not None:
            message["aps"]["category"] = category
        if icon_url is not None:
            message["icon"] = icon_url
        with httpx.Client(http2=True) as client:
            response = client.post(
                f"https://api.push.apple.com/3/device/{self._device_token}",
                headers=self._headers,
                json=message,
            )
            if not response.is_success:
                raise BarkNotificatorException(response.text)

    def refresh_token(self):
        self._last_token_time = int(time.time())
        self._token = jwt.encode(
            payload={"iss": self._team_id, "iat": self._last_token_time},
            key=self._key,
            algorithm="ES256",
            headers={"kid": self._auth_key_id},
        )
        self._headers["authorization"] = f"bearer {self._token}"
