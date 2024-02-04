model_name_or_path = "TheBloke/Llama-2-70B-chat-GGML"
model_basename = "llama-2-70b-chat.ggmlv3.q5_1.bin" # the model is in bin format
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
  ff=open("llama_70b/"+ll[i],"w")
  lll=lll.read()
  llll=lll.split()
  temp=""
  for j in range(0,len(llll)):
    temp=temp+llll[j]+" "
    counter=counter+1
    if counter % 250 == 0:
      response=lcpp_llm(prompt= """You have been given  Bengali sentence(s) with errors. Your assignment has two main components: (1) Produce the Corrected Sentence: Identify and rectify the errors in the provided sentence, ensuring it is both grammatically and contextually accurate in Bengali. (2) Provide Concise Explanations for Each Error Type: For every error corrected in the sentence, categorize the error type and offer a brief explanation. Clarify the grammatical, syntactical, or semantic issues addressed and present the rationale behind each correction. The goal is to enhance understanding of the language intricacies involved. 
                          Example: 
                          Incorrect sentece: 
                          আমি গতকাল বাজারে যাই সবজি কিনি।                                                                                                      
                          Corrected Sentence:
                          আমি গতকাল বাজারে গিয়ে সবজি কিনলাম।
                          Explanations:

                         1. যাই → গিয়ে
                            Error Type: Verb Form
                            Explanation: The verb "যাই" (jai) implies the act of going, while the context of the sentence requires the past action of going to the market. Therefore, the correct form is "গিয়ে" (giye), indicating that the speaker went to the market.

                           2. কিনি → কিনলাম
                             Error Type: Verb Form
                             Explanation: The original sentence used the verb "কিনি" (kini), which is the present tense form. To match the past tense context of the sentence, the correct form is "কিনলাম" (kinlam), indicating that the speaker bought vegetables in the past.

                             Sentence(s) for correction is/are provided below.                                                      
                             {}
                      """, max_tokens=50, temperature=0.7, top_p=0.95, repeat_penalty=1.2, top_k=50,  echo=True)
        ttt=response["choices"][0]["text"]
        ttt=ttt.split("}")
        print(ttt[-1])
        ff.write(ttt[-1])
        temp=""
    print("-------------------------------------------------------------")
                                                                         
