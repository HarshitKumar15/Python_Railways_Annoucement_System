import os
import gtts
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToAudio(text,filename):
    mystr= str(text)
    language= "hi"
    myobj= gTTS(text= mystr,lang= language,slow= True)
    myobj.save(filename)


#This function returns pydub audio segment
def mergeAudio(audios):
    combine= AudioSegment.empty()
    for audio in audios:
        combine+=AudioSegment.from_mp3(audio)
    return combine

def generateSkeleton():
    audio= AudioSegment.from_mp3("Railways.mp3")

    # 1- generate kripya dhan dijiye
    start= 1000 # All the no. in mili second
    finish= 3200
    audioProccessed= audio[start:finish]
    audioProccessed.export("1_hindi.mp3",format="mp3")

    #2- train no.
    start= 3300
    finish= 5000
    audioProccessed= audio[start:finish]
    audioProccessed.export("2_hindi.mp3",format="mp3")

    #3- from city

    #4- ke rasta
    start= 9300
    finish= 10000
    audioProccessed= audio[start:finish]
    audioProccessed.export("4_hindi.mp3",format="mp3")
    
    #5- via city

    #6- generate aani wali
    start= 10800
    finish= 11700
    audioProccessed= audio[start:finish]
    audioProccessed.export("6_hindi.mp3",format="mp3")

    #7- to city

    #8 -generate ko jane wali
    start= 14990
    finish= 16000
    audioProccessed= audio[start:finish]
    audioProccessed.export("8_hindi.mp3",format="mp3")

    #9- train name and train no.

    #10- generate par khadi hai
    start= 17500
    finish= 18700
    audioProccessed= audio[start:finish]
    audioProccessed.export("10_hindi.mp3",format="mp3")

    #11- platform no.


def generateAnnouncement(filename):
    # pass
    df= pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
       #3- from city
       textToAudio(item['from'],"3_hindi.mp3")
       
       #5- via city
       textToAudio(item['via'],"5_hindi.mp3")

       #7- to city
       textToAudio(item['to'],"7_hindi.mp3")

       #9-train name
       textToAudio(str(item['Train name']) + " " + str(item['Train no.']),"9_hindi.mp3")

       #11-platform no.
       textToAudio(item['Platform no.'],"11_hindi.mp3")

       audios= [f"{i}_hindi.mp3" for i in range(1,12)]
       announcement= mergeAudio(audios)
       announcement.export(f"announcement_{item['Train no.']}_{index+1}.mp3",format="mp3")

if __name__=="__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now generating announcement...")
    generateAnnouncement("announcement_hindi.xlsx")