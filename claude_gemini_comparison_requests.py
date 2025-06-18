import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Claude results
claude_rows = [
    ("Run 1", 16, 23),
    ("Run 2", 19, 14),
    ("Run 3", 14, 19),
    ("Run 4", 16, 18),
    ("Run 5", 19, 23),
]

# Gemini results
gemini_rows = [
    ("Run 1", 14, 24),
    ("Run 2", 22, 13),
    ("Run 3", 18, 19),
    ("Run 4", 14, 19),
    ("Run 5", 18, 22),
]


def create_comparison_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # バーの幅と位置の設定
    runs = ["Run 1", "Run 2", "Run 3", "Run 4", "Run 5"]
    x = np.arange(len(runs))
    width = 0.18  # バーの幅を少し細く

    # より洗練されたカラーパレット
    colors = {
        "Claude with Docstrings": "#E74C3C",  # 明るい赤
        "Claude without Docstrings": "#C0392B",  # 濃い赤
        "Gemini with Docstrings": "#3498DB",  # 明るい青
        "Gemini without Docstrings": "#2980B9",  # 濃い青
    }

    # データの抽出
    claude_with = [row[1] for row in claude_rows]
    claude_without = [row[2] for row in claude_rows]
    gemini_with = [row[1] for row in gemini_rows]
    gemini_without = [row[2] for row in gemini_rows]

    # バーグラフの描画（位置を調整）
    bars1 = ax.bar(
        x - 1.5 * width,
        claude_with,
        width,
        label="Claude with Docstrings",
        color=colors["Claude with Docstrings"],
    )
    bars2 = ax.bar(
        x - 0.5 * width,
        claude_without,
        width,
        label="Claude without Docstrings",
        color=colors["Claude without Docstrings"],
    )
    bars3 = ax.bar(
        x + 0.5 * width,
        gemini_with,
        width,
        label="Gemini with Docstrings",
        color=colors["Gemini with Docstrings"],
    )
    bars4 = ax.bar(
        x + 1.5 * width,
        gemini_without,
        width,
        label="Gemini without Docstrings",
        color=colors["Gemini without Docstrings"],
    )

    # 軸とラベルの設定
    ax.set_ylabel("Requests", fontsize=20, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(runs, fontsize=16, fontweight="bold")
    ax.tick_params(axis="y", labelsize=16)

    # 縦軸を整数で表示
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"{int(x)}"))

    # グリッドを追加（より薄く）
    ax.grid(axis="y", alpha=0.2, linestyle="--", linewidth=0.5)
    ax.set_axisbelow(True)

    # 軸の範囲を設定（少し余裕を持たせる）
    ax.set_ylim(
        0, max(claude_with + claude_without + gemini_with + gemini_without) * 1.1
    )

    # 凡例の設定（より見やすく）
    ax.legend(
        fontsize=13,
        ncol=2,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.08),
        frameon=True,
        fancybox=True,
        shadow=True,
    )

    # スパインの調整
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(0.5)
    ax.spines["bottom"].set_linewidth(0.5)

    # レイアウトの調整
    plt.tight_layout()
    plt.subplots_adjust(left=0.08, right=0.98, top=0.88, bottom=0.08)

    return fig, ax


# グラフの生成と表示
fig, ax = create_comparison_chart()
plt.show()


# 統計情報の表示
def print_summary():
    claude_with = [row[1] for row in claude_rows]
    claude_without = [row[2] for row in claude_rows]
    gemini_with = [row[1] for row in gemini_rows]
    gemini_without = [row[2] for row in gemini_rows]

    print("=== 統計サマリー ===")
    print(
        f"Claude with Docstrings - 平均: {np.mean(claude_with):,.0f}, 標準偏差: {np.std(claude_with):,.0f}"
    )
    print(
        f"Claude without Docstrings - 平均: {np.mean(claude_without):,.0f}, 標準偏差: {np.std(claude_without):,.0f}"
    )
    print(
        f"Gemini with Docstrings - 平均: {np.mean(gemini_with):,.0f}, 標準偏差: {np.std(gemini_with):,.0f}"
    )
    print(
        f"Gemini without Docstrings - 平均: {np.mean(gemini_without):,.0f}, 標準偏差: {np.std(gemini_without):,.0f}"
    )


print_summary()
