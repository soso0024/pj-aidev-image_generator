import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Re-create the DataFrame (or use if already existing)
rows = [
    ("Run 1", 427000, 751000),
    ("Run 2", 559000, 329000),
    ("Run 3", 370000, 546000),
    ("Run 4", 436000, 449000),
    ("Run 5", 587000, 743000),
]

metrics = ["Total Tokens"]
models = ["with Docstrings", "without Docstrings"]
columns = pd.MultiIndex.from_product([models, metrics])
index = [row[0] for row in rows]
data = [row[1:] for row in rows]
df = pd.DataFrame(data, index=index, columns=columns)

# より見やすいカラーデザイン
colors = ["#E74C3C", "#3498DB"]  # 明るい赤・明るい青


# Helper to draw a grouped bar chart for a chosen metric
def plot_metric(
    metric, label_fontsize, tick_fontsize, legend_fontsize, figsize=(5, 3.5)
):
    fig, ax = plt.subplots(figsize=figsize)  # 引数で受け取る
    x = range(len(df.index))
    bar_width = 0.25

    for i, model in enumerate(models):
        ax.bar(
            [p + (i - 0.5) * bar_width for p in x],
            df[(model, metric)],
            width=bar_width,
            label=model,
            color=colors[i],  # ここで色を指定
        )

    ax.set_xticks(x)
    ax.set_xticklabels(df.index, fontsize=tick_fontsize)
    ax.set_ylabel(metric, fontsize=label_fontsize)
    ax.tick_params(axis="y", labelsize=tick_fontsize)  # 縦軸の数字も大きく

    # 縦軸を千単位（K）で表示
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"{x/1000:.0f}K"))

    # グリッドを追加して見やすくする
    ax.grid(axis="y", alpha=0.3, linestyle="--", linewidth=0.7)
    ax.set_axisbelow(True)  # グリッドをバーの後ろに表示

    # ax.set_title(f"{metric} per Run", fontsize=label_fontsize)
    ax.legend(
        fontsize=legend_fontsize, ncol=2, loc="upper center", bbox_to_anchor=(0.5, 1.15)
    )
    plt.tight_layout()
    plt.subplots_adjust(left=0.14, right=0.98, top=0.85, bottom=0.1)  # 余白を調整


# Generate three separate charts
plot_metric(
    "Total Tokens",
    label_fontsize=18,
    tick_fontsize=16,
    legend_fontsize=12,
    figsize=(8, 5),  # 出力画像のサイズを調整
)
plt.show()

# plot_metric(
#     "API Costs",
#     label_fontsize=18,
#     tick_fontsize=16,
#     legend_fontsize=12,
#     figsize=(8, 5),
# )
# plt.show()

# plot_metric(
#     "Requests",
#     label_fontsize=18,
#     tick_fontsize=16,
#     legend_fontsize=12,
#     figsize=(8, 5),
# )
# plt.show()
