import pandas as pd
import matplotlib.pyplot as plt

# 画像のデータ
rows = [
    ("Row 1", 751000, 0.576, 23, 682000, 0.780, 24, 301000, 0.223, 13),
    ("Row 2", 329000, 0.348, 14, 296000, 0.217, 13, 296000, 0.217, 13),
    ("Row 3", 546000, 0.503, 19, 478000, 0.360, 19, 363000, 0.233, 15),
    ("Row 4", 449000, 0.595, 18, 485333, 0.452, 19, 373000, 0.231, 16),
    ("Row 5", 743000, 0.701, 23, 580000, 0.570, 22, 300000, 0.223, 13),
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
