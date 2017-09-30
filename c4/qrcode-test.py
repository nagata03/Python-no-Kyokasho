# パッケージをインポート
import qrcode
# QRコード
img = qrcode.make("http://kujirahand.com/")
# ファイルに保存
img.save("qrcode-test.png")
