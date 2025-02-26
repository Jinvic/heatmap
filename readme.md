# GitHub与GitLab合并热力图

## 简介

因为在两个平台都有提交,就简单写了这个合并来自GitHub和GitLab的提交数据，生成一张新的热力图。

## 功能

- 从GitHub和GitLab API获取提交数据
- 合并两者的提交数据
- 生成并保存热力图
- 支持自定义时间范围

## 环境要求

- Python 3.10
- 相关依赖库：`requests`, `matplotlib`, `numpy`, `pandas`, `python-dotenv`

## 本地部署

1. 克隆项目到本地：

   ```bash
   git clone <项目地址>
   cd <项目目录>
   ```

2. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

3. 配置环境变量：
   在项目根目录下创建一个`.env`文件，并添加以下内容：

   ```env
   GITHUB_USERNAME=你的GitHub用户名
   GITHUB_TOKEN=你的GitHub访问令牌
   GITLAB_USER_ID=你的GitLab用户ID
   GITLAB_TOKEN=你的GitLab访问令牌
   EXPAND_DAYS=60  # 可选，设置要分析的天数
   ```

4. 生成热力图:

运行`python main.py`命令生成热力图

## Github Actions

1. Fork项目
2. 配置Secret作为环境变量
3. 手动触发GitHub Actions

## TODO List

-[ ] 更多平台支持
-[ ] 更美观的热力图
