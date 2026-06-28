# 典型漏洞案例

## 案例 1：硬编码密钥（Critical）

```python
# ❌ 错误示例
DB_PASSWORD = "admin123!@#"
AWS_ACCESS_KEY = "AKIA1234567890ABCDEF"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def connect_db():
    conn = mysql.connect(password="admin123!@#")
```

**风险**：密钥泄露导致数据泄露、资源被盗用。

**修复**：使用环境变量或配置中心。

## 案例 2：SQL 注入（Critical）

```python
# ❌ 错误示例
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
```

**风险**：攻击者可构造恶意 SQL 获取全量数据。

**修复**：使用参数化查询。

## 案例 3：命令注入（Critical）

```python
# ❌ 错误示例
def ping(host):
    os.system(f"ping -c 4 {host}")
```

**风险**：`host = "8.8.8.8; rm -rf /"` 可导致任意命令执行。

**修复**：使用 subprocess.run 并做参数校验。
