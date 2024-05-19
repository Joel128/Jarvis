from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import re
import os

def preprocess_data(text):
    """
    Preprocesses text data for classification.

    Args:
        text (str): The text to be preprocessed.

    Returns:
        str: The preprocessed text.
    """
    # Convert to lowercase
    text = text.lower()

    # Remove non-alphanumeric characters except spaces
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

def load_training_data(file_path):
    """
    Loads training data from a tab-delimited text file.

    Args:
        file_path (str): The path to the training data file.

    Returns:
        list[str], list[str]: The preprocessed text data and labels, respectively.
    """
    X_train = []
    y_train = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "/" in line:
                text, label = line.strip().split("/")
                X_train.append(preprocess_data(text))
                y_train.append(label)
            else:
                print(f"Incorrect format in line: {line.strip()}")

    return X_train, y_train

def train_model():
    """
    Trains a text classification model.

    Returns:
        sklearn.pipeline.Pipeline: The trained model.
    """
    X_train, y_train = load_training_data("queries.txt")

    global model
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)

    return model

def retrain_model():
    """
    Retrains the text classification model with new data.

    (Note: This function assumes new data is manually labeled in the 'queries.txt' file)
    """
    if os.path.exists("queries.txt"):
        with open("queries.txt", "r") as file:
            user_queries = file.readlines()

        X_train = [preprocess_data(query) for query in user_queries]
        y_train = ["data"]  # Manually label the new data

        model.fit(X_train, y_train)

def classify_query(query):
    """
    Classifies a new query using the trained model.

    Args:
        query (str): The query to classify.

    Returns:
        str: The predicted label for the query.
    """
    query = preprocess_data(query)
    label = model.predict([query])[0]
    return label

def collect_data(query):
    """
    Collects new user data by appending it to the training data file.

    Args:
        query (str): The new user query.
    """
    with open("queries.txt", "a", encoding="utf-8") as file:
        file.write(query + "\n")

# Train the model initially
model = train_model()
