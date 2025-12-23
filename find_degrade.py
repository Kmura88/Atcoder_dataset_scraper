import pandas as pd

INPUT_FILE = "submissions.csv"
OUTPUT_FILE = "ac_wa_pairs.csv"
PROBLEM_ID = "tessoku_book_a"
LANGUAGE = "Java"

"""
languageは
Java (OpenJDK 17)
Java8 (OpenJDK 1.8.0)
のように書式にばらつきがあるので先頭一致で判定している。
"""

def find_ac_wa_pairs(input_file:str, output_file:str, problem_id:str=None, language:str=None):
	print(f"--- Start Process find_ac_wa_pairs ---")

	# 1. 読み込み
	df = pd.read_csv(
		input_file,
		usecols=['id', 'epoch_second', 'problem_id', 'user_id', 'result', 'language']
	)

	# 2. 問題ID, languageで絞る
	if problem_id:
		df = df[df['problem_id'] == problem_id]
	if language:
		# 言語が "Java" の場合のみ、JavaScript を除外する処理を追加
		if language == "Java":
			df = df[
				df['language'].str.startswith("Java", na=False) & 
				~df['language'].str.startswith("JavaScript", na=False)
			]
		else:
			# それ以外は通常通り前方一致
			df = df[df['language'].str.startswith(language, na=False)]

	# 3. ACとWAだけに絞り、ユーザー・時間順にソート
	# これにより、並び順は必ず ... -> AC -> WA -> ... のようになります
	df = df[df['result'].isin(['AC', 'WA'])]
	df = df.sort_values(['user_id', 'epoch_second'])

	# 4. ユーザーごとに「1つ前の行」の情報を取得して列に追加
	df['prev_result'] = df.groupby('user_id')['result'].shift(1)
	df['prev_id']     = df.groupby('user_id')['id'].shift(1)
	df['prev_epoch']  = df.groupby('user_id')['epoch_second'].shift(1)

	# 5. 条件フィルタリング
	# 「現在の結果がWA」 かつ 「直前の結果がAC」 の行を抽出
	target_df = df[
		(df['result'] == 'WA') & 
		(df['prev_result'] == 'AC')
	]

	# 6. 列を整理してリネーム
	output_df = target_df[[
		'user_id', 
		'prev_id', 'prev_epoch',   # 直前のACの情報
		'id', 'epoch_second'       # 現在のWAの情報
	]].copy()

	output_df.columns = ['user_id', 'ac_id', 'ac_epoch', 'wa_id', 'wa_epoch']

	# floatになった列をintに戻す 
	output_df['ac_id'] = output_df['ac_id'].astype(int)
	output_df['ac_epoch'] = output_df['ac_epoch'].astype(int)

	# 保存
	output_df.to_csv(output_file, index=False)
	print(f"Found {len(output_df)} pairs. Saved to {output_file}")
	
	# 確認用表示
	if len(output_df) > 0:
		print("\n--- Preview ---")
		print(output_df.head())

if __name__ == '__main__':
	find_ac_wa_pairs(INPUT_FILE, OUTPUT_FILE, PROBLEM_ID , LANGUAGE)