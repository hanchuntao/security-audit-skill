#!/bin/bash
# 敏感信息泄露扫描脚本
set -euo pipefail

EXCLUDE_DIRS=(
  --exclude-dir=node_modules
  --exclude-dir=.git
  --exclude-dir=venv
  --exclude-dir=.venv
  --exclude-dir=dist
  --exclude-dir=build
  --exclude-dir=out
)

SECRET_PATTERN='(password|secret|token|ak|sk|access_key|private_key)="?.+"?'

echo "[Secret Scan] Start scanning hardcode secrets..."

grep -rnE "${SECRET_PATTERN}" \
  "${EXCLUDE_DIRS[@]}" \
  --exclude=*.log . || true

echo "[Secret Scan] Scan finished."
