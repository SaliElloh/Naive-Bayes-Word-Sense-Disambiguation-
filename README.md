# Naive-Bayes-Word-Sense-Disambiguation-

For more information about me, please visit my LinkedIn:

[![LinkedIn][LinkedIn.js]][LinkedIn-url]

<!-- ABOUT THE PROJECT -->

## About the Project:

### Introduction:

This project implements a Naive Bayes algorithm for Word Sense Disambiguation (WSD) without using external libraries such as scikit-learn, pandas, or NLTK. The primary goal is to classify instances of the word "plant" based on its context within a sentence, using a dataset from the British National Corpus (BNC). The project further extends to other words such as "bass," "crane," "motion," "palm," and "tank."

### Project Overview:

Word Sense Disambiguation is the task of determining the correct sense (meaning) of a word in a given context when the word has multiple meanings. In this project, the focus is on disambiguating the sense of the word "plant."

### Naive Bayes Algorithm:

The Naive Bayes algorithm is a probabilistic classifier based on Bayes' theorem. It assumes that the presence of a particular feature in a class is independent of the presence of any other feature (the "naive" assumption). In this project, the words surrounding the target word ("plant" in the first task) are used as features to predict the word's sense.


<!-- Dataset -->

##  Dataset:

The primary dataset used in this project consists of instances of the word "plant" drawn from the British National Corpus (BNC). Each instance is manually annotated with the correct sense of the word, such as plant%living or plant%factory.

### Data Example:

![image](https://github.com/user-attachments/assets/c1f9ac7e-8d7e-415f-b826-f5c0bee20d79)

<!-- METHODOLOGY -->

## Methodology

### Algorithm Steps:

1. **Data Preprocessing**:
   - **Feature Extraction**: 
     - Remove stop words, punctuation, and apply stemming to retain meaningful words.
   - **Normalization**: 
     - Convert text to lowercase.
     - Remove extra spaces to ensure consistency.

2. **Data Processing**:
   - **Instance Grouping**: 
     - Group data by instance ID, associating each target word with its context.
   - **Sense Counting**: 
     - Count word instances for each sense in the training data to build a frequency distribution.

3. **Model Training**:
   - **Dictionary Creation**: 
     - Create separate dictionaries for each sense, storing the sentences related to each sense.
   - **Word Counting**: 
     - Calculate word counts for each sense and the total word count in the training set.

4. **Model Testing**:
   - **Probability Calculation**: 
     - Use the Naive Bayes formula to calculate probabilities for each sense based on the training data.
   - **Sense Assignment**: 
     - Assign the sense with the highest probability to each instance in the test data.

5. **K-Fold Cross-Validation**:
   - **Dataset Splitting**: 
     - Divide the dataset into k folds, using one fold for testing and the remaining folds for training.
   - **Accuracy Evaluation**: 
     - Calculate accuracies for each fold and determine the mean accuracy to assess overall model performance.

6. **Output Generation**:
   - **Prediction Storage**: 
     - Store the predicted senses for each test instance in an output file.
   - **Result Summary**: 
     - Print key details about the dataset, sense counts, fold accuracies, and average accuracy.

### Example:

a. **Sentence to be Classified**:  
   *We made the non-slip surfaces by stippling the tops with a **bass** broom—a fairly new one works best.*

b. **Output**:  
   The count of each sense in `bass.wsd` is `{'bass%fish': 317, 'bass%music': 3182}`.
   
   The accuracy of each fold of `bass.wsd` is `[22.22, 88.89, 94.44, 94.44, 100.0]`.
   
   The average accuracy for `bass.wsd` is `80.0%`.
   

  <!-- GETTING STARTED -->
  
## Getting Started:

### Steps to run the code:


<!-- Results -->

## Results:

| **Word**  | **Accuracy of Each Fold (%)**                                                                                                                                       | **Average Accuracy (%)** |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| `bass.wsd`  | [22.22, 88.89, 94.44, 94.44, 100.0]                                                                                                                                | 80.00                    |
| `crane.wsd` | [31.58, 73.68, 73.68, 78.95, 84.21]                                                                                                                                | 68.42                    |
| `motion.wsd`| [48.65, 47.22, 13.51, 24.32, 8.11]                                                                                                                                 | 28.36                    |
| `palm.wsd`  | [67.57, 35.14, 32.43, 27.03, 13.51]                                                                                                                                | 35.14                    |
| `tank.wsd`  | [56.76, 29.73, 27.03, 27.03, 35.14]                                                                                                                                | 35.14                    |

<!-- Built With -->

## Built With:

The frameworks and libraries used within this project are:

* [![Python][Python.js]][Python-url]
* [![NumPy][NumPy.js]][NumPy-url]
* [![Datetime][Datetime.js]][Datetime-url]


<!-- CONTACT -->

## Contact

Sali E-loh - [@Sali El-loh](https://www.linkedin.com/in/salielloh12/) - ellohsali@gmail.com


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[LinkedIn.js]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[LinkedIn-url]: https://www.linkedin.com/in/salielloh12/

[Python.js]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[NumPy.js]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/

[Datetime.js]: https://img.shields.io/badge/Datetime-44a833?style=for-the-badge
[Datetime-url]: https://docs.python.org/3/library/datetime.html


#  Files in Repository:
The repository includes six training files for each ambiguous word, aimed at determining their respective senses:

  1. bass.wsd
  2. crane.wsd
  3. motion.wsd
  4. palm.wsd
  5. tank.wsd
  6. plant.wsd
  
  7. WSD.py:
  Contains the implementation of Naive Bayes for word sense disambiguation.
  
  8. WSD.answers:
  A text file providing detailed explanations for the obtained accuracies.

