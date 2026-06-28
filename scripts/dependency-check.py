#!/usr/bin/env python3
# 简单依赖风险检测模板
import json


def check_deps():
    try:
        with open("requirements.txt", "r") as f:
            content = f.read()
            if "==" in content and ("2.7" in content or "3.6" in content):
                print("[HIGH] 发现老旧依赖包版本，存在已知CVE风险")
    except Exception:
        pass

    try:
        with open("package.json", "r") as f:
            pkg_json = json.load(f)
            deps = pkg_json.get("dependencies", {})
            for name, version in deps.items():
                if "0.0.1" in version or "beta" in version:
                    print(f"[MEDIUM] 测试版依赖包：{name}@{version}")
    except Exception:
        pass


if __name__ == "__main__":
    check_deps()
