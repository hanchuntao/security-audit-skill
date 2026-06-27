#!/usr/bin/env python3
# 简单依赖风险检测模板
import json


def check_py_deps():
    try:
        with open("requirements.txt", "r") as f:
            content = f.read()
            if "==" in content and ("2.7" in content or "3.6" in content):
                print("[HIGH] 发现老旧Python版本依赖，存在已知CVE风险")
    except Exception:
        pass

    try:
        with open("package.json", "r") as f:
            data = json.load(f)
            deps = data.get("dependencies", {})
            for pkg, ver in deps.items():
                if "0.0.1" in ver or "beta" in ver:
                    print(f"[MEDIUM] 测试版依赖包：{pkg}@{ver}")
    except Exception:
        pass


if __name__ == "__main__":
    check_py_deps()
