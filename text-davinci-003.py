import csv
import time
import openai
import csv
openai.api_key=""
import json
import os
lll=open("write1_davinci_edm_6.txt","a+")
ll=os.listdir("Tap/")
for i in range(0,1):
    with open("Tap/"+ll[i]) as jsonFile:
        data = json.load(jsonFile)
        jsonData = data["transcription"]
        data=jsonData
        print(data)
        temp_summary="You have been given  Bengali sentence(s) with errors. Your assignment has two main components:(1) Produce the Corrected Sentence:Identify and rectify the errors in the provided sentence, ensuring it is both grammatically and contextually accurate in Bengali.(2) Provide Concise Explanations for Each Error Type:For every error corrected in the sentence, categorize the error type and offer a brief explanation. Clarify the grammatical, syntactical, or semantic issues addressed and present the rationale behind each correction. The goal is to enhance understanding of the language intricacies involved.Example:Incorrect sentece:Error Type: Typographical Explanation: The correct spelling of the word "+"liking"+ " or preference is in Bengali. The error in the original sentence is a typographical mistake where the letters and  got swapped.2. rror Type: Pronoun AgreementE Explanation: The original sentence used the pronoun (ei), which refers to something close to the speaker. However, since we are talking about a country lover t is more appropriate to use o refer to the concept of a country, which is considered as a neutral or distant object or Type: Spelling/Grammatical Explanation: The correct form is (y kare) which means truthful or genuine. The original sentence had a spelling error by using"


sleep(5)
    #response = openai.Completion.create(
    #            model="text-davinci-002",
    #            prompt=temp_summary,
    #            temperature=0.7,
    #            max_tokens=50,
    #            top_p=1.0,
    #            frequency_penalty=0.0,
    #            presence_penalty=1
    #            )
    response = openai.Completion.create(
                model="text-davinci-003",
                prompt=temp_summary2,
                temperature=0.7,
                max_tokens=ratio,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=1
                )

    print(i)
    #print(response["message"]["content"])
    llllll.write(response["choices"][0]["text"]+"\n")
