---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 41b1ca04b8a988d8362f0617c7907a58_743d351d722c11f1897e5254002afed2
    ReservedCode1: G6KnM2327d4O1MHCoT18yfyaTrsFEL+qXRmSNb13aY6d32U8Vn8b0SGTa7N0Wk9zm4df6gBZgj4zjbMaApUiy05MKbdQWMORgkEOtuVWPFwrFNAFeROif0vC7bYlJIJ7odvaRVJHg9pHRNJB6Krcm+2eCqcjc/QMbAzuJaxPGbBrq5XGLOTMpyXEHtE=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 41b1ca04b8a988d8362f0617c7907a58_743d351d722c11f1897e5254002afed2
    ReservedCode2: G6KnM2327d4O1MHCoT18yfyaTrsFEL+qXRmSNb13aY6d32U8Vn8b0SGTa7N0Wk9zm4df6gBZgj4zjbMaApUiy05MKbdQWMORgkEOtuVWPFwrFNAFeROif0vC7bYlJIJ7odvaRVJHg9pHRNJB6Krcm+2eCqcjc/QMbAzuJaxPGbBrq5XGLOTMpyXEHtE=
---



# Security Workflow 企业安全审计技能

## 能力总览

本 Skill 为标准化、可落地的**生产级代码安全质检工作流**，适配线上环境安全合规要求，统一团队安全代码规范，自动识别并修复常见高危漏洞，杜绝密钥泄露、注入漏洞、权限绕过、不安全配置、依赖漏洞等线上风险，保障生产代码安全稳定。

支持语言：Python / Java / Go / JavaScript / TypeScript / Shell / YAML / JSON

## 扫描覆盖范围（生产高危必查）

### 1. 密钥与敏感信息泄露
- 硬编码 AK/SK、Token、Password、Secret
- 明文账号密码、数据库凭证、私钥
- 注释内隐藏敏感信息

### 2. 代码高危漏洞
- SQL 注入、命令注入、XSS、SSRF、文件遍历
- 不安全正则、不安全随机数、弱加密
- 未过滤用户输入、危险函数调用

### 3. 依赖与组件风险
- 高危 CVE 依赖包、过期废弃组件
- 不安全版本锁定、开发依赖混入生产包

### 4. 安全规范合规
- 权限校验缺失、参数未校验
- 日志泄露敏感数据
- 调试代码残留、后门代码、冗余测试接口

## 执行工作流（固定 6 步标准流程）

### 步骤1：初始化扫描配置
读取当前技能 config.json 配置，加载扫描阈值、黑白名单、豁免目录、风险等级定义，启用生产严格模式。

### 步骤2：全量文件扫描
通过 Glob 遍历项目源码目录，跳过 node_modules、venv、dist、build 等编译目录；对源码、配置、脚本文件执行多维度安全检测。

### 步骤3：多引擎规则校验
1. 调用 secret-scan.sh 扫描敏感信息泄露
2. 调用 lint-security.py 扫描代码逻辑漏洞
3. 调用 dependency-check.py 检测依赖风险
4. 对照 references 安全编码规范与 CWE 高危清单合规校验

### 步骤4：风险分级定级
严格按照四级生产风险分级，适配上线准入标准：
- **Critical**：阻断上线、必须立即修复、禁止合并生产分支
- **High**：本轮迭代必须修复、禁止提交生产
- **Medium**：限期整改、纳入迭代风控
- **Low**：建议优化、纳入技术债务，不阻断上线

### 步骤5：自动修复与提示
生产环境仅**自动修复低风险规范类问题**（格式不规范、冗余调试代码等）；中高、高危风险仅输出精准告警、不自动修改业务代码，避免影响生产稳定性，同步输出代码行、风险原理、整改方案、合规依据。

### 步骤6：生成标准化审计报告
基于 report 模板输出结构化报告：风险汇总、漏洞清单、位置定位、修复建议、合规结论，留存生产审计记录。

## 输出规范
1. 所有问题必须标注：文件路径 + 行号 + 风险等级 + 漏洞描述
2. 每条问题必须附带：修复方案 + 错误原因 + 合规依据
3. 高危问题必须明确告知：是否阻断提交/上线
4. 最终输出整体安全评分与整改完成度

## 使用指令
- `/security-audit` 全项目安全扫描
- `/security-fix` 自动修复可处理低风险问题
- `/security-report` 生成完整审计报告
- `/security-check-file` 检查当前单个文件

## 生产环境约束与边界
1. 严格隔离业务代码，不修改业务核心逻辑，仅修复低风险安全规范问题
2. 遵循最小权限原则，仅扫描业务源码目录，无越权访问、修改能力
3. 所有扫描、修改记录可追溯、可逆、可复盘，满足生产合规审计
4. 跳过第三方依赖、编译产物、静态资源、文档目录，不产生无效扫描
5. 高危风险强制拦截，杜绝带漏洞代码上线，保障生产环境安全
*（内容由AI生成，仅供参考）*
