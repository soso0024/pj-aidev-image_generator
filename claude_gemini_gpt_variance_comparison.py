import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Claude results
claude_rows = [
    ("Run 1", 427000, 751000),
    ("Run 2", 559000, 329000),
    ("Run 3", 370000, 546000),
    ("Run 4", 436000, 449000),
    ("Run 5", 587000, 743000),
]

# Gemini results
gemini_rows = [
    ("Run 1", 353000, 682000),
    ("Run 2", 643000, 296000),
    ("Run 3", 498000, 478000),
    ("Run 4", 340000, 485000),
    ("Run 5", 491500, 580000),
]

gpt_rows = [
    ("Run 1", 319000, 301000),
    ("Run 2", 454000, 296000),
    ("Run 3", 370000, 363000),
    ("Run 4", 433000, 373000),
    ("Run 5", 386000, 300000),
]


def create_variance_comparison_chart():
    """ばらつき（標準偏差）を表現した棒グラフを作成"""
    fig, ax = plt.subplots(figsize=(14, 8))

    # データの抽出
    claude_with = [row[1] for row in claude_rows]
    claude_without = [row[2] for row in claude_rows]
    gemini_with = [row[1] for row in gemini_rows]
    gemini_without = [row[2] for row in gemini_rows]
    gpt_with = [row[1] for row in gpt_rows]
    gpt_without = [row[2] for row in gpt_rows]

    # 統計値の計算
    data_stats = {
        "Claude with\nDocstrings": {
            "mean": np.mean(claude_with),
            "std": np.std(claude_with, ddof=1),
        },
        "Claude without\nDocstrings": {
            "mean": np.mean(claude_without),
            "std": np.std(claude_without, ddof=1),
        },
        "Gemini with\nDocstrings": {
            "mean": np.mean(gemini_with),
            "std": np.std(gemini_with, ddof=1),
        },
        "Gemini without\nDocstrings": {
            "mean": np.mean(gemini_without),
            "std": np.std(gemini_without, ddof=1),
        },
        "GPT with\nDocstrings": {
            "mean": np.mean(gpt_with),
            "std": np.std(gpt_with, ddof=1),
        },
        "GPT without\nDocstrings": {
            "mean": np.mean(gpt_without),
            "std": np.std(gpt_without, ddof=1),
        },
    }

    # カテゴリーとデータの準備
    categories = list(data_stats.keys())
    means = [data_stats[cat]["mean"] for cat in categories]
    stds = [data_stats[cat]["std"] for cat in categories]

    # カラーパレット
    colors = ["#E74C3C", "#C0392B", "#3498DB", "#2980B9", "#27AE60", "#229954"]

    # バーの位置
    x = np.arange(len(categories))
    width = 0.7

    # バーグラフの描画（エラーバー付き）
    bars = ax.bar(
        x,
        means,
        width,
        yerr=stds,
        color=colors,
        alpha=0.8,
        edgecolor="black",
        linewidth=1.2,
        error_kw={
            "elinewidth": 3,  # エラーバーの線の太さを2→4に変更
            "ecolor": "darkred",  # エラーバーの色を黒→暗赤に変更（より目立つ）
            "alpha": 0.9,  # エラーバーの透明度を0.7→0.9に変更（より濃く）
            "capsize": 15,  # エラーバーのキャップサイズを8→15に変更
            "capthick": 3,  # エラーバーのキャップの太さを2→4に変更
        },
    )

    # 値をバーの上に表示
    for i, (bar, mean, std) in enumerate(zip(bars, means, stds)):
        height = bar.get_height()
        # 平均値を表示
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + std + 15000,  # 距離を10000→15000に変更（バランス調整）
            f"{mean:,.0f}",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
        )
        # 標準偏差を表示
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + std + 45000,  # 距離を25000→45000に変更（より離す）
            f"±{std:,.0f}",
            ha="center",
            va="bottom",
            fontsize=11,
            style="italic",
            color="darkred",  # 色をgray→darkredに変更（エラーバーと統一）
            fontweight="bold",
        )

    # 軸とラベルの設定
    ax.set_ylabel(
        "Total Tokens (Mean ± Standard Deviation)", fontsize=16, fontweight="bold"
    )
    ax.set_xlabel("Model and Configuration", fontsize=16, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=12, fontweight="bold")
    ax.tick_params(axis="y", labelsize=14)

    # 縦軸を千単位（K）で表示
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"{x/1000:.0f}K"))

    # グリッドを追加
    ax.grid(axis="y", alpha=0.3, linestyle="--", linewidth=0.5)
    ax.set_axisbelow(True)

    # 軸の範囲を設定
    max_value = max([m + s for m, s in zip(means, stds)])
    ax.set_ylim(0, max_value * 1.15)

    # タイトルの追加
    # ax.set_title(
    #     "Token Usage Comparison: Mean Values with Standard Deviation",
    #     fontsize=18,
    #     fontweight="bold",
    #     pad=20,
    # )

    # スパインの調整
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1.0)
    ax.spines["bottom"].set_linewidth(1.0)

    # レイアウトの調整
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)

    return fig, ax


