import csv
import time
import openai
import csv
openai.api_key="API KEY"
import json
import os
lll=open("write1_gpt3.5t_edm_6.txt","a+")
ll=os.listdir("Tap/")
for i in range(0,1):
    with open("Tap/"+ll[i]) as jsonFile:
        data = json.load(jsonFile)
        jsonData = data["transcription"]
        data=jsonData
        print(datah)
        temp_summary = """You have been given  Bengali sentence(s) with errors. Your assignment has two main components: (1) Produce the Corrected Sentence: Identify and rectify the errors in the provided sentence, ensuring it is both grammatically and contextually accurate in Bengali. (2) Provide Concise Explanations for Each Error Type: For every error corrected in the sentence, categorize the error type and offer a brief explanation. Clarify the grammatical, syntactical, or semantic issues addressed and present the rationale behind each correction. The goal is to enhance understanding of the language intricacies involved. 
                          Example: 
                          Incorrect sentece: 
                          আমি গতকাল বাজারে যাই সবজি কিনি।                                                                                                      
                          Corrected Sentence:
                          আমি গতকাল বাজারে গিয়ে সবজি কিনলাম।
                          Explanations:

                         1. যাই → গিয়ে
                            Error Type: Verb Tense
                            Explanation: The verb "যাই" (jai) implies the act of going, while the context of the sentence requires the past action of going to the market. Therefore, the correct form is "গিয়ে" (giye), indicating that the speaker went to the market.

                           2. কিনি → কিনলাম
                             Error Type: Verb Tense
                             Explanation: The original sentence used the verb "কিনি" (kini), which is the present tense form. To match the past tense context of the sentence, the correct form is "কিনলাম" (kinlam), indicating that the speaker bought vegetables in the past.

                             Sentence(s) for correction is/are provided below.                                                      
                             {}
                       """

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
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content":temp_summary}],
                temperature=0.7,
                max_tokens=1000,
                stop=None
                )
    print(i)
    #print(response["message"]["content"])
    for choice in response.choices:
        lll.write(choice["message"]["content"])
        lll.write("\n--------------------------\n")
