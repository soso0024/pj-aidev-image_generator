import pandas as pd
import matplotlib.pyplot as plt

# 画像のデータ
rows = [
    ("Row 1", 377000, 0.361, 15, 350000, 0.395, 14, 409000, 0.285, 16),
    ("Row 2", 371000, 0.289, 15, 453000, 0.401, 17, 312000, 0.195, 13),
    ("Row 3", 561000, 0.494, 19, 401500, 0.398, 16, 314000, 0.196, 13),
    ("Row 4", 430000, 0.654, 16, 677000, 0.621, 23, 671000, 0.414, 23),
    ("Row 5", 612000, 0.54, 20, 565000, 0.511, 20, 321000, 0.204, 13),
]

metrics = ["Total Tokens", "API Costs", "Requests"]
models = ["Claude 3.7 Sonnet", "Gemini 2.5 Pro Preview", "GPT-4.1"]
columns = pd.MultiIndex.from_product([models, metrics])
index = [row[0] for row in rows]
data = [row[1:] for row in rows]
df = pd.DataFrame(data, index=index, columns=columns)


def plot_metric(metric):
    fig, ax = plt.subplots(figsize=(8, 5))
    x = range(len(df.index))
    bar_width = 0.25

    for i, model in enumerate(models):
        ax.bar(
            [p + i * bar_width for p in x],
            df[(model, metric)],
            width=bar_width,
            label=model,
        )

    ax.set_xticks([p + bar_width for p in x])
    ax.set_xticklabels(df.index)
    ax.set_ylabel(metric)
    ax.set_title(f"{metric} per Row")
    ax.legend()
    plt.tight_layout()


# グラフを表示
plot_metric("Total Tokens")
plt.show()
plot_metric("API Costs")
plt.show()
plot_metric("Requests")
plt.show()
