import pandas as pd
import matplotlib.pyplot as plt

# 画像のデータ
rows = [
    (
        "Prompt + Docstrings",
        475800,
        0.502,
        16.8,
        465100,
        0.377,
        17.2,
        393200,
        0.258,
        14.8,
    ),
    ("Prompt", 563800, 0.545, 19.4, 504267, 0.476, 19.2, 326600, 0.225, 14.0),
    (
        "Prompt + Docstrings\nwith LLMLingua-2",
        470200,
        0.468,
        17.0,
        489300,
        0.465,
        17.9,
        405400,
        0.259,
        15.6,
    ),
    (
        "Prompt +\nRandom Docstrings",
        551800,
        0.598,
        18.2,
        391400,
        0.351,
        15.0,
        364200,
        0.260,
        14.0,
    ),
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
    fig, ax = plt.subplots(figsize=figsize)
    x = range(len(df.index))
    bar_width = 0.25

    for i, model in enumerate(models):
        ax.bar(
            [p + i * bar_width for p in x],
            df[(model, metric)],
            width=bar_width,
            label=model,
            color=colors[i],
        )

    ax.set_xticks([p + bar_width for p in x])
    ax.set_xticklabels(df.index, fontsize=tick_fontsize)
    ax.set_ylabel(metric, fontsize=label_fontsize)
    ax.tick_params(axis="y", labelsize=tick_fontsize)
    # ax.set_title(f"{metric} per Row", fontsize=label_fontsize)
    ax.legend(
        fontsize=legend_fontsize, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.15)
    )
    plt.tight_layout()
    plt.subplots_adjust(left=0.10, right=0.98, top=0.85, bottom=0.1)


# グラフを表示
plot_metric(
    "Total Tokens",
    label_fontsize=13,
    tick_fontsize=11,
    legend_fontsize=12,
    figsize=(8, 5),
)
plt.show()

plot_metric(
    "API Costs",
    label_fontsize=13,
    tick_fontsize=11,
    legend_fontsize=12,
    figsize=(8, 5),
)
plt.show()

plot_metric(
    "Requests",
    label_fontsize=13,
    tick_fontsize=11,
    legend_fontsize=12,
    figsize=(8, 5),
)
plt.show()
