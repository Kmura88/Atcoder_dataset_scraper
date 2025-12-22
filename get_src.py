import pandas as pd
import urllib.request
import time
import os
from html.parser import HTMLParser
from tqdm import tqdm

# --- 設定 ---
INPUT_CSV = "ac_wa_pairs.csv"  # 前回の出力ファイル
OUTPUT_DIR = "source_codes"    # 保存先フォルダ
CONTEST_ID = "typical90"       # 対象の問題ID (コンテストID特定に使用)
SLEEP_TIME = 1.5               # アクセス間隔(秒) ※重要: 1秒以上あけること

# --- Parserクラス ---
class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.title = False
        self.link = False
        self.data = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        # AtCoderのソースコードは <pre id="submission-code"> 等で囲まれています
        if tag == "pre":
            self.data.append({})
            self.title = True
            self.link = True

    def handle_data(self, data):
        if self.title == True:
            self.data[-1].update({"code": data})
            self.title = False

# --- URLからコードを取得する関数 ---
def get_submission_code(url):
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            body = res.read().decode('utf-8') # decodeを追加
            
        parser = Parser()
        parser.feed(body)
        parser.close()
        
        code = ""
        # 抽出したデータの整形
        for i in parser.data:
            if "code" in i:
                code = i['code'].replace("\r\n", "\n").replace("\t", "    ")
                break
        return code
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# --- メイン処理 ---
def main():
    # 1. 保存先ディレクトリの作成
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 2. CSV読み込み
    print(f"Loading {INPUT_CSV}...")
    df = pd.read_csv(INPUT_CSV)
    
    print(f"Target Contest: {CONTEST_ID}")
    print(f"Total pairs to download: {len(df)}")

    # 3. ループ処理
    for index, row in tqdm(df.iterrows(), total=len(df)):
        user_id = row['user_id']
        ac_id = row['ac_id']
        wa_id = row['wa_id']
        
        # ファイルの拡張子を簡易判定 (Java想定)
        # 必要に応じて row['ac_lang'] の中身を見て分岐してください (.py, .cpp 等)
        ext = ".java" 

        # --- ACの取得 ---
        ac_url = f"https://atcoder.jp/contests/{CONTEST_ID}/submissions/{ac_id}"
        ac_code = get_submission_code(ac_url)
        
        if ac_code:
            filename = f"{OUTPUT_DIR}/{user_id}_{ac_id}_AC{ext}"
            with open(filename, "w", encoding='utf-8') as f:
                f.write(ac_code)
        
        time.sleep(SLEEP_TIME) # 待機

        # --- WAの取得 ---
        wa_url = f"https://atcoder.jp/contests/{CONTEST_ID}/submissions/{wa_id}"
        wa_code = get_submission_code(wa_url)
        
        if wa_code:
            filename = f"{OUTPUT_DIR}/{user_id}_{wa_id}_WA{ext}"
            with open(filename, "w", encoding='utf-8') as f:
                f.write(wa_code)

        time.sleep(SLEEP_TIME) # 待機

if __name__ == "__main__":
    main()