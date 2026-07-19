import pandas as pd
import urllib.request
import time
import os
from html.parser import HTMLParser
from tqdm import tqdm

# --- 設定 ---
INPUT_CSV = "ac_wa_pairs.csv"
OUTPUT_DIR = "source_codes"
CONTEST_ID = "tessoku-book"
SLEEP_TIME = 1.5

# --- Parserクラス (変更なし) ---
class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.title = False
        self.link = False
        self.data = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "pre":
            self.data.append({})
            self.title = True
            self.link = True

    def handle_data(self, data):
        if self.title == True:
            self.data[-1].update({"code": data})
            self.title = False

# --- URLからコードを取得する関数 (変更なし) ---
def get_submission_code(url):
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
            }
        )
        with urllib.request.urlopen(req) as res:
            body = res.read().decode('utf-8')
            
        parser = Parser()
        parser.feed(body)
        parser.close()
        
        code = ""
        for i in parser.data:
            if "code" in i:
                code = i['code'].replace("\r\n", "\n").replace("\t", "    ")
                break
        
        if not code:
            return None
            
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
        
        ext = ".java"

        # --- ACの取得 ---
        ac_url = f"https://atcoder.jp/contests/{CONTEST_ID}/submissions/{ac_id}"
        ac_code = get_submission_code(ac_url)
        
        time.sleep(SLEEP_TIME) # AC取得後の待機

        # ACが失敗していたら WA は取りに行かずにスキップ
        if ac_code is None:
            print(f"Skipping {user_id}: AC fetch failed.")
            continue

        # --- WAの取得 ---
        wa_url = f"https://atcoder.jp/contests/{CONTEST_ID}/submissions/{wa_id}"
        wa_code = get_submission_code(wa_url)
        
        time.sleep(SLEEP_TIME) # WA取得後の待機

        # WAが失敗していたら 保存せずにスキップ
        if wa_code is None:
            print(f"Skipping {user_id}: WA fetch failed.")
            continue

        # --- 両方成功した場合のみ保存 ---
        if ac_code and wa_code:
            # ACの保存
            ac_filename = f"{OUTPUT_DIR}/{user_id}_{wa_id}/src_before/Main{ext}"
            os.makedirs(os.path.dirname(ac_filename), exist_ok=True)
            with open(ac_filename, "w", encoding='utf-8') as f:
                f.write(ac_code)

            # WAの保存
            wa_filename = f"{OUTPUT_DIR}/{user_id}_{wa_id}/src/Main{ext}"
            os.makedirs(os.path.dirname(wa_filename), exist_ok=True)
            with open(wa_filename, "w", encoding='utf-8') as f:
                f.write(wa_code)

if __name__ == "__main__":
    main()