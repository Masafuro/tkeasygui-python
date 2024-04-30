# 互換性確認試験等

## 動作確認
- python 3.8.10
- tests内の.pyを実行
  - 実行結果
  - TypeError: 'type' object is not subscriptable
  - おそらくpython3.9以降を想定？
    - Typingモジュールで書き換える方法もあるが、、、？

- python 3.9.0
- tests内の.pyを実行
  - 特に問題なく動作している。
  - python3.9環境であれば、tests作成時に作者が動作確認しているものとみなしても良さそう。

## 使い分け
PySimpleGUIはpython3.6以降なので3.6~3.8を利用する場合、PySimpleGUIのバージョン4を利用すれば良さそう。

### GUIと接続
GUIと関係があり、急所となる接続先
1. Selenium
2. Excelファイル
3. Serial Port

ハード系は場合によっては3.9系についてきていない可能性もある。

ExcelはPandasやopenpyxlなどでアクセスできるのでよい。
Seleniumは組み込みの場合、ChromiunとセットでWebdriverを設置することになるのでバージョンが遅い傾向にある。
SerialPortは特に問題ないと思うが要確認

httpやmqttなどのネットワーク系は比較的早い傾向にあるので問題はあまりないか、実験の優先度は低いかも。
