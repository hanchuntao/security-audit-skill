#!/bin/bash
# 敏感信息泄露扫描脚本
set -e

echo "[Secret Scan] Start scanning hardcode secrets..."

grep -rnE \
  '(password|secret|token|ak|sk|access_key|private_key)="?.+"?' \
  --exclude-dir=node_modules --exclude-dir=.git \
  --exclude=*.log .

echo "[Secret Scan] Scan finished."
