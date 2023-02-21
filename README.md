# capstone

RES:
- https://www.apptweak.com/en/aso-blog/use-app-review-sentiment-analysis-to-make-product-decisions
- https://www.kaggle.com/code/mmmarchetti/play-store-sentiment-analysis-of-user-reviews/notebook


to-do

- data fetching - done
- attribute selection:    
- sort it by thumbsupcount, plot the data
- we need a statistical reasoning to select number of data points. so identify the threshold. then select the data points.
- plot a q-q plot to prove it's real-world data
- data cleaning: score, thumbsupcount, content, 
- find keywords from the dataset we will focus on. RES = https://www.nltk.org/_modules/nltk/stem/porter.html
- plot freq dist of keywords batch by bqtch, like of 4 first, then 10, then all
- word cloud of keyword freq distribution
- define the sentiments based on the word cloud, keyword freq
- find the attributes based on which we can rank the apps, before performing sentiment analysis.
- discuss ui elements, again.
