#!/usr/bin/env python3
# 基础代码安全风险检测（高危函数、注入风险）
import os
import re

EXCLUDED_DIRS = {".git", "node_modules", "venv", ".venv", "dist", "build", "out", "examples", "references"}

risk_patterns = [
    (r"os\.system\(", "HIGH", "命令注入风险，禁止直接拼接用户输入"),
    (r"eval\(",       "HIGH", "Eval 动态执行风险"),
    (r"exec\(",       "HIGH", "Exec 代码执行风险"),
    (r"input\(",      "MEDIUM", "未校验用户输入风险"),
    (r"http\.get\(",  "MEDIUM", "未校验域名，存在SSRF风险"),
]

SCAN_EXTENSIONS = (".py", ".js", ".ts", ".go", ".java")


def scan_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
    except Exception:
        return

    for lineno, line in enumerate(lines, start=1):
        for pattern, level, message in risk_patterns:
            if re.search(pattern, line):
                print(f"[{level}] {filepath}:{lineno} {message} | CODE: {line.strip()}")


def walk_scan():
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for filename in files:
            if filename.endswith(SCAN_EXTENSIONS):
                scan_file(os.path.join(root, filename))


if __name__ == "__main__":
    walk_scan()
