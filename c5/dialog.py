#  ダイアログを表示するために必要なモジュールを取り込む
import tkinter.messagebox as mb # tkinterはPythonの標準ライブラリ

# ダイアログを表示
ans = mb.askyesno("質問", "ラーメンは好きですか？")  # 第一引数は「タイトル」、第二引数は「メッセージ」
# askyesno()関数は、YesかNoで答える質問のダイアログを表示する。
# Yesが押されるとTrueが、Noが押されるとFalseが返る。

if ans == True:
    # OKボタンがあるだけのダイアログを表示
    mb.showinfo("同意", "僕も好きです。")
else:
    mb.showinfo("本当？", "まさか、ラーメンが嫌いだなんて！")
