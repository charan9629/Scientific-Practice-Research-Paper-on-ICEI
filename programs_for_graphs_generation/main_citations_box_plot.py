import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Read Excel File
file_path = "/content/Organised_Data_Sets.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="total_consolidated_data"
)

# Clean Column Names
df.columns = df.columns.str.strip()


# Conferences of Interest
selected_conferences = [
    "SenSys",
    "EWSN",
    "DCOSS-IoT",
    "WF-IoT",
    "BIOTC"
]

df = df[
    df["Conference"].isin(selected_conferences)
]


# Create Conference-Year Label
df["Conference_Year"] = (
    df["Conference"]
    + "-"
    + df["Conference year"].astype(str)
)


# Remove Missing Citation Values
df = df.dropna(
    subset=["Number of citations under Google Scholar"]
)


# Order of Display
conference_order = [
    "BIOTC-2023",
    "BIOTC-2024",
    "DCOSS-IoT-2023",
    "DCOSS-IoT-2024",
    "EWSN-2023",
    "EWSN-2024",
    "SenSys-2023",
    "SenSys-2024",
    "WF-IoT-2023",
    "WF-IoT-2024"
]

box_data = []

for conf in conference_order:

    citations = df[
        df["Conference_Year"] == conf
    ]["Number of citations under Google Scholar"]

    box_data.append(citations)


# Plot
fig, ax = plt.subplots(figsize=(8,6))

bp = ax.boxplot(
    box_data,
    positions=np.arange(1, 11),
    widths=0.6,
    patch_artist=True,
    tick_labels=[""] * len(conference_order),
    showfliers=True
)


# Box Colors
for i, box in enumerate(bp['boxes']):

    if "2023" in conference_order[i]:

        box.set(
            facecolor="lightcoral",
            edgecolor="darkred",
            hatch="//",
            linewidth=1.5
        )

    else:

        box.set(
            facecolor="lightblue",
            edgecolor="navy",
            hatch="\\\\",
            linewidth=1.5
        )


# Median Lines
for median in bp['medians']:
    median.set(
        color='black',
        linewidth=2
    )


# Outlier Markers
for i, flier in enumerate(bp['fliers']):

    if "2023" in conference_order[i]:

        flier.set(
            marker='o',
            markerfacecolor='red',
            markeredgecolor='darkred',
            markersize=6
        )

    else:

        flier.set(
            marker='s',
            markerfacecolor='blue',
            markeredgecolor='navy',
            markersize=6
        )


# Conference Labels (Only Once)
conference_centers = [1.5, 3.5, 5.5, 7.5, 9.5]

conference_labels = [
    "BIOTC",
    "DCOSS-IoT",
    "EWSN",
    "SenSys",
    "WF-IoT"
]

ax.set_xticks(conference_centers)

ax.set_xticklabels(
    conference_labels,
    fontsize=12,
)

# Year Labels Under Each Box
year_labels = [
    "2023", "2024",
    "2023", "2024",
    "2023", "2024",
    "2023", "2024",
    "2023", "2024"
]


# Axis Labels
ax.set_ylabel(
    "Paper Citations",
    fontsize=12,
    fontweight="bold"
)

ax.set_xlabel(
    "Conference",
    fontsize=12,
    fontweight="bold"
)

ax.set_title(
    "Citation Distribution Across Major IoT Conferences",
    fontsize=14,
    fontweight="bold"
)


# Grid
ax.grid(
    axis='y',
    linestyle='--',
    alpha=0.4
)


# Legend
legend_elements = [
    Patch(
        facecolor='lightcoral',
        edgecolor='darkred',
        hatch='//',
        label='2023'
    ),
    Patch(
        facecolor='lightblue',
        edgecolor='navy',
        hatch='\\\\',
        label='2024'
    )
]

ax.legend(
    handles=legend_elements,
    loc='upper right'
)

# Save Figure
plt.tight_layout()

plt.savefig(
    "Figure2_Selected_Conference_Boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()