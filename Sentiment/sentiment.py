from textblob import TextBlob as tb

class SentimentAnalysis(tb):

    def checkSentiment(self):
        polarity, subjectivity = super().sentiment

        if polarity > 0:
            sentiment = "Positive"

        elif polarity < 0:
            sentiment = "Negative"

        else:
            polarity = 0
            sentiment = "Neutral"
        
        if subjectivity > 0 and subjectivity < 0.5:
            subObj = "Not a Completely Objective (Factual) Statement it might contain some personal opinion or it's a mix of both"

        elif subjectivity >= 0.5 and subjectivity <= 1:
            subObj = "Subjective (Personal Opinion)"

        else:
            subjectivity = 0
            subObj = "Objective (Highly Factual)"

        result= round(polarity,2),round(subjectivity,2),sentiment,subObj
        return result

