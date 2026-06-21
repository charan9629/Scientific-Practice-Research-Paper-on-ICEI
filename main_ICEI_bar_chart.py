import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# File Path
file_path = "/content/Organised_Data_Sets.xlsx"

# Check Sheet Names
xls = pd.ExcelFile(file_path)

print("Available Sheets:")
print(xls.sheet_names)
df = pd.read_excel(
    file_path,
    sheet_name="statistical_evaluation ",
    header=43,
    usecols="A:H",
    nrows=16
)

# Clean Column Names
df.columns = (
    df.columns
      .astype(str)
      .str.strip()
      .str.replace("\n", " ", regex=False)
)

print("\nDetected Columns:")
print(df.columns.tolist())

# Verify Required Columns Exist
required_columns = [
    "Name of the Conference",
    "Year",
    "Citation Impact Score",
    "Diversity Score",
    "Reference Quality Score",
    "Collaboration Score",
    "Visual Communication Score"
]

missing = [c for c in required_columns if c not in df.columns]

if len(missing) > 0:
    print("\nMissing Columns:")
    print(missing)
    raise ValueError(
        "Column names do not match Excel sheet. "
        "Check printed column names above."
    )

# Calculate ICEI
df["ICEI"] = (
    0.50 * df["Citation Impact Score"] +
    0.15 * df["Diversity Score"] +
    0.15 * df["Reference Quality Score"] +
    0.10 * df["Collaboration Score"] +
    0.10 * df["Visual Communication Score"]
)

df["ICEI"] = df["ICEI"].round(4)

# Save Calculated Values
df.to_excel("ICEI_Calculated.xlsx", index=False)

# Create Pivot Table
pivot_df = df.pivot(
    index="Name of the Conference",
    columns="Year",
    values="ICEI"
)

pivot_df = pivot_df.sort_index()

# Plot
plt.figure(figsize=(8,6))

x = np.arange(len(pivot_df))
width = 0.35

bars_2023 = plt.bar(
    x - width/2,
    pivot_df.get(2023),
    width,
    color="red",
    edgecolor="black",
    label="2023"
)

bars_2024 = plt.bar(
    x + width/2,
    pivot_df.get(2024),
    width,
    color="blue",
    edgecolor="black",
    label="2024"
)

# Value Labels
for bar in bars_2023:
    h = bar.get_height()
    if not np.isnan(h):
        plt.text(
            bar.get_x() + bar.get_width()/2,
            h + 0.01,
            f"{h:.2f}",
            ha="center",
            fontsize=8
        )

for bar in bars_2024:
    h = bar.get_height()
    if not np.isnan(h):
        plt.text(
            bar.get_x() + bar.get_width()/2,
            h + 0.01,
            f"{h:.2f}",
            ha="center",
            fontsize=8
        )

# Formatting
plt.xlabel(
    "Conference",
    fontsize=12,
    fontweight="bold"
)

plt.ylabel(
    "ICEI Score",
    fontsize=12,
    fontweight="bold"
)

plt.title(
    "IoT Conference Excellence Index (ICEI): 2023 vs 2024",
    fontsize=14,
    fontweight="bold"
)

plt.xticks(
    x,
    pivot_df.index,
    rotation=45,
    ha="right"
)

plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

plt.savefig(
    "Figure1_ICEI_Grouped_BarChart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Rankings
rank2023 = (
    df[df["Year"] == 2023]
    [["Name of the Conference", "ICEI"]]
    .sort_values("ICEI", ascending=False)
)

rank2024 = (
    df[df["Year"] == 2024]
    [["Name of the Conference", "ICEI"]]
    .sort_values("ICEI", ascending=False)
)

print("\n ICEI Ranking 2023")
print(rank2023)

print("\n ICEI Ranking 2024")
print(rank2024)

print("\nGenerated Files:")
print("ICEI_Calculated.xlsx")
print("Figure1_ICEI_Grouped_BarChart.png")