#!/usr/bin/env python3
# 基础代码安全风险检测（高危函数、注入风险）
import os
import re

risk_patterns = [
    (r"os\.system\(", "HIGH", "命令注入风险，禁止直接拼接用户输入"),
    (r"eval\(", "HIGH", "Eval 动态执行风险"),
    (r"exec\(", "HIGH", "Exec 代码执行风险"),
    (r"input\(", "MEDIUM", "未校验用户输入风险"),
    (r"http\.get\(", "MEDIUM", "未校验域名，存在SSRF风险"),
]


def scan_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        return

    for idx, line in enumerate(lines):
        for pat, level, msg in risk_patterns:
            if re.search(pat, line):
                print(f"[{level}] {path}:{idx+1} {msg} | CODE: {line.strip()}")


def walk_scan():
    for root, _, files in os.walk("."):
        if any(x in root for x in ["node_modules", ".git", "venv"]):
            continue
        for f in files:
            if f.endswith((".py", ".js", ".ts", ".go", ".java")):
                scan_file(os.path.join(root, f))


if __name__ == "__main__":
    walk_scan()
