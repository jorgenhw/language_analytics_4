import src.emotion_classification as ec
import src.visualizing_emotion_classification as vec

import argparse
import os

# Path: main.py

def main():
    """
    ### Main function for emotion classification of news headlines ###
    """
   
   # load data
    data_path = os.path.join("data", "fake_or_real_news.csv")
    data = ec.load_data(data_path)

    # load classifier model
    classifier_model = ec.load_model(model_name="j-hartmann/emotion-english-distilroberta-base")

    # perform classification
    end_df = ec.emotions_classification_func(classifier_model, data, "title")

    # save data
    end_df.to_csv(os.path.join("data", "fake_or_real_news_with_emotions.csv"), index=False)

    """
    ### Visualizing the results of the emotion classification ###
    """

    # create table of emotions
    vec.table_of_emotions(end_df, "table_of_emotions.txt")

    # create countplot of emotions
    vec.create_emotion_countplot(end_df, "emotion_countplot.png")

    # create pie chart of emotions
    vec.create_emotion_piecharts(end_df, "emotion_piechart.png")

if __name__ == "__main__":
    main()