def create_coefficient_of_variation_chart():
    """変動係数 (CV) を表現した棒グラフを作成"""
    fig, ax = plt.subplots(figsize=(12, 6))

    # データの抽出
    claude_with = [row[1] for row in claude_rows]
    claude_without = [row[2] for row in claude_rows]
    gemini_with = [row[1] for row in gemini_rows]
    gemini_without = [row[2] for row in gemini_rows]
    gpt_with = [row[1] for row in gpt_rows]
    gpt_without = [row[2] for row in gpt_rows]

    # 変動係数の計算 (CV = std/mean * 100)
    datasets = {
        "Claude with\nDocstrings": claude_with,
        "Claude without\nDocstrings": claude_without,
        "Gemini with\nDocstrings": gemini_with,
        "Gemini without\nDocstrings": gemini_without,
        "GPT with\nDocstrings": gpt_with,
        "GPT without\nDocstrings": gpt_without,
    }

    categories = list(datasets.keys())
    cvs = []

    for name, data in datasets.items():
        mean_val = np.mean(data)
        std_val = np.std(data, ddof=1)
        cv = (std_val / mean_val) * 100
        cvs.append(cv)

    # カラーパレット
    colors = ["#E74C3C", "#C0392B", "#3498DB", "#2980B9", "#27AE60", "#229954"]

    # バーの位置
    x = np.arange(len(categories))
    width = 0.6

    # バーグラフの描画
    bars = ax.bar(
        x, cvs, width, color=colors, alpha=0.8, edgecolor="black", linewidth=1.2
    )

    # 値をバーの上に表示
    for bar, cv in zip(bars, cvs):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.5,
            f"{cv:.1f}%",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
        )

    # 軸とラベルの設定
    ax.set_ylabel("Coefficient of Variation (%)", fontsize=16, fontweight="bold")
    ax.set_xlabel("Model and Configuration", fontsize=16, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=12, fontweight="bold")
    ax.tick_params(axis="y", labelsize=14)

    # グリッドを追加
    ax.grid(axis="y", alpha=0.3, linestyle="--", linewidth=0.5)
    ax.set_axisbelow(True)

    # 軸の範囲を設定
    ax.set_ylim(0, max(cvs) * 1.15)

    # タイトルの追加
    # ax.set_title(
    #     "Variability Comparison: Coefficient of Variation",
    #     fontsize=18,
    #     fontweight="bold",
    #     pad=20,
    # )

    # スパインの調整
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1.0)
    ax.spines["bottom"].set_linewidth(1.0)

    # レイアウトの調整
    plt.tight_layout()

    return fig, ax


def print_variance_statistics():
    """ばらつきに関する詳細統計を出力"""
    claude_with = [row[1] for row in claude_rows]
    claude_without = [row[2] for row in claude_rows]
    gemini_with = [row[1] for row in gemini_rows]
    gemini_without = [row[2] for row in gemini_rows]
    gpt_with = [row[1] for row in gpt_rows]
    gpt_without = [row[2] for row in gpt_rows]

    datasets = {
        "Claude with Docstrings": claude_with,
        "Claude without Docstrings": claude_without,
        "Gemini with Docstrings": gemini_with,
        "Gemini without Docstrings": gemini_without,
        "GPT with Docstrings": gpt_with,
        "GPT without Docstrings": gpt_without,
    }

    print("=== ばらつき統計サマリー ===")
    print("-" * 80)

    for name, data in datasets.items():
        mean_val = np.mean(data)
        std_val = np.std(data, ddof=1)
        cv = (std_val / mean_val) * 100
        min_val = np.min(data)
        max_val = np.max(data)
        range_val = max_val - min_val

        print(f"\n{name}:")
        print(f"  平均値: {mean_val:,.0f}")
        print(f"  標準偏差: {std_val:,.0f}")
        print(f"  変動係数: {cv:.1f}%")
        print(f"  最小値: {min_val:,.0f}")
        print(f"  最大値: {max_val:,.0f}")
        print(f"  範囲: {range_val:,.0f}")


# メイン実行
if __name__ == "__main__":
    # 標準偏差付き棒グラフの生成
    print("標準偏差付き棒グラフを生成中...")
    fig1, ax1 = create_variance_comparison_chart()

    # 変動係数棒グラフの生成
    print("変動係数棒グラフを生成中...")
    fig2, ax2 = create_coefficient_of_variation_chart()

    # 統計情報の表示
    print_variance_statistics()

    # グラフの表示
    plt.show()

    # 画像として保存（オプション）
    # fig1.savefig("imgs/variance_comparison_with_error_bars.png", dpi=300, bbox_inches="tight")
    # fig2.savefig("imgs/coefficient_of_variation_comparison.png", dpi=300, bbox_inches="tight")
