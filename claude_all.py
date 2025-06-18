import pandas as pd
import matplotlib.pyplot as plt

# 実験データ（画像から転記）
rows = [
    (
        "Run 1",
        427000,
        0.418,
        16,
        751000,
        0.576,
        23,
        377000,
        0.361,
        15,
        558000,
        0.663,
        19,
    ),
    (
        "Run 2",
        559000,
        0.672,
        19,
        329000,
        0.348,
        14,
        371000,
        0.289,
        15,
        331000,
        0.351,
        13,
    ),
    (
        "Run 3",
        370000,
        0.381,
        14,
        546000,
        0.503,
        19,
        561000,
        0.494,
        19,
        468000,
        0.471,
        16,
    ),
    (
        "Run 4",
        436000,
        0.404,
        16,
        449000,
        0.595,
        18,
        430000,
        0.654,
        16,
        847000,
        0.892,
        25,
    ),
    (
        "Run 5",
        587000,
        0.635,
        19,
        743000,
        0.701,
        23,
        612000,
        0.54,
        20,
        555000,
        0.611,
        18,
    ),
]

metrics = ["Total Tokens", "API Costs", "Requests"]
experiments = [
    "Prompt + Docstrings",
    "Prompt",
    "Prompt + Docstrings with LLMingua-2",
    "Prompt + Random Docstrings",
]
columns = pd.MultiIndex.from_product([experiments, metrics])
index = [row[0] for row in rows]
data = [row[1:] for row in rows]
df = pd.DataFrame(data, index=index, columns=columns)

# 色（カラーユニバーサルデザインの4色）
colors = ["#FF4B00", "#005AFF", "#03AF7A", "#4DC4FF"]  # オレンジ, 青, 緑, 水色

# 指標ごとにグループ化棒グラフを描画


def plot_metric(metric, label_fontsize, tick_fontsize, legend_fontsize, figsize=(8, 5)):
    fig, ax = plt.subplots(figsize=figsize)
    x = range(len(df.index))
    bar_width = 0.18
    for i, exp in enumerate(experiments):
        ax.bar(
            [p + i * bar_width for p in x],
            df[(exp, metric)],
            width=bar_width,
            label=exp,
            color=colors[i],
        )
    ax.set_xticks([p + 1.5 * bar_width for p in x])
    ax.set_xticklabels(df.index, fontsize=tick_fontsize)
    ax.set_ylabel(metric, fontsize=label_fontsize)
    ax.tick_params(axis="y", labelsize=tick_fontsize)
    ax.legend(
        fontsize=legend_fontsize, ncol=2, loc="upper center", bbox_to_anchor=(0.5, 1.15)
    )
    plt.tight_layout()
    plt.subplots_adjust(left=0.18, right=0.98, top=0.85, bottom=0.1)


# 3つの指標でグラフを作成
plot_metric("Total Tokens", label_fontsize=18, tick_fontsize=16, legend_fontsize=12)
plt.show()
w
plot_metric("API Costs", label_fontsize=18, tick_fontsize=16, legend_fontsize=12)
plt.show()

plot_metric("Requests", label_fontsize=18, tick_fontsize=16, legend_fontsize=12)
plt.show()
