# Step 0. Importing relevant libraries
import os
from dotenv import load_dotenv
from langchain.adapters.openai import convert_openai_messages
from langchain_community.chat_models import ChatOpenAI

# Step 1. Load environment variables
load_dotenv()

# Step 2. Instantiating your TavilyClient
from tavily import TavilyClient

def answer_qustion(question):

    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    # Step 2. Executing the search query and getting the results
    content = client.search(question, search_depth="advanced")["results"]

    # Step 3. Setting up the OpenAI prompts

    query = "下面是一道题，可能是单项选择题、多项选择题填空题、判断题中的一种，请判断题型。题目如下:{question}。之后，根据Information中的信息，回答问题，直接给出相应的答案".format(question=question)
    prompt = [{
        "role": "system",
        "content":  f'You are an AI critical thinker research assistant. '\
                    f'Your sole purpose is to write well written, critically acclaimed,'\
                    f'objective and structured reports on given text.'
    }, {
        "role": "user",
        "content": f'Information: """{content}"""\n\n' \
                   f'Using the above information, answer the following'\
                   f'query: "{query}" in a detailed report --'\
                   f'Please use MLA format and markdown syntax.'
    }]

    # Step 4. Running OpenAI through Langchain
    lc_messages = convert_openai_messages(prompt)
    report = ChatOpenAI(model='gpt-4o-mini', openai_api_key=os.getenv("OPENAI_API_KEY"), openai_api_base=os.getenv("OPENAI_API_BASE")).invoke(lc_messages).content

    # Step 5. That's it! Your research report is now done!
    # print(report)
    return report