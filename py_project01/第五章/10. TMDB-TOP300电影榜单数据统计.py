import os

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from pandas import Series

# 当前文件所在目录（保证从任意工作目录运行都能找到 data 目录）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# 展示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题


# ==================== 数据加载 ====================
def load_data(file_path: str) -> pd.DataFrame:
    """加载电影数据，并处理年份缺失值"""
    # int64 : 整型数字（不支持空值）;
    # Int64 : 整型数字（支持空值）
    # float64 : 浮点型数字（支持空值）;
    data = pd.read_csv(file_path, usecols=['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言'],
                       dtype={'年份': 'Int64'})

    # 年份缺失时，从上映时间中截取
    data['年份'] = data['年份'].fillna(data['上映时间'].str[:4])
    return data


# ==================== 各需求的数据统计 ====================
def get_year_data(data: pd.DataFrame) -> tuple[list[int], list[int]]:
    """需求一：统计 TOP300 电影中每年上映的电影数量"""
    year_count = data.groupby('年份')['年份'].count()

    # x轴数据: 完整的年份区间
    min_year = year_count.index.min()
    max_year = year_count.index.max()
    x = [i for i in range(min_year, max_year + 1)]

    # y轴数据: 没有数据的年份补 0
    y = [int(year_count.get(i, 0)) for i in x]
    return x, y


def get_language_data(data: pd.DataFrame) -> tuple[list[str], list[int]]:
    """需求二：统计不同语言的电影数量（降序）"""
    language_count = data.groupby('语言')['语言'].count().sort_values(ascending=False)
    return language_count.index.tolist(), language_count.values.tolist()


def get_type_data(data: pd.DataFrame) -> tuple[list[str], list[int]]:
    """需求三：统计不同类型电影数量（一部电影可能有多个类型）"""
    type_count: dict[str, int] = {}  # {'剧情': 5, '犯罪': 3}
    for types in data['类型'].str.split(','):  # [剧情, 犯罪]
        for movie_type in types:  # 剧情
            type_count[movie_type] = type_count.get(movie_type, 0) + 1
    return list(type_count.keys()), list(type_count.values())


def get_score_data(data: pd.DataFrame) -> tuple[list[int], list[int]]:
    """需求四：统计不同评分的电影数量占比，比例 < 2% 的合并为『其他』"""
    score_count = data.groupby('评分')['评分'].count()

    total = score_count.sum()
    large_scores: Series = score_count.loc[score_count >= total * 0.02]  # 大数据, 比例 >= 2%
    small_scores: Series = score_count.loc[score_count < total * 0.02]  # 小数据, 比例 < 2%
    if small_scores.shape[0] > 0:
        large_scores['其他'] = small_scores.sum()

    return large_scores.index.tolist(), large_scores.values.tolist()


# ==================== 绘图 ====================
def create_canvas() -> tuple[Figure, list[list[Axes]]]:
    """创建 2x2 的画布和子图"""
    # figure: 画布对象; axes: 子图数组(里面存放的是 Axes 类型的对象)
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    fig.suptitle('TMDB-TOP300电影榜单数据统计', fontsize=23, x=0.5, y=0.98)  # 画布标题 - x/y: 标题位置
    fig.subplots_adjust(hspace=0.5, wspace=0.2)  # 子图间距, hspace: 垂直间距, wspace: 水平间距
    return fig, axes


def plot_year_line(axes: Axes, x: list[int], y: list[int]) -> None:
    """需求一：每年电影数量变化折线图"""
    axes.plot(x, y, color='green')
    axes.set_title('每年电影数量变化折线图', fontsize=18)
    axes.set_xlabel('年份', fontsize=12)
    axes.set_ylabel('电影数量', fontsize=12)
    axes.set_xticks(x[::8])  # X轴刻度间隔
    axes.set_yticks([i for i in range(0, 31, 3)])  # Y轴刻度间隔
    axes.grid(linestyle='--', alpha=0.5)


def plot_language_bar(axes: Axes, x: list[str], y: list[int]) -> None:
    """需求二：不同语言电影数量柱状图"""
    axes.bar(x, y, color='green', width=0.7)
    axes.set_title('不同语言电影数量柱状图', fontsize=18)
    axes.set_xlabel('语言', fontsize=12)
    axes.set_ylabel('电影数量', fontsize=12)
    axes.grid(linestyle='--', alpha=0.5)
    axes.tick_params(axis='x', rotation=90)


def plot_type_bar(axes: Axes, x: list[str], y: list[int]) -> None:
    """需求三：不同类型电影数量柱状图"""
    axes.bar(x, y, color='green', width=0.7)
    axes.set_title('不同类型电影数量柱状图', fontsize=18)
    axes.set_xlabel('类型', fontsize=12)
    axes.set_ylabel('电影数量', fontsize=12)
    axes.grid(linestyle='--', alpha=0.5)
    axes.tick_params(axis='x', rotation=90)


def plot_score_pie(axes: Axes, labels: list[int], values: list[int]) -> None:
    """需求四：不同评分电影数量占比饼状图"""
    axes.pie(values, labels=labels, autopct='%1.1f%%', startangle=0, radius=1.2)  # startangle: 起始角度
    axes.set_title('不同评分电影数量占比饼状图', fontsize=15)
    axes.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.3))


def main() -> None:
    # 加载数据
    data = load_data(os.path.join(DATA_DIR, 'movies.csv'))

    # 创建画布
    fig, axes = create_canvas()

    # 依次绘制四个需求的图表
    plot_year_line(axes[0][0], *get_year_data(data))
    plot_language_bar(axes[0][1], *get_language_data(data))
    plot_type_bar(axes[1][0], *get_type_data(data))
    plot_score_pie(axes[1][1], *get_score_data(data))

    # 保存图片
    fig.savefig(os.path.join(DATA_DIR, 'TMDB-TOP300.png'))

    # 展示图表
    plt.show()


if __name__ == '__main__':
    main()
