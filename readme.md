# 热力图合并

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
   git clone https://github.com/Jinvic/heatmap
   cd heatmap
   ```

2. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

3. 配置环境变量：
   在项目根目录下创建一个`.env`文件，并添加以下内容：

   ```env
    _GITHUB_USERNAME=你的GitHub用户名
    _GITHUB_TOKEN=你的GitHub访问令牌
    _GITHUB_API_HOST=https://api.github.com
    _GITLAB_USER_ID=你的GitLab用户ID
    _GITLAB_TOKEN=你的GitLab访问令牌
    _GITLAB_API_HOST=https://gitlab.com/api/v4  # 支持自建的GitLab仓库
    _EXPAND_DAYS=60  # 可选，设置要分析的天数
   ```

4. 生成热力图:

运行`python main.py`命令生成热力图

## Github Actions

1. Fork项目
2. 配置Secret作为环境变量
3. 手动触发GitHub Actions

## TODO List

- [x] 多账户支持
- [ ] 更多平台支持
- [ ] 更美观的热力图
