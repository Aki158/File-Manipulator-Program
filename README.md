# File-Manipulator-Program

## 🌱概要
コマンド入力を利用してファイル操作ができるスクリプト

## ✨デモ
![output](https://github.com/Aki158/File-Manipulator-Program/assets/119317071/1fd77005-e743-4fce-bfc1-37ea19c7c4ab)

## 📝説明
このスクリプトは、コマンド入力を利用してファイル操作ができるスクリプトです。

一般的なPC作業と言えば、下記のようなイメージを持たれているかもしれません。

- マウスを使用してファイルをコピーしたり、開いたりする

- キーボードでショートカットキーを使用する<br>(コピー`Ctrl + c`、貼り付け`Ctrl + v`...)

ソフトウェア開発者は、ターミナルという黒い画面にコマンドを入力して作業することがあります。

なぜ、ターミナルを使用するのでしょうか🤔?

ターミナルを使用すると、キーボードのみで作業が完結するため、マウスを使用する場合に比べて高速で、より多くの作業を迅速に実行することができます。

このスクリプトでは、ターミナルのコマンド入力を利用してファイルを操作することができます。

お目当てのコマンドが見つかれば、作業を効率化できるかもしれません!

💬「今の作業を効率化できるコマンドはないかな?」という目線で見ると楽しめます。

コマンドは、下記の4つを利用することができます。

各コマンドの機能の詳細は、[機能一覧](#機能一覧)を確認してください。

- reverse
- copy
- duplicate-contents
- replace-string

### 補足
[説明](#説明)で登場する用語について補足します。

用語の意味がわからない時は、下記表を確認してください。

| 用語 | 意味 |
| ------- | ------- |
| スクリプト | 一連のコマンドや命令を記述したテキストファイルのことで、コンピュータに特定のタスクを自動的に実行させるために使用されます。<br>スクリプトは、特定のスクリプト言語（例：Bash、Python、Perl、Ruby、JavaScriptなど）で書かれます。<br>今回は、Pythonを使用してスクリプトを作成しています。 |
| ターミナル | コンピュータに対してテキストベースのコマンド入力と出力を行うインターフェースのことです。<br>このインターフェースは、コマンドラインインターフェース（CLI）とも呼ばれます。<br>[デモ](#デモ)の左側に表示されている黒い画面のことです。 |
| コマンド | コンピュータに対して特定の操作を実行するよう指示するテキストベースの命令です。<br>コマンドを入力することで、コンピュータは、コマンドの意味を読み取りアクションをおこします。 |

## 🧰前提条件
このスクリプトを実行するには、下記ソフトウェアを事前にインストールしておく必要があります。

インストールされていない場合は、[インストール](#インストール)/[使用方法](#使用方法)/[使用例](#使用例)で記載されているコマンドが実行できませんので

必ずインストールしてから進めてください。

### Git
Gitがインストールされていない場合は、下記手順でインストールしてください。

1. ターミナルを起動する。<br>使用するOSによりターミナルの名称が異なりますので注意してください。<br>(例. Windows:コマンドプロンプト,mac:ターミナル)

2. Gitがインストールされているか確認する。<br>`git version 2.34.1` のように表示された場合は、Gitがインストールされています。<br>以降の手順はスキップしてください。<br>**また、ターミナルは引き続き使用しますので開いたままにしてください!**
```
git --version
```

3. システムを更新する
```
sudo apt-get update
```

4. Gitをインストールする
```
sudo apt install git
```

5. Gitがインストールされたことを確認する。<br>`git version 2.34.1` のように表示されていれば、Gitのインストールは完了です!
```
git --version
```

### Python 3.x
[Python](https://www.python.org/downloads/)の公式サイトからあなたのPCのOSに合わせて、ダウンロードしてください。

ダウンロードしたファイルを使用してインストールできます。

Pythonがインストールされているかは、下記コマンドで確認することができます。

`Python 3.10.12`のように表示されていれば、Pythonはインストールされています。

```
python3 --version
```

## 🍴インストール
### クローン
このスクリプトをあなたのPCで実行するために、クローンします。

クローンとは、このスクリプトの実行に必要なファイル(リポジトリのコンテンツ)をあなたのPCのローカル環境へコピーすることです。

下記手順でクローンしてください。

1. リポジトリをクローンする
```
git clone https://github.com/Aki158/File-Manipulator-Program.git
```

2. クローンしたリポジトリへ移動する
```
cd File-Manipulator-Program
```

## 🚀使用方法
1. ファイルを用意する
2. スクリプトを実行する
3. 生成されたファイルを確認する

## 🙋使用例
一通りの手順のイメージは[デモ](#デモ)を参考にしてください。

1. ファイルを用意する。<br>インプットとなるファイルを作成してください。<br>ファイルには、文章などのテキストが入力されている必要があります。<br>今回は、input.txtというファイルを作成し、`Hello world!`という文字を入力しておきました。
2. スクリプトを実行する。<br>スクリプトを利用する際は、ターミナルに[コマンドの入力例](#コマンドの入力例)のようなコマンドを入力します。<br>今回は、ファイル内の文字列を反転させたファイルが欲しかったので、[コマンドの入力使用例](#コマンドの入力使用例)のようにコマンドを入力しました。
3. 生成されたファイルを確認する。<br>output.txtというファイル内の文字列が反転されたファイルが生成されていました。

### 手順2の補足
#### コマンドの入力例
##### reverse
```
python3 file_manipulator.py reverse [inputpath] [outputpath]
```
| コマンド | 内容 |
| ------- | ------- |
| `[inputpath]`| 手順1.で用意したファイルのパスを入力します。<br>パスには、用意したファイルの名前まで含めてください。 |
| `[outputpath]`| スクリプトを利用することで、生成されるファイルのパスを入力します。<br>パスには、生成されるファイルの名前まで含めてください。 |

##### copy
```
python3 file_manipulator.py copy [inputpath] [outputpath]
```
| コマンド | 内容 |
| ------- | ------- |
| `[inputpath]`| 手順1.で用意したファイルのパスを入力します。<br>パスには、用意したファイルの名前まで含めてください。 |
| `[outputpath]`| スクリプトを利用することで、生成されるファイルのパスを入力します。<br>パスには、生成されるファイルの名前まで含めてください。 |

##### duplicate-contents
```
python3 file_manipulator.py duplicate-contents [inputpath] [n]
```

| コマンド | 内容 |
| ------- | ------- |
| `[inputpath]`| 手順1.で用意したファイルのパスを入力します。<br>パスには、用意したファイルの名前まで含めてください。 |
| `[n]`| ファイルの内容を読み込み、n回複製します。 |

##### replace-string
```
python3 file_manipulator.py replace-string [inputpath] [needle] [newstring]
```

| コマンド | 内容 |
| ------- | ------- |
| `[inputpath]`| 手順1.で用意したファイルのパスを入力します。<br>パスには、用意したファイルの名前まで含めてください。 |
| `[needle]`| 用意したファイル内に存在する文字列で、これから置換したい文字列を入力します。 |
| `[newstring]`| 置換後の文字列を入力します。 |

#### コマンドの入力使用例
```
python3 file_manipulator.py reverse ../python_practice/input.txt ../python_practice/output.txt
```

## 💾使用技術
<table>
<tr>
  <th>カテゴリ</th>
  <th>技術スタック</th>
</tr>
<tr>
  <td>開発言語</td>
  <td>Python</td>
</tr>
<tr>
  <td rowspan=2>インフラ</td>
  <td>Ubuntu</td>
</tr>
<tr>
  <td>VirtualBox</td>
</tr>
</table>

## 👀機能一覧
![image](https://github.com/Aki158/File-Manipulator-Program/assets/119317071/f653ea6e-90cf-4106-909a-c21545e1a12f)

| 機能 | 内容 |
| ------- | ------- |
| reverse | inputpathにあるファイルを受け取り、outputpathにinputpathの内容を逆にした新しいファイルを作成します。 |
| copy | inputpathにあるファイルのコピーを作成し、outputpathとして保存します。 |
| duplicate-contents | inputpathにあるファイルの内容を読み込み、その内容を複製し、複製されたinputにn回複製します。 |
| replace-string | inputpathにあるファイルの内容から文字列'needle'を検索し、'needle'を'newstring'に置き換えます。 |
| エラーハンドリング | コマンドが正しく入力されていない場合は、`Command not found...`というメッセージが表示されて終了します。<br>コマンドの入力は、認識されていないため、ファイルは生成されません。 |

## 📜作成の経緯
⭐️後で記載する!!!

作成した理由を記載する。

## ⭐️こだわった点
⭐️後で記載する!!!

テキストや参考にした記事などを再度読み返して技術の理解を深めてから書く。

ここがエンジニアに一番読んでもらいたい箇所なのでできるだけ詳細に書く。

## 📮今後の実装したいもの
- [ ] コマンドの追加
- [ ] 存在しないパスを入力した場合のエラーハンドリングの処理追加

## 📑参考文献
### 公式ドキュメント
- [Python](https://docs.python.org/ja/3/)

### 参考にしたサイト
- [Python_Download](https://www.python.org/downloads/)
