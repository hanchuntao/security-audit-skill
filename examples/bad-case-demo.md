---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 41b1ca04b8a988d8362f0617c7907a58_76f1e034722c11f1897e5254002afed2
    ReservedCode1: nrGKbAd1O9Mk0WKUfdK8ieYVl1FmGyiKU3VOGUtTF++pqdx33+PFiAoXIJXDNplqxErNvzEpT7X8S34RgZdfo+H3n1gtum80q5wCpA67BeJ4JfPcjjN3mZ3fKrtGHYCm4X/QXZoGEZbKVWWAGgaOYCsZwB8miNmF38xOmn0o4kpMUjya0dVQz2ni9+w=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 41b1ca04b8a988d8362f0617c7907a58_76f1e034722c11f1897e5254002afed2
    ReservedCode2: nrGKbAd1O9Mk0WKUfdK8ieYVl1FmGyiKU3VOGUtTF++pqdx33+PFiAoXIJXDNplqxErNvzEpT7X8S34RgZdfo+H3n1gtum80q5wCpA67BeJ4JfPcjjN3mZ3fKrtGHYCm4X/QXZoGEZbKVWWAGgaOYCsZwB8miNmF38xOmn0o4kpMUjya0dVQz2ni9+w=
---



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
*（内容由AI生成，仅供参考）*
*（内容由AI生成，仅供参考）*
