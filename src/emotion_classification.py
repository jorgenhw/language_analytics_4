# Utilities 
import pathlib # for path utilities
from tqdm import tqdm # progress bar

# For data processing
import pandas as pd 

# huggingface model
from transformers import pipeline


# function to load data
def load_data(data_path):
    # load data
    data = pd.read_csv(data_path)
    return data

def load_model(model_name):
    # initialize pipeline
    classifier_model = pipeline("text-classification", 
                      model=model_name,
                      return_all_scores=True,
                      top_k = 1 
                      )
    return classifier_model

def emotions_classification_func(classifier, data, text_column):
   
    # Initialising list to save all predictions (emotions)
    emotion_predictions = []

    # for each text in data, perform classification
    for text in tqdm(data[text_column], desc="Performing classification"):
        # creating the prediction
        prediction = classifier(text)
        # appending the prediction to emotion_predictions list 
        emotion_predictions.append(prediction[0][0]) 

    # make predictions dataframe
    predictions_df = pd.DataFrame(emotion_predictions) 

    # renaming label into "emotion" to make it distinguishable from other labels in data
    predictions_data = predictions_df.rename(columns={"label": "emotion"})

    # combine predictions_data with text and label col in original dataframe
    end_df = pd.concat([data, predictions_data], axis=1)

    return end_df
