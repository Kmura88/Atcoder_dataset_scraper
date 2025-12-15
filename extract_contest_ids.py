import pandas as pd

INPUT_FILE = 'submissions.csv'
OUTPUT_FILE = 'contest_ids.csv'

def extract_unique_contest_ids(input_file:str, output_file:str):
    unique_ids = set()
    chunk_size = 1000000 # 一度に読み込む行数

    for i, chunk in enumerate(pd.read_csv(input_file, usecols=['contest_id'], chunksize=chunk_size)):
        unique_ids.update(chunk['contest_id'].unique())
        print(f"Processed {(i+1) * chunk_size} rows...")

    # 結果を保存
    pd.DataFrame(sorted(unique_ids), columns=['contest_id']).to_csv(output_file, index=False)
    print("Done!")

if __name__ == '__main__':
    extract_unique_contest_ids(INPUT_FILE, OUTPUT_FILE)