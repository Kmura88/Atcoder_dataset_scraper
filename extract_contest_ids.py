import csv
import os

INPUT_FILE = 'submissions.csv' 
OUTPUT_FILE = 'contest_ids.csv'

def extract_unique_contest_ids(input_path, output_path):
    unique_ids = set()
    
    print(f"Reading from {input_path}...")
    
    try:
        with open(input_path, mode='r', encoding='utf-8', newline='') as infile:
            # ヘッダーを読み込んで contest_id の列番号（インデックス）を特定する
            reader = csv.reader(infile)
            header = next(reader, None)
            
            if not header:
                print("Error: File is empty.")
                return

            try:
                # 'contest_id' カラムが何列目にあるか探す
                contest_id_index = header.index('contest_id')
            except ValueError:
                print("Error: 'contest_id' column not found in header.")
                return

            # 1行ずつ読み込んでセットに追加（メモリ節約のためDictReaderではなくreaderを使用）
            for i, row in enumerate(reader):
                if row and len(row) > contest_id_index:
                    unique_ids.add(row[contest_id_index])
                
                # 進捗表示
                if (i + 1) % 1_000_000 == 0:
                    print(f"Processed {i + 1} rows...")

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
        return

    print(f"Finished reading. Found {len(unique_ids)} unique contest IDs.")
    print(f"Writing to {output_path}...")

    # 結果をCSV出力
    with open(output_path, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['contest_id'])  # ヘッダー
        
        # ソートして書き出し
        for contest_id in sorted(unique_ids):
            writer.writerow([contest_id])

    print("Done!")

if __name__ == '__main__':
    extract_unique_contest_ids(INPUT_FILE, OUTPUT_FILE)