# Atcoder_dataset_scraper


[Atcoder API](https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md)の`Datasets/Submissions`を利用している。

まず最初にrootディレクトリに`submissions.csv`を配置する。

### extract_contest_ids
コンテストID一覧を取得してCSV出力。

```console
python extract_contest_ids.py
```

### extract_problem_ids
問題ID一覧を取得してCSV出力。

```console
python extract_problem_ids.py
```

### find_degrade
ACからWAになった提出を検索してCSV出力。
現状は中身の変数を書き換えて使う。

``` console
python find_degrade.py
```
### get_src
find_degradeが作成したcsvを使ってsrcを取得する

``` console
python get_src.py
```

### submissions.csvメモ
CSVファイルであり、各行が以下の要素を持つ。右は例。

- `id` : 2003997
- `epoch_second` : 1516540436
- `problem_id` : arc089_b
- `contest_id` : arc089
- `user_id` : kenkoooo
- `language` : Rust (1.15.1)
- `point` : 0
- `length` : 3101
- `result` : WA
- `execution_time` : 88
