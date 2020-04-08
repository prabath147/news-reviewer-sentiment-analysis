from matplotlib import pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
def sentiment_scores(sentence): 

    sid_obj = SentimentIntensityAnalyzer() 
 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
      
    print("Overall sentiment dictionary is : ",sentiment_dict) 
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
  
    print("Sentence Overall Rated As", end = " ") 
    h1=sentiment_dict['neg']*100
    h2=sentiment_dict['neu']*100
    h3=sentiment_dict['pos']*100
    
     
    if sentiment_dict['compound'] >= 0.05 : 
        print("Positive") 
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        print("Negative") 
  
    else : 
        print("Neutral") 
    left = [1, 2, 3] 
  
    
    height = [h1,h2,h3] 
      
    
    tick_label = ['negative', 'neutral', 'positive'] 
      
    
    plt.bar(left, height, tick_label = tick_label, 
            width = 0.8, color = ['red','blue', 'green']) 
      
    
    plt.xlabel('x - axis') 
    
    plt.ylabel('y - axis') 
    
    plt.title('My bar chart!') 

    plt.show()


if __name__ == "__main__" : 

  
    print("\nEnter the Statement :") 
     
    sentence=input()
    sentiment_scores(sentence)  

