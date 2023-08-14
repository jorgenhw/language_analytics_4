from tabulate import tabulate
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def table_of_emotions(data, path_to_save):
    # making a table showing the disctribution of emotions per fake and real news
    count_table = pd.crosstab(index=data['emotion'],
                             columns=data['label'], 
                             )

    # emotion_count column which is the sum of all emotions
    count_table["emotion_count"] = count_table.sum(axis=1)

    # sort table by emotion_coiunt column
    count_table = count_table.sort_values(by="emotion_count", ascending=False)

    # creating labels and capitalizing them 
    emotion_labels = [label.title() for label in count_table.index]

    # now we are creating the table
    table = tabulate(
        [["emotion_count"] + count_table["emotion_count"].tolist(),
        ["REAL"] + count_table["REAL"].tolist(), 
        ["FAKE"] + count_table["FAKE"].tolist()], 
        headers=emotion_labels
    )

    # write table to .txt file
    with open(os.path.join("figures",path_to_save), "w") as f:
        f.write(table)




def create_emotion_countplot(data, savepath):
    # Capitalize emotion labels
    data["emotion"] = data["emotion"].str.title()
    
    # Get the order of emotions based on their count
    order = data["emotion"].value_counts().index

    # Define the color palette
    colors = sns.color_palette("hls", 8)
    
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # Adjust the top spacing to make room for the overall title
    fig.subplots_adjust(top=0.85)

    # Set the title for the first subplot
    axes[0].set_title("All News Headlines", fontsize=15)
    
    # Create a countplot for all news headlines
    sns.countplot(ax=axes[0], x='emotion', data=data, order=order, palette=colors, width=0.6)

    # Set the title for the second subplot
    axes[1].set_title("Real versus Fake Headlines", fontsize=15)
    
    # Define the order of the hue (label) for the second subplot
    hue_order = ["REAL", "FAKE"]
    
    # Create a countplot for real versus fake headlines with label hue
    sns.countplot(ax=axes[1], x='emotion', data=data, order=order, hue_order=hue_order, palette=["#DB5F57", "#EDAFAB"], hue='label', width=0.6)

    # Set the x and y labels for both subplots
    for ax in axes:
        ax.set_xlabel("Emotion")
        ax.set_ylabel("Count")

    # Set the legend for the second subplot
    axes[1].legend(title="Label", loc='upper right')

    # Set the overall title for the figure
    fig.suptitle("Emotion Labels in Real and Fake News Headlines", fontsize=18, fontweight="bold")

    # Save the figure to the specified path
    fig.savefig(os.path.join("figures", savepath), dpi=300)


def create_emotion_piecharts(data, savepath):
    # Create a cross-tabulation table of emotions per fake and real headlines
    count_table = pd.crosstab(index=data['emotion'], columns=data['label'])
    
    # Get the emotion labels from the count_table index
    emotion_labels = count_table.index

    # Define the color palette for the pie charts
    colors = ["#91db57","#57d3db", "#dbc257", "#a157db", "#db5f57", "#57db80", "#5770db"]
    
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    # Iterate over the subplots and labels
    for ax, label in zip(axes, ["REAL", "FAKE"]):
        # Create a pie chart with the count of emotions for the given label
        ax.pie(count_table[label], labels=emotion_labels, autopct='%1.1f%%', startangle=90, colors=colors, pctdistance=0.85, textprops={'fontsize': 10, 'fontweight': 'bold'}, wedgeprops={'linewidth': 2, 'edgecolor': 'white'})
        
        # Set equal aspect ratio for a nicer layout
        ax.axis('equal')
        
        # Set the title for each pie chart
        ax.set_title(f"{label.title()} Headlines", fontsize=20, pad=15)
        
        # Adjust the position of the pie chart to make room for the overall title
        original_pos = ax.get_position()
        new_pos = [original_pos.x0, (original_pos.y0 -0.065),  original_pos.width, original_pos.height]
        ax.set_position(new_pos)

    # Set the overall title for the figure
    fig.suptitle("Proportion of Emotion Labels in Real and Fake News Headlines", fontsize=25, fontweight="bold")

    # Save the figure to the specified path
    fig.savefig(os.path.join("figures", savepath), dpi=300)