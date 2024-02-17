# How Ready Are Generative Pre-trained Large Language Models for Explaining Bengali Grammatical Errors?
This repository contains code and data for the paper titled "How Ready Are Generative Pre-trained Large Language Models for Explaining Bengali Grammatical Errors?" The goal of this research is to evaluate the performance of various pre-trained large language models on the task of correcting grammatical errors in Bengali sentences and providing concise explanations for each error type. It is important to note that the codes include only one-shot example.

### Code Files:

The following Python scripts are included in the repository:

- gpt-4-turbo.py
- gpt-3.5-turbo.py
- text-davinci-003.py
- text-curie-001.py
- text-babbage-001.py
- text-ada-001.py
- llama-2-7b.py
- llama-2-13b.py
- llama-2-70b.py
  
Each script is designed to take a Bengali sentence with errors as input and output the corrected sentence along with concise explanations for each error type. The models used include GPT-4 Turbo, GPT-3.5 Turbo, text-davinci-003, text-curie-001, text-babbage-001, text-ada-001, llama-2-7b, llama-2-13b, and llama-2-70b.


A sample of the dataset can be found under the 'Data_Samples' folder. The full dataset will be released shortly.

The "Data_Samples" folder consists of the following .txt files:

- err.txt: Compilation of erroneous Bengali sentences from various sources such as Bengali essays, news, and social media.

- ref.txt: Contains grammatically correct versions of sentences in "err.txt". 

- cat.txt: Provides error type information corresponding to sentences in "err.txt". 
