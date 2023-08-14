<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Cultural Datascience 2023</h1> 
  <h2 align="center">Assignment 4</h2> 
  <h3 align="center">Language Analytics</h3> 
  <p align="center">
    Jørgen Højlund Wibe<br>
    Student number: 201807750
  </p>
</p>


<!-- ABOUT THE PROJECT -->
## About the project
This project is part of the portfolios for language analytics exam project. This time we focuse on emotion classification of news headlines using [transformers pipeline](https://huggingface.co/docs/transformers/main_classes/pipelines). The goal is to classify news headlines into different emotions using a pre-trained language model. The project includes data processing, model loading, classification, and visualization of the results.

<!-- USAGE -->
## Usage

To use or reproduce the results you need to adopt the following steps.

**NOTE:** There may be slight variations depending on the terminal and operating system you use. The following example is designed to work using the Visual Studio Code version 1.77.3 (Universal). The terminal code should therefore work using a unix-based bash. The avoid potential package conflicts, the ```setup.sh``` bash files contains the steps necesarry to create a virtual environment, install libraries and run the project.

1. Clone repository
2. Run ```setup.sh```

### Clone repository

Clone repository using the following lines in the unix-based bash:

```bash
git clone https://github.com/jorgenhw/language_analytics_assignment_4.git
cd language_analytics_assignment_4
```

### Run ```setup.sh```

To replicate the results, I have included a bash script that automatically 

1. Creates a virtual environment for the project
2. Activates the virtual environment
3. Installs the correct versions of the packages required
4. Runs the script
5. Deactivates the virtual environment

Run the code below in your bash terminal:

```bash
bash setup.sh
```

## Inspecting results

When running the script, the different outputs will be saved in the ```data``` folder and the ```figures``` folder. The data folder contains the original data which the model is applied to as well as the dataframe with the new predictions (```fake_or_real_news_with_emotions.csv```). The ```figures``` folder contains a table showing the distribution of emotions as well as a barplot and pitchart showing the distribution of labels in real vs fake news generation.

<!-- REPOSITORY STRUCTURE -->
## Repository structure

This repository has the following structure:
```
│   main.py
│   README.md
│   requirements.txt
│   setup.sh
│
├───src
│       emotion_classification.py
│       visualizing_emotion_classification.py
│
├───figures
│       table_of_emotions.txt
│       emotion_countplot.png
│       emotion_piechart.png
│
└──data
        fake_or_real_news.csv
        fake_or_real_news_with_emotions.csv
 

```

<!-- DATA -->
## Data
The data used for this project is sourced from the "fake_or_real_news.csv" dataset, which contains news headlines labeled as either "REAL" or "FAKE". The dataset includes the following columns:

* **title**: The headline of the news article.
* **label**: Indicates whether the news article is classified as "REAL" or "FAKE".

The "fake_or_real_news.csv" dataset serves as the input for the emotion classification task. After performing the emotion classification using the j-hartmann/emotion-english-distilroberta-base model, the resulting dataset, "fake_or_real_news_with_emotions.csv", is generated. This dataset includes additional columns:

* **emotion**: Represents the predicted emotion label assigned to each news headline by the model.

The labeled data allows for further analysis of the distribution of emotions within both REAL and FAKE news headlines.

The original dataset is available through this [Kaggle](https://www.kaggle.com/) on [this link](https://www.kaggle.com/datasets/jillanisofttech/fake-or-real-news).

<!-- RESULTS -->
## Remarks on findings
The analysis of the data reveals interesting insights about the emotions associated with news headlines. Let's examine the findings in a structured manner.

**Emotion Classification of News Headlines**
*Count Plot and Table Analysis*
The first count plot and accompanying table provide valuable information about the emotions assigned to news headlines. It is evident that a clear majority of the headlines have been classified as Neutral by the BERT emotion model. Following Neutral, the emotion most frequently associated with the headlines is Fear.

**Emotion Distribution in REAL and FAKE News Headlines**
The second count plot aims to compare the distribution of emotions between REAL and FAKE news headlines. Although no major differences are observed, there are slightly more FAKE headlines classified under the emotions of Disgust, Anger, Joy, and Surprise.

**Interpreting Differences between REAL and FAKE News Headlines**
It is important to approach the interpretation of differences between REAL and FAKE news headlines with caution. Absolute values on the count plot may not fully represent the magnitude of differences, especially when there is an uneven distribution within each group. In this case, the discrepancy in the number of headlines per group is relatively small, but still noticeable. Thus, it is necessary to explore the proportion of emotions within each group for a more accurate understanding.

## Conclusion
The emotion classification results obtained from the j-hartmann/emotion-english-distilroberta-base model reveal no significant disparities between REAL and FAKE headlines. The prevailing classification for both types of headlines appears to be Neutral.

However, it is crucial to recognize that these classifications are solely derived from a single fine-tuned model and should not be considered as definitive truth. They represent the model's subjective interpretation rather than an objective assessment of the headlines. The model card on Hugging Face indicates an evaluation accuracy of 66%, surpassing the chance level of 14%. Nevertheless, it is important to acknowledge that the model is not infallible.

To gain a more comprehensive understanding of these differences, two approaches can be considered. Firstly, comparing the outcomes of the current model with those of other similar models may offer insights into the agreement or divergence in the assigned classifications. Secondly, examining the probability scores associated with each emotion label, as provided in the labelled data (fake_or_real_news_with_emotion_labels.csv), can shed light on variations in the model's confidence when classifying emotions for REAL versus FAKE headlines. Exploring these avenues will provide a more nuanced perspective on the observed differences.