# Naive-Bayes-Word-Sense-Disambiguation-
Naive Bayes Word Sense Disambiguation is a computational technique used to resolve the ambiguity present in natural language, where a word can have multiple meanings depending on its context. Leveraging the principles of the Naive Bayes algorithm, this approach aims to accurately assign the most appropriate meaning to a word by analyzing the surrounding words or context. By considering the probabilities of different word senses given the context, Naive Bayes Word Sense Disambiguation offers a valuable solution to enhancing the precision and comprehension of language processing systems, facilitating more accurate and context-aware interpretations of textual data


# Example Input/Output:
Multiple instances (sentences) of the ambigous word we are trying to examine (example, bass):

 instance id="bass.1000001" docsrc = "BNC/A16"
 answer instance="bass.1000001" senseid="bass%fish
 context
 It goes without .... We made the non-slip surfaces by stippling the tops with a bass broom  a fairly new one works best. 
 /context
 /instance


# Example Output:
the count of each sense in bass.wsd is {'bass%fish': 317, 'bass%music': 3182} 
the accuracy of each fold of bass.wsd are [22.22222222222222, 88.88888888888889, 94.44444444444444, 94.44444444444444, 100.0]
the average accuracy for bass.wsd is 80.0


# Agorithm Steps:

### 1.Data Preprocessing:

Stop words, punctuation, and stemming are removed to extract meaningful features.
Lowercasing and removal of extra spaces are performed.

### 2.Data Processing:
 Data is read and grouped by instance ID and relevant context.
Word instances are counted for each sense in the training data.

### 3.Model Training:
Dictionaries are created for each sense, storing sentences associated with each sense.
Word counts for each sense and the total word count are calculated.

### 4.Model Testing:

The model is tested using counts from the training data.
Probabilities for each sense are calculated using the Naive Bayes formula.
The sense with the highest probability is assigned to the test instances.

### 5.K-Fold Cross-Validation:

The dataset is divided into k folds for iterative training and testing.
Accuracies are calculated for each fold, and the mean accuracy is determined.

### 6.Output Generation:
Predicted senses for each fold are stored in an output file.
Key details about the dataset, sense counts, fold accuracies, and average accuracy are printed for each file.


#  Files in Repository:
The repository includes six training files for each ambiguous word, aimed at determining their respective senses:

bass.wsd
crane.wsd
motion.wsd
palm.wsd
tank.wsd
plant.wsd

WSD.py:
Contains the implementation of Naive Bayes for word sense disambiguation.

WSD.answers:
A text file providing detailed explanations for the obtained accuracies.

