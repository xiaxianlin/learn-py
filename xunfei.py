from websocket import WebSocketApp, enableTrace
import datetime
import hashlib
import base64
import hmac
import json
from urllib.parse import urlencode
import ssl
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime, sleep
import _thread as thread


STATUS_FIRST_FRAME = 0  # 第一帧的标识
STATUS_CONTINUE_FRAME = 1  # 中间帧标识
STATUS_LAST_FRAME = 2  # 最后一帧的标识


class SparkParams(object):
    app_id = None
    api_key = None
    api_secret = None
    # 音频编码
    aue = "lame"
    # 开始流式返回
    sfl = 1
    # 音频采样率
    auf = "audio/L16;rate=16000"
    # 音色
    vcn = "xiaoyan"
    # 语速
    speed = 50
    # 音量
    volume = 50
    # 音高
    pitch = 50
    # 合成音频的背景音
    bgs = 0
    # 文本编码格式
    tte = "UTF8"
    # 英文发音方式
    reg = "2"
    # 合成音频数字发音方式
    rdn = "0"

    common: dict = None
    business: dict = None

    # 初始化
    def __init__(self, *, app_id, api_key, api_secret):
        self.app_id = app_id
        self.api_key = api_key
        self.api_secret = api_secret

        # 公共参数(common)
        self.common = {"app_id": self.app_id}
        # 业务参数(business)，更多个性化参数可在官网查看
        self.business = {
            "aue": self.aue,
            "sfl": self.sfl,
            "auf": self.auf,
            "vcn": self.vcn,
            "speed": self.speed,
            "volume": self.volume,
            "pitch": self.pitch,
            "bgs": self.bgs,
            "tte": self.tte,
            "reg": self.reg,
            "rdn": self.rdn,
        }

    # 生成url
    def create_url(self):
        url = "wss://tts-api.xfyun.cn/v2/tts"
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + "ws-api.xfyun.cn" + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + "/v2/tts " + "HTTP/1.1"
        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(
            self.api_secret.encode("utf-8"),
            signature_origin.encode("utf-8"),
            digestmod=hashlib.sha256,
        ).digest()
        signature_sha = base64.b64encode(signature_sha).decode(encoding="utf-8")

        authorization_origin = (
            'api_key="%s", algorithm="%s", headers="%s", signature="%s"'
            % (self.api_key, "hmac-sha256", "host date request-line", signature_sha)
        )
        authorization = base64.b64encode(authorization_origin.encode("utf-8")).decode(
            encoding="utf-8"
        )
        # 将请求的鉴权参数组合为字典
        v = {"authorization": authorization, "date": date, "host": "ws-api.xfyun.cn"}
        # 拼接鉴权参数，生成url
        url = url + "?" + urlencode(v)
        return url


class SparkTTSCallback:
    def on_open(self):
        pass

    def on_message(self, data: bytes):
        pass

    def on_error(self, error):
        pass

    def on_close(self):
        pass


class SparkTTS:
    url: str = None
    payload: dict = None
    callback: SparkTTSCallback = None

    def __init__(self, params: SparkParams, callback: SparkTTSCallback) -> None:
        self.payload = {"common": params.common, "business": params.business}
        self.url = params.create_url()
        self.callback = callback

    def _on_message(self, ws, message):
        try:
            message = json.loads(message)
            sid = message["sid"]
            code = message["code"]
            status = message["data"]["status"]
            print("sid:%s call code is:%s" % (sid, code))

            if status == 2:
                ws.close()

            if code == 0:
                self.callback.on_message(base64.b64decode(message["data"]["audio"]))
            else:
                self.callback.on_error(ValueError(message["message"]))

        except Exception as e:
            self.callback.on_error(e)

    def _on_error(self, _, error):
        self.callback.on_error(error)

    def _on_close(self, _a, _b, _c):
        print("websocket closed")
        self.callback.on_close()

    def _on_open(self, ws):
        self.callback.on_open()
        print(f"===> 发送文本：{self.text}")
        self.payload["data"] = {
            "status": 2,
            "text": str(base64.b64encode(self.text.encode("utf-8")), "UTF8"),
        }

        payload = json.dumps(self.payload)

        thread.start_new_thread(ws.send, (payload,))

    def call(self, text):
        enableTrace(False)
        self.text = text
        self.ws = WebSocketApp(
            self.url,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close,
        )

        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


if __name__ == "__main__":
    # 测试时候在此处正确填写相关信息即可运行
    parms = SparkParams(
        app_id="",
        api_key="",
        api_secret="",
    )

    file = None

    class Callback(SparkTTSCallback):
        def on_open(self):
            global file
            file = open("demo.mp3", "wb")

        def on_message(self, data: bytes):
            global file
            if file:
                file.write(data)
                file.flush()

        def on_close(self):
            global file
            if file:
                file.close()

        def on_error(self, error):
            print(error)

    test_text = [
        "默认采样率代表当前音色的最佳采样率，",
        "缺省条件下默认按照该采样率输出，",
        "同时支持降采样或升采样。",
    ]

    tts = SparkTTS(parms, callback=Callback())
    for text in test_text:
        tts.call(text)
