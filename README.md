# Online-Medical-Consultations-Crawling

Generally, when we use machine learning algorithm to do some task, large amounts of data is necessary. Sometimes we do not have so much data. Then, we can do few-shot learning, or we can make training pairs by ourself. For example, if we are doing the face recognition task with few images and labels, we can do data(image) augmentation to generate more training data with labels.

Nowadays, medical AIs become more and more popular. We use AI to do Pathological identification for years. Now we epand this work to do medical history taking to check the cause. However, because of patient privacy, the amount of data is very less. 

This project provides a function call which can download the questions and answers pair on the online-doctor pages of Department of Health in Taiwan. The online-doctor pages contains many questions asked by patients and correspond answers provided by professional doctors. With these QA pairs, we can train a basic QA model in the medical doamin.

## Requirement

beautifulsoup4 == 4.9.3

bs4 == 0.0.1

requests == 2.25.1


## Run

Just call the fuction in crawler.py with different parameters, e.g., " crawler.getAllArticles("復健科") ".

Then, you will get the QA pairs of the correspond department.

```sh
python crawler.py
```

