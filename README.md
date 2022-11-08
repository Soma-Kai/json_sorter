1.概要
　本CLIツールはjsonファイルを受け取り、その要素を各idに基づいてsortするツールである。

2.動作環境
　zshで実行可能
　Python3.9.6

3.使い方
　./json_sorter -option element
  
  とすることでoptionをelementに設定できる。

  optionについて
  　-type
  	insetion quick merge　の3種類から選択可能　デフォルトはinsertion

　　-json
	ソートしたいjsonのファイル名を入力　デフォルトはtestディレクトリに存在するテストファイル　./test/users.json

　　-output
	アウトプットするjsonファイル名を入力　デフォルトはsample.json

3.ファイルツリー
　app -- src ソースコード
       |
       - output アウトプットファイルが格納されるディレクトリ
       |
       - test テスト用json fileを格納
