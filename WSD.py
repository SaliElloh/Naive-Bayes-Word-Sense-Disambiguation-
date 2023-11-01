import numpy as np
import math
from datetime import datetime


date_time = datetime.now()
print(date_time)


class NBWD():

    def __init__(self):
        self.sense_prob = {}
        self.y_words_prob = {}
        self.actual_word_tags = {}

    #to calculate the accuracy
    def accuracy(self, actual_sense, predicted_sense):
        wrong_sentences = []
        correct_predictions = 0
        total_predictions = len(actual_sense)
        for sentence in actual_sense:
            if sentence in predicted_sense and predicted_sense[sentence] == actual_sense[sentence]:
                correct_predictions += 1
            else:
                wrong_sentences.append(sentence)

        accuracy = correct_predictions/total_predictions * 100

        return accuracy, wrong_sentences


    # preprocessing, which involves removing stop words, punctuation, making it lower case, and getting rid of
    # any extra space
    def preprocessing_data_(self, text):
        #remove stop words
        stop_words = ["0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "affecting", "affects", "after", "afterwards", "ag", "again", "against", "ah", "ain", "ain't", "aj", "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appear", "appreciate", "appropriate", "approximately", "ar", "are", "aren", "arent", "aren't", "arise", "around", "as", "a's", "aside", "ask", "asking", "associated", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "can't", "cause", "causes", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "changes", "ci", "cit", "cj", "cl", "clearly", "cm", "c'mon", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn", "couldnt", "couldn't", "course", "cp", "cq", "cr", "cry", "cs", "c's", "ct", "cu", "currently", "cv", "cx", "cy", "cz", "d", "d2", "da", "date", "dc", "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "didn't", "different", "dj", "dk", "dl", "do", "does", "doesn", "doesn't", "doing", "don", "done", "don't", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "effect", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "empty", "en", "e", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "first", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "h2", "h3", "had", "hadn", "hadn't", "happens", "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven", "haven't", "having", "he", "hed", "he'd", "he'll", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "here's", "hereupon", "hers", "herself", "hes", "he's", "hh", "hi", "hid", "him", "himself", "his", "hither", "hj", "ho", "home", "hopefully", "how", "howbeit", "however", "how's", "hr", "hs", "http", "hu", "hundred", "hy", "i", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ibid", "ic", "id", "i'd", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "i'll", "im", "i'm", "immediate", "immediately", "importance", "important", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "invention", "inward", "io", "ip", "iq", "ir", "is", "isn", "isn't", "it", "itd", "it'd", "it'll", "its", "it's", "itself", "iv", "i've", "ix", "iy", "iz", "j", "jj", "jr", "js", "jt", "ju", "just", "k", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "know", "known", "knows", "ko", "l", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets", "let's", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mightn't", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "mustn't", "my", "myself", "n", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "necessary", "need", "needn", "needn't", "needs", "neither", "never", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "other", "others", "otherwise", "ou", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "possible", "possibly", "potentially", "pp", "pq", "pr", "predominantly", "present", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "qj", "qu", "que", "quickly", "quite", "qv", "r", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "s2", "sa", "said", "same", "saw", "say", "saying", "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "sf", "shall", "shan", "shan't", "she", "shed", "she'd", "she'll", "shes", "she's", "should", "shouldn", "shouldn't", "should've", "show", "showed", "shown", "showns", "shows", "si", "side", "significant", "significantly", "similar", "similarly", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "system", "sz", "t", "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "there's", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'd", "they'll", "theyre", "they're", "they've", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "t's", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "ut", "v", "va", "value", "various", "vd", "ve", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "wa", "want", "wants", "was", "wasn", "wasnt", "wasn't", "way", "we", "wed", "we'd", "welcome", "well", "we'll", "well-b", "went", "were", "we're", "weren", "werent", "weren't", "we've", "what", "whatever", "what'll", "whats", "what's", "when", "whence", "whenever", "when's", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "where's", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "who's", "whose", "why", "why's", "wi", "widely", "will", "willing", "wish", "with", "within", "without", "wo", "won", "wonder", "wont", "won't", "words", "world", "would", "wouldn", "wouldnt", "wouldn't", "www", "x", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "y2", "yes", "yet", "yj", "yl", "you", "youd", "you'd", "you'll", "your", "youre", "you're", "yours", "yourself", "yourselves", "you've", "yr", "ys", "yt", "z", "zero", "zi", "zz"]
        stemming = ['sses', 'ies', 'ss', 's', 'ed', 'ing', 'ational', 'tional', 'ed', 'ing', 'ational', 'tional', 'ational', 'al', 'ance', 'ence', 'er', 'ic', 'able', 'ible', 'ant', 'ement', 'ment', 'ent', 'ou', 'ism', 'ate', 'iti', 'ous', 'ive', 'ize']
        filtered_text = []
        word_list = text.split()
        for word in word_list:
            if word.lower() not in stop_words:
                filtered_text.append(word)
            # for stem in stemming:
            #     if word.endswith(stem):
            #         filtered_text += word[:len(stem)]

        filtered_text_str = ' '.join(filtered_text)  # Join the words with spaces

        return filtered_text_str

    #read the file, and group the data for each instance id in one list
    def read(self, file_name):
        self.instances = []
        with open(file_name, 'r') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines if line.strip()]
            punctuation = [".", ",", ":", ";", "!", "?", "'", "(", ")", "[", "]", "{", "}", "-", "_"
                        , "|", "@", "#", "$", "^", "&", "*", "~", "`", "+"]
            filtered_lines = []
            for line in lines:
                filtered_line = ''.join(char for char in line if char not in punctuation)
                filtered_lines.append(filtered_line)


            grouped_lines = [filtered_lines[i:i + 6] for i in range(0, len(filtered_lines), 6)]
            for group in grouped_lines:
                #get rid of any unnecessary data, we only need the sense_id and context (sentences)
                simplified_group = {}
                simplified_group['sense_id'] = group[1]

                simplified_group['context'] = self.preprocessing_data_(group[3].lower().strip())

                # simplified_group['context'] = group[3]

                self.instances.append(simplified_group)


            for item in self.instances:
                item['sense_id'] = item['sense_id'].split('senseid="')[1].split('"/>')[0]

            return self.instances


    # def get_instance_id(self, context):
    #     for item in self.grouped_lines:
    #         if item[3].lower().strip() == context.lower().strip():
    #             return item[0]
    #     return None

    #count the word instances of the TRAINING datas, This is done by counting the number of times a word appears given a sense
    # C(word|sense 1), C(word|sense 2)
    # sense_count = total number of words given a sense
    def count_instances(self):

        self.total = len(self.instances)

        self.senses_count = {}
        self.sense_1 = {}
        self.sense_2 = {}

        for item in self.instances:
            if item['sense_id'] not in self.senses_count:
                self.senses_count[item['sense_id']] = 1
            else:
                self.senses_count[item['sense_id']] += 1

        for key, value in self.senses_count.items():
            self.sense_prob[key] = value / self.total

    def train(self, train, test):
        accuracies = []
        grouped_data = {}

        # Creating dictionaries for each sense of the training data
            # here, im storing the senses as keys in a dictionary,
            # then appending all sentences associated with that sense as their values
        for instance in train:
            sense_id = instance['sense_id']
            if sense_id not in grouped_data:
                grouped_data[sense_id] = []
                grouped_data[sense_id].append(instance['context'])
            else:
                grouped_data[sense_id].append(instance['context'])

        self.count_of_words = {} #count of words given a sense
        self.total_count_per_sense = {} #total number of words in a sense

        # calculating total word count for each sense
        for key, value in grouped_data.items():
            self.total_count_per_sense[key] = 0  # Initialize the count for each sense
            self.count_of_words[key] = {}
            for context in value:
                words = context.split()
                self.total_count_per_sense[key] += len(words)
                for word in words:
                    if word in self.count_of_words[key]:
                        self.count_of_words[key][word] += 1
                    else:
                        self.count_of_words[key][word] = 1
            self.total_count_per_sense[key] = sum(self.count_of_words[key].values())

        self.words_prob = {}
        self.vocabulary_size = 0 #size of the vocabulary for BOTH senses
        for words_dict in self.count_of_words.values():
            self.vocabulary_size += len(words_dict)

        #Testing the data
        # here, we use the counts that we found in the training set, and apply them to the test set
        grouped_y_data = []
        self.y_words_prob = {}
        self.actual_word_tags = {}


        for instance in test:
            context = instance['context']
            self.actual_word_tags[context] = instance['sense_id']
            grouped_y_data.append(context)

        for sentence in grouped_y_data:
            context = sentence.split()
            sense_prob_sum = 0
            probabilities_of_senses = {}  #
            for word in context:
                for sense in self.count_of_words:  #looping through both senses
                    max_sense = None
                    max_prob = float('-inf')  #
                    prob_word = math.log2((self.count_of_words[sense].get(word, 0) + 1) / ( #add 1 smoothing, by addding 1 to the numerator, and the vocabulary size of both sense combined into the denominator
                            self.total_count_per_sense[sense] + self.vocabulary_size))
                    sense_prob_sum += prob_word   #adding the probabilities of the senses together (since we used logarithm)
                sentence_prob = sense_prob_sum + math.log2(self.sense_prob[sense])  #adding the probabilities to prior probability(P(S) =C(S)/C(instances)
                probabilities_of_senses[sense] = sentence_prob  #appending the sentence probability of each sense

            max_prob = max(probabilities_of_senses.values())  #calulating the maximum probability of both senses

            for key, value in probabilities_of_senses.items():
                if value == max_prob:
                    max_sense = key
                    self.y_words_prob[sentence] = max_sense #assigning the predicted max sense to the sentence)

        fold_accuracy, wrong_sentence = self.accuracy(self.actual_word_tags, self.y_words_prob)  #accuracy of fold
        return fold_accuracy, wrong_sentence,  self.total_count_per_sense



