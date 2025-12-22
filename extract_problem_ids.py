import pandas as pd

INPUT_FILE = 'submissions.csv'
OUTPUT_FILE = 'problem_ids.csv'

def extract_unique_problem_ids(input_file:str, output_file:str):
    unique_ids = set()
    chunk_size = 1000000 # 一度に読み込む行数

    for i, chunk in enumerate(pd.read_csv(input_file, usecols=['problem_id'], chunksize=chunk_size)):
        # 欠損値(NaN)を削除し、文字列型に統一してから unique を取得
        clean_ids = chunk['problem_id'].dropna().astype(str).unique()
        unique_ids.update(clean_ids)
        print(f"Processed {(i+1) * chunk_size} rows...")

    # 結果を保存
    pd.DataFrame(sorted(unique_ids), columns=['problem_id']).to_csv(output_file, index=False)
    print("Done!")

if __name__ == '__main__':
    extract_unique_problem_ids(INPUT_FILE, OUTPUT_FILE)