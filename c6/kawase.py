# 今日の為替レートを取得するプログラム
import json
import urllib.request

# 為替情報を得るクラス
class Kawase:
    # 為替情報の取得元（筆者のWebサイト）
    API = "http://api.aoikujira.com/kawase/json/usd"

    # 非公開のメソッド
    def __get_api(self):
        '''APIを使って今日のレート情報を取得する'''
        res = urllib.request.urlopen(Kawase.API)
        return res.read().decode('utf8')

    def __analize_result(self, json_str):
        '''取得したレート情報を解析する'''
        return json.loads(json_str)

    # 公開メソッド
    def get_result(self):
        '''APIから為替情報を取得する'''
        json_str = self.__get_api()
        return self.__analize_result(json_str)

    # 静的メソッド
    @staticmethod
    def get_usd_jpy():
        '''USD/JPYの結果を得る'''
        kawase = Kawase()
        data = kawase.get_result()
        usd = data.get("JPY", -1)
        return usd

# 本日の為替レート情報を表示
print("USD:JPY = 1:", Kawase.get_usd_jpy())
