import tweepy
import model
import time
import random 


def main():
            auth = tweepy.OAuthHandler("GI3TbwV8FasjwxnoazzTvjeH7", "L6uq4GLNhBb94SkuQ1av0nPojfbcNK1cY6edNDwsUPVPbTZhu5")
            auth.set_access_token("2152561794-MbnoTmQ0ec3FIK8z3JYlFaEZC3iXwV6Ty6UroQZ", "i7UrWbOqBKXwwh7AJTebSm8carGz4iKOQPYEl5oyfcPnS")
            api = tweepy.API(auth)
    
            box = []
            test2 = model.model_();  
            test=test2
            while(len(test) > 10):
                hashtag = test.find(' ')
                if hashtag == 0:
                    test = test[1:]
                else :
                    #print(hashtag)
                    result = test[:hashtag]
                    test = test[hashtag:]
                    box.append(result)
            #print(box)
            hashtag = []
            for i in range(3):
                try:
                    r = random.randint(0, len(box)-1)
                    hashtag.append(box[r])
                except:
                    r = 1    
                    hashtag.append(box[r])

            string_ = test2.replace(" ", "")
            print(string_+"\n.\n#ทวิตนี้ถูกเขียนด้วยAIจากแฮชแท็กต่อไปนี้ #IamaI #ความรัก #ชีวิต #ฮาวทูทิ้ง #"+hashtag[0]+" #"+hashtag[1]+" #"+hashtag[2])
            api.update_status(string_+"\n.\n#ทวิตนี้ถูกเขียนด้วยAIจากแฮชแท็กต่อไปนี้ #IamaI #ความรัก #ชีวิต #ฮาวทูทิ้ง #"+hashtag[0]+" #"+hashtag[1]+" #"+hashtag[2])
            #print(string_)
            time.sleep(3600)

if __name__== "__main__":
    while(1):
        main()