# Analysis for Plant.wsd only
nwd = NBWD()
nwd.read("plant.wsd")
nwd.count_instances()
k = 5
instances = nwd.read("plant.wsd")
fold_size = math.ceil(len(instances) / 5)
test_fold = len(instances) - fold_size*4


accuracies = []
f_predictions = []

#5 k fold

for i in range(k):
    s = i * test_fold
    e = (i + 1) * test_fold
    test_data = instances[s:e]
    train_data = [instance for instance in instances if instance not in test_data]
    fold_accuracy, wrong_sentence, sense_count = nwd.train(train_data, test_data)
    accuracies.append(fold_accuracy)
    mean_accuracy = np.mean(accuracies)

    f_predictions.append(f"Fold {i + 1}")
    for i, instance in enumerate(test_data):
        prediction = nwd.y_words_prob.get(instance['context'], 'None')
        f_predictions.append(f"{i} {prediction}")

    # Writing the fold predictions to an output file
    with open(f"plant.wsd.out", 'w') as f:
        f.write('\n'.join(f_predictions))

print(f"size of plant.wsd dataset is {len(instances)}")
print(f"the count of each sense in plant.wsd is {sense_count} ")
print(f"the accuracy of each fold of plant.wsd are {accuracies}")
print(f'the average accuracy for plant.wsd is {mean_accuracy}')


# Analyzing the rest of the files

files = ['bass.wsd', 'crane.wsd', 'motion.wsd', 'palm.wsd', "tank.wsd"]

for file in files:
    nwd = NBWD()
    nwd.read(file)
    nwd.count_instances()
    k = 5
    instances = nwd.read(file)
    fold_size = math.ceil(len(instances) / 5)
    test_fold = len(instances) - fold_size*4

    accuracies = []
    f_predictions = []

    for i in range(k):
        s = i * test_fold
        e = (i + 1) * test_fold
        test_data = instances[s:e]
        train_data = [instance for instance in instances if instance not in test_data]
        fold_accuracy,wrong_sentences, sense_count = nwd.train(train_data, test_data)
        accuracies.append(fold_accuracy)
        mean_accuracy = np.mean(accuracies)  #Calculating the mean of the accuracies


    print(f"size of {file} dataset is {len(instances)}")
    print(f"the count of each sense in {file} is {sense_count} ")
    print(f"the accuracy of each fold of {file} are {accuracies}")
    print(f'the average accuracy for {file} is {mean_accuracy}')
