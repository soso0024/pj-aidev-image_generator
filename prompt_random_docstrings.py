import pandas as pd
import matplotlib.pyplot as plt

# 画像のデータ
rows = [
    ("Row 1", 558000, 0.663, 19, 418000, 0.444, 16, 382000, 0.263, 15),
    ("Row 2", 331000, 0.351, 13, 362000, 0.374, 14, 333000, 0.243, 13),
    ("Row 3", 468000, 0.471, 16, 461000, 0.353, 17, 337000, 0.245, 13),
    ("Row 4", 847000, 0.892, 25, 361000, 0.322, 14, 362000, 0.260, 14),
    ("Row 5", 555000, 0.611, 18, 355000, 0.264, 14, 407000, 0.291, 15),
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
