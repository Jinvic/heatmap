import requests
import zhplot  # noqa 
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from collections import defaultdict
import os
import numpy as np
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# GitHub API 获取事件数据
def get_github_contributions(username, token, host, since_date):
    url = f"{host}/users/{username}/events"
    headers = {"Authorization": f"token {token}"}
    params = {
        "per_page": 100,
        "page": 1,
    }
    contributions = defaultdict(int)

    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"GitHub API 请求失败: {response.status_code}")
            break
        events = response.json()
        if not events:
            break
        for event in events:
            event_date = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ').date()
            if event_date < since_date:
                return contributions
            # if event['type'] == 'PushEvent':
            contributions[event_date] += 1
        params["page"] += 1

    return contributions

# GitLab API 获取事件数据
def get_gitlab_contributions(user_id, token, host, since_date):
    url = f"{host}/users/{user_id}/events"
    headers = {"PRIVATE-TOKEN": token}
    params = {
        "per_page": 100,
        "page": 1,
    }
    contributions = defaultdict(int)

    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"GitLab API 请求失败: {response.status_code}")
            break
        events = response.json()
        if not events:
            break
        for event in events:
            event_date = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
            if event_date < since_date:
                return contributions
            # if event['action_name'] == 'pushed to':
            contributions[event_date] += 1
        params["page"] += 1

    return contributions

# 合并数据并保存为CSV格式
def merge_contributions():
    merged = defaultdict(int)
    if config['github_accounts']:
        for github_account in config['github_accounts']:
            github_contributions = get_github_contributions(github_account['username'], github_account['token'], github_account['host'], since_date)
            for date, count in github_contributions.items():
                merged[date] += count
    if config['gitlab_accounts']:
        for gitlab_account in config['gitlab_accounts']:
            gitlab_contributions = get_gitlab_contributions(gitlab_account['user_id'], gitlab_account['token'], gitlab_account['host'], since_date)
            for date, count in gitlab_contributions.items():
                merged[date] += count

    # 创建dist目录
    os.makedirs("./dist", exist_ok=True)
    # 保存为CSV格式
    with open('./dist/merged_contributions.csv', 'w', encoding='utf-8') as f:
        f.write("date,count\n")
        for date, count in merged.items():
            f.write(f"{date},{count}\n")
    
    return merged

def plot_custom_calendar_heatmap(contributions, start_date, end_date):
    """
    生成一段时间内的网格状热力图
    :param contributions: 贡献数据，格式为 {日期: 贡献次数}
    :param start_date: 开始日期（datetime.date 对象）
    :param end_date: 结束日期（datetime.date 对象）
    """
    # 计算时间范围的总天数
    delta = (end_date - start_date).days + 1
    weeks = (delta + start_date.weekday()) // 7 + 1  # 计算总周数

    # 创建一个空的日历网格
    calendar = np.zeros((7, weeks))  # 7 行（星期几） x 周数
    calendar[:] = np.nan  # 初始化为 NaN

    # 填充数据
    for date_str, count in contributions.items():
        date = datetime.strptime(str(date_str), "%Y-%m-%d").date()
        if date < start_date or date > end_date:
            continue  # 跳过不在时间范围内的数据
        day_of_week = date.weekday()  # 星期几（0-6，0 是周一）
        week_of_range = (date - start_date).days // 7  # 计算在当前时间范围内的周数
        calendar[day_of_week, week_of_range] = count

    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    plt.figure(figsize=(weeks, 2))
    plt.imshow(calendar, cmap="YlGnBu", aspect="auto", vmin=0, vmax=max(contributions.values()))
    plt.colorbar(label="贡献次数")
    plt.title(f"{start_date} 到 {end_date} 的贡献热力图", fontsize=16)
    date_labels = [start_date + timedelta(days=i*7) for i in range(weeks)]
    plt.xticks(range(weeks), [date.strftime("%Y-%m-%d") for date in date_labels], rotation=45)
    
    plt.ylabel("星期几")
    plt.yticks(range(7), ["周一", "周二", "周三", "周四", "周五", "周六", "周日"])
    # plt.show()

    # 保存热力图
    plt.savefig("./dist/heatmap.png", bbox_inches="tight")
    plt.close()

# 示例使用
since_date = (datetime.now() - timedelta(days=int(config['expand_days']))).date()
contributions = merge_contributions()
plot_custom_calendar_heatmap(contributions, since_date, datetime.now().date())