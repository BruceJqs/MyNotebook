# Seed-Wheel 细化想法补充

## RAG 引擎

- 数据源：
	- 文本：杜老师 SEED 书、SEED 实验讲解及要求、SEED-emulator 相关论文（涉及 emulator 手册等等）、网络资料（涉及联网搜索）、附加资料（例如历年优秀实验 Report）
	- 视频：杜老师网课
	- 图片：所有除文本资料以外的图片资料（可能涉及打 tag）

可以 Seedlab 与 Seed-Emulator 分开（？）
***
## 伴学模块

- 启发式、引导性的提问：通过 Prompt 设置
- 一个 Agent，LLM 配备 RAG 引擎，可以涉及反思的 Workflow
***
## 助研模块

一个 Agent，配备 RAG 引擎，反思 Workflow 以及动态 RAG 更新

- 可能涉及大量 MCP 模块
	- 自动 Emulator 代码生成：代码运行建立 docker 网络并验证 MCP 工具
	- 文献处理：PDFMathTranslate 等 MCP 工具
	- 最新研究动态：调用外部 API（例如 Github，Arxiv 等）MCP 工具
***
## 助教模块

一个 Agent，配备 RAG 引擎（用于后续推送相关习题），动态 RAG 更新

- 可能涉及大量 MCP 模块
	- Moodle 后台管理、数据库等资源获取
	- 会话日志记录备份审核
***
