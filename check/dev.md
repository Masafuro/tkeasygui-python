# 互換性確認試験等

## 動作確認
- python 3.8.10
- tests内の.pyを実行
  - 実行結果
  - TypeError: 'type' object is not subscriptable
  - おそらくpython3.9以降を想定？
    - Typingモジュールで書き換える方法もあるが、、、？

## 使い分け
PySimpleGUIはpython3.6以降なので3.6~3.8を利用する場合、PySimpleGUIのバージョン4を利用すれば良さそう。


