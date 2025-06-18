import pandas as pd
import matplotlib.pyplot as plt

# Re-create the DataFrame (or use if already existing)
rows = [
    ("Run 1", 427000, 0.418, 16, 353000, 0.363, 14, 319000, 0.230, 13),
    ("Run 2", 559000, 0.672, 19, 643000, 0.457, 22, 454000, 0.313, 14),
    ("Run 3", 370000, 0.381, 14, 498000, 0.410, 18, 374000, 0.236, 15),
    ("Run 4", 436000, 0.404, 16, 340000, 0.285, 14, 433000, 0.267, 17),
    ("Run 5", 587000, 0.635, 19, 491500, 0.371, 18, 386000, 0.246, 15),
]

metrics = ["Total Tokens", "API Costs", "Requests"]
models = ["Claude 3.7 Sonnet", "Gemini 2.5 Pro Preview", "GPT-4.1"]
columns = pd.MultiIndex.from_product([models, metrics])
index = [row[0] for row in rows]
data = [row[1:] for row in rows]
df = pd.DataFrame(data, index=index, columns=columns)

# カラーユニバーサルデザインの3色
colors = ["#FF4B00", "#005AFF", "#03AF7A"]  # 赤・青・緑


# Helper to draw a grouped bar chart for a chosen metric
def plot_metric(
    metric, label_fontsize, tick_fontsize, legend_fontsize, figsize=(5, 3.5)
):
    fig, ax = plt.subplots(figsize=figsize)  # 引数で受け取る
    x = range(len(df.index))
    bar_width = 0.25

    for i, model in enumerate(models):
        ax.bar(
            [p + i * bar_width for p in x],
            df[(model, metric)],
            width=bar_width,
            label=model,
            color=colors[i],  # ここで色を指定
        )

    ax.set_xticks([p + bar_width for p in x])
    ax.set_xticklabels(df.index, fontsize=tick_fontsize)
    ax.set_ylabel(metric, fontsize=label_fontsize)
    ax.tick_params(axis="y", labelsize=tick_fontsize)  # 縦軸の数字も大きく
    # ax.set_title(f"{metric} per Run", fontsize=label_fontsize)
    ax.legend(
        fontsize=legend_fontsize, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.15)
    )
    plt.tight_layout()
    plt.subplots_adjust(left=0.18, right=0.98, top=0.85, bottom=0.1)  # 余白を調整


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
