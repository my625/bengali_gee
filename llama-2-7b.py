model_name_or_path = "TheBloke/Llama-2-7B-chat-GGML"
model_basename = "llama-2-7b-chat.ggmlv3.q5_1.bin" # the model is in bin format
from huggingface_hub import hf_hub_download
from llama_cpp import Llama
model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)
lcpp_llm = None
lcpp_llm = Llama(
    model_path=model_path,
    n_threads=30, # CPU cores
    n_batch=512, # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
    n_gpu_layers=32 # Change this value based on your model and your GPU VRAM pool.
    )
prompt = "Write a linear regression in python"
import os
#from google.colab import drive
#drive.mount('/content/drive')
ll=os.listdir("test-data/judgement/")
#print(ll)
#ff=open("llama_summary/")
for i in range(83,len(ll)):
  counter=0
  lll=open("Tap/"+ll[i],"r")
  ff=open("llama_7b/"+ll[i],"w")
  lll=lll.read()
  llll=lll.split()
  temp=""
  for j in range(0,len(llll)):
    temp=temp+llll[j]+" "
    counter=counter+1
    if counter % 250 == 0:
      response=lcpp_llm(prompt="You have been given  Bengali sentence(s) with errors. Your assignment has two main components:(1) Produce the Corrected Sentence:Identify and rectify the errors in the provided sentence, ensuring it is both grammatically and contextually accurate in Bengali.(2) Provide Concise Explanations for Each Error Type:For every error corrected in the sentence, categorize the error type and offer a brief explanation. Clarify the grammatical, syntactical, or semantic issues addressed and present the rationale behind each correction. The goal is to enhance understanding of the language intricacies involved.Example:Incorrect sentece:Error Type: Typographical Explanation: The correct spelling of the word "+"liking"+ " or preference is in Bengali. The error in the original sentence is a typographical mistake where the letters and  got swapped.2. rror Type: Pronoun AgreementE Explanation: The original sentence used the pronoun (ei), which refers to something close to the speaker. However, since we are talking about a country lover t is more appropriate to use o refer to the concept of a country, which is considered as a neutral or distant object or Type: Spelling/Grammatical Explanation: The correct form is (y kare) which means truthful or genuine. The original sentence had a spelling error by using", max_tokens=50, temperature=0.7, top_p=0.95,
                  repeat_penalty=1.2, top_k=50,
                  echo=True)
      ttt=response["choices"][0]["text"]
      ttt=ttt.split("}")
      print(ttt[-1])
      ff.write(ttt[-1])
      temp=""
  print("-------------------------------------------------------------")
                                                                         