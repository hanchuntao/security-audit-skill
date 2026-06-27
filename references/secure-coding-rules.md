---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 41b1ca04b8a988d8362f0617c7907a58_7502af5d722c11f1897e5254002afed2
    ReservedCode1: N0kKikHp9zWgACVZpUEb5OFa2MO811IzueQZqD1jmWqOzY2slVSFHEQPnLXZ8b13l2iYwyn7bdHEc61E6dcu8DskuoJyD0LNEw+wTu+zHkPQubnCGW2h8MxQUtWlzBoqNfQMHV18M6oGrR4kIK/HnVlD7SjJhr3u9CIKyRHDghfG57DVbNckCHaDvXc=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 41b1ca04b8a988d8362f0617c7907a58_7502af5d722c11f1897e5254002afed2
    ReservedCode2: N0kKikHp9zWgACVZpUEb5OFa2MO811IzueQZqD1jmWqOzY2slVSFHEQPnLXZ8b13l2iYwyn7bdHEc61E6dcu8DskuoJyD0LNEw+wTu+zHkPQubnCGW2h8MxQUtWlzBoqNfQMHV18M6oGrR4kIK/HnVlD7SjJhr3u9CIKyRHDghfG57DVbNckCHaDvXc=
---



# 团队安全编码规范

## 1. 密钥规范
- 禁止代码内硬编码任何密钥、凭证、Token
- 所有敏感配置必须使用环境变量/配置中心
- 禁止提交私钥、证书、密钥文件

## 2. 输入校验规范
- 所有外部入参必须做类型、长度、正则、白名单校验
- 禁止直接拼接SQL、命令、URL

## 3. 输出规范
- 禁止日志打印手机号、身份证、邮箱、密钥
- 接口返回禁止透传敏感字段

## 4. 依赖规范
- 禁止使用终止维护、存在高危CVE的版本
- 禁止引入测试版、非正式稳定依赖
*（内容由AI生成，仅供参考）*
*（内容由AI生成，仅供参考）*
