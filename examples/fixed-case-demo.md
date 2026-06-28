# 修复标准案例

## 案例 1：硬编码密钥 → 环境变量

```python
# ✅ 正确示例
import os

DB_PASSWORD = os.environ.get("DB_PASSWORD")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

def connect_db():
    conn = mysql.connect(password=DB_PASSWORD)
```

## 案例 2：SQL 注入 → 参数化查询

```python
# ✅ 正确示例
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
```

## 案例 3：命令注入 → subprocess + 参数校验

```python
# ✅ 正确示例
import subprocess
import re

def ping(host):
    if not re.match(r'^[a-zA-Z0-9.\-]+$', host):
        raise ValueError("Invalid host")
    subprocess.run(["ping", "-c", "4", host])
```
