#!/bin/sh

# コーパス中で頻出する述語（サ変接続名詞+を+動詞）
cat result/chapter5/result_47.txt | cut -f1 | sort | uniq -c | sort -nr

# コーパス中で頻出する述語と助詞パターン
cat result/chapter5/result_47.txt | cut -f1-2 | sort | uniq -c | sort -nr | head -n 30
