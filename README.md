<div align="center">
  <h3 align="center">A brief Read.me introducing the project and its contents</h3>
    <br />
  </p>
</div>


<!-- ABOUT THE PROJECT -->

## About the Project:

### Introduction:

This project implements a Naive Bayes algorithm for Word Sense Disambiguation (WSD) without using external libraries such as scikit-learn, pandas, or NLTK. The primary goal is to classify instances of the word "plant" based on its context within a sentence, using a dataset from the British National Corpus (BNC). The project further extends to other words such as "bass," "crane," "motion," "palm," and "tank."


my LinkedIn:  [![LinkedIn][LinkedIn.js]][LinkedIn-url]

### Project Overview:

Word Sense Disambiguation is the task of determining the correct sense (meaning) of a word in a given context when the word has multiple meanings. In this project, the focus is on disambiguating the sense of the word "plant."

### Naive Bayes Algorithm:

The Naive Bayes algorithm is a probabilistic classifier based on Bayes' theorem. It assumes that the presence of a particular feature in a class is independent of the presence of any other feature (the "naive" assumption). In this project, the words surrounding the target word ("plant" in the first task) are used as features to predict the word's sense.


<!-- Dataset -->
##  Dataset:

The primary dataset used in this project consists of instances of the word "plant" drawn from the British National Corpus (BNC). Each instance is manually annotated with the correct sense of the word, such as plant%living or plant%factory.

### Data Example:

<instance id="plant.1000000" docsrc = "BNC/A07">
<answer instance="plant.1000000" senseid="plant%factory"/>
<context>
Until the mid- and late 1970s, there ....  <head> plant </head>  is owned by the church, or appropriate church body. 
</context>
</instance>

<!-- METHODOLOGY -->

## Methodology:

## Agorithm Steps:

### 1.Data Preprocessing:
* Feature Extraction: Stop words, punctuation, and stemming are removed to retain only meaningful words.
* Normalization: Convert text to lowercase and remove any extra spaces for consistency.

### 2.Data Processing:
* Instance Grouping: The data is read and grouped by instance ID, associating each target word with its surrounding context.
* Sense Counting: Word instances are counted for each sense in the training data to build a frequency distribution.

### 3.Model Training:
* Dictionary Creation: Separate dictionaries are created for each sense, storing the sentences related to each sense.
* Word Counting: Calculate the word counts for each sense and the total word count in the training set.

### 4.Model Testing:

* Probability Calculation: Using the Naive Bayes formula, probabilities are calculated for each sense based on the training data.
* Sense Assignment: The sense with the highest probability is assigned to each instance in the test data.


### 5.K-Fold Cross-Validation:

* Dataset Splitting: The dataset is divided into k folds, with one fold used for testing and the remaining folds for training.
* Accuracy Evaluation: Accuracies are calculated for each fold, and the mean accuracy is determined to assess overall model performance.

### 6.Output Generation:
* Prediction Storage: The predicted senses for each test instance are stored in an output file.
* Result Summary: Key details about the dataset, sense counts, fold accuracies, and average accuracy are printed for each file.

Example:

**Sentence to be Classified** : We made the non-slip surfaces by stippling the tops with a **bass** broom  a fairly new one works best. 

**Output**:

the count of each sense in bass.wsd is {'bass%fish': 317, 'bass%music': 3182} 

the accuracy of each fold of bass.wsd are [22.22222222222222, 88.88888888888889, 94.44444444444444, 94.44444444444444, 100.0]

the average accuracy for bass.wsd is 80.0



  <!-- GETTING STARTED -->
## Getting Started:

### Steps to run the code:





<!-- Results -->


<!-- Built With -->
## Built With:



The frameworks and libraries used within this project are:

[![Python][Python.js]][Python-url]
[![NumPy][NumPy.js]][NumPy-url]

<!-- LICENSE -->
## License

No License used.

<!-- CONTACT -->
## Contact

Sali E-loh - [@Sali El-loh](https://www.linkedin.com/in/salielloh12/) - ellohsali@gmail.com


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[LinkedIn.js]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[LinkedIn-url]: https://www.linkedin.com/in/salielloh12/
[Tensorflow.js]: https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[Tensorflow-url]: https://www.tensorflow.org/
[Keras.js]: https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white
[Keras-url]: https://keras.io/
[NumPy.js]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/
[Matplotlib.js]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[Matplotlib-url]: https://matplotlib.org/

[Python.js]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Pafy.js]: https://img.shields.io/badge/Pafy-FF6600?style=for-the-badge
[Pafy-url]: https://github.com/mps-youtube/pafy

[OS.js]: https://img.shields.io/badge/OS-44a833?style=for-the-badge
[OS-url]: https://docs.python.org/3/library/os.html

[OpenCV.js]: https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white
[OpenCV-url]: https://opencv.org/

[Math.js]: https://img.shields.io/badge/Math-000000?style=for-the-badge
[Math-url]: https://docs.python.org/3/library/math.html

[Random.js]: https://img.shields.io/badge/Random-44a833?style=for-the-badge
[Random-url]: https://docs.python.org/3/library/random.html

[NumPy.js]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/

[Datetime.js]: https://img.shields.io/badge/Datetime-44a833?style=for-the-badge
[Datetime-url]: https://docs.python.org/3/library/datetime.html

[TensorFlow.js]: https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[TensorFlow-url]: https://www.tensorflow.org/

[Deque.js]: https://img.shields.io/badge/Deque-44a833?style=for-the-badge
[Deque-url]: https://docs.python.org/3/library/collections.html#collections.deque

[Matplotlib.js]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[Matplotlib-url]: https://matplotlib.org/

[Keras.js]: https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white
[Keras-url]: https://keras.io/

[MoviePy.js]: https://img.shields.io/badge/MoviePy-FF4500?style=for-the-badge
[MoviePy-url]: https://zulko.github.io/moviepy/
































# Naive-Bayes-Word-Sense-Disambiguation-


# Example Input/Output:
Multiple instances (sentences) of the ambigous word we are trying to examine (example, bass):

Example of one sentence: We made the non-slip surfaces by stippling the tops with a **bass** broom  a fairly new one works best. 

# Example Output:
the count of each sense in bass.wsd is {'bass%fish': 317, 'bass%music': 3182} 

the accuracy of each fold of bass.wsd are [22.22222222222222, 88.88888888888889, 94.44444444444444, 94.44444444444444, 100.0]

the average accuracy for bass.wsd is 80.0



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

