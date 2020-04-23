#!/bin/sh

# コーパス中で頻出する述語と格パターンの組み合わせ
cat result/chapter5/result_45.txt | sort | uniq -c | sort -nr | head -n 30

# 「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
cat result/chapter5/result_45.txt | grep -- '^する[[:space:]]\|^見る[[:space:]]\|^与える[[:space:]]' | sort | uniq -c | sort -nr | head -n 30
