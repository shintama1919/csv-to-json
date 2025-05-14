import sys
import os
import csv
import json

def csv_to_json(csv_path):
    # 入力ファイルのパスからJSONファイル名を生成
    base, _ = os.path.splitext(csv_path)
    json_path = base + ".json"

    # CSVを読み込み
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # JSONとして書き出し
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=4)
    print(f"変換完了: {json_path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("CSVファイルをドラッグ＆ドロップ、またはファイルパスを引数で指定してください。")
        input("エンターで終了")
        sys.exit(1)
    csv_file = sys.argv[1]
    if not os.path.exists(csv_file):
        print("指定されたCSVファイルが見つかりません。")
        input("エンターで終了")
        sys.exit(1)
    csv_to_json(csv_file)
    input("エンターで終了")
