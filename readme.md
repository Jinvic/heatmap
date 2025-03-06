# 热力图合并

## 简介

因为在两个平台都有提交,就简单写了这个合并来自GitHub和GitLab的贡献数据，生成一张新的热力图。

## 功能

- 从GitHub和GitLab API获取事件数据
- 合并两者的数据
- 生成并保存热力图
- 支持自定义时间范围

## 环境要求

- Python 3.10
- 相关依赖库：`requests`, `matplotlib`, `numpy`, `zhplot`, `PyYAML`

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
   在项目根目录下创建一个`config.yaml`文件，并添加以下内容：

   ```yaml
   github_accounts:
   - username: 账户1的GitHub用户名
      token: 账户1的GitHub访问令牌
      host: 账户1的GitHub主机地址
   - username: 账户2的GitHub用户名
      token: 账户2的GitHub访问令牌
      host: 账户2的GitHub主机地址

   gitlab_accounts:
   - user_id: 账户1的GitLab用户ID
      token: 账户1的GitLab访问令牌
      host: 账户1的GitLab主机地址
   - user_id: 账户2的GitLab用户ID
      token: 账户2的GitLab访问令牌
      host: 账户2的GitLab主机地址

   expand_days: 要分析的天数
   ```

4. 生成热力图:

运行`python main.py`命令生成热力图

## Github Actions

1. Fork项目
2. 创建名为CONFIG_YAML的secret
3. 按照`config.yaml.example`的格式填写配置
4. 手动触发GitHub Actions

## TODO List

- [x] 多账户支持
- [ ] 更多平台支持
- [ ] 更美观的热力图
