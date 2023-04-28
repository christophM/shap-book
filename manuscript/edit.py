import sys
import os
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import MarkdownTextSplitter
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

human_template = """
{text}
"""
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

system_text = """You are an expert technical editor specializing in machine learning books written for machine learning engineers and data scientist. You are especially good at cutting clutter.

- Improve grammar and language
- fix errors
- cut clutter
- keep tone and voice
- don't change markdown syntax, e.g. keep [@reference]
- never cut jokes
- output 1 line per sentence (same as input)
"""



system_text = """You are an expert editor. Your job is to make documents
consistent.

- Fix spelling errors
- Bullet point lists should end in period ".", except when the point is an item or a sentence fragment, then end without "."
- Level 1 headers (#) in title case
- Level 2 headers (##) sentence case. Except when it's within a "box", i.e. between ::: and :::
- For strings in Python code examples use ' instead of "
- Each sentence is on a new line
- otherwise, don't change anything

"""

system_prompt = SystemMessage(content=system_text)

keyfile = "oai.key"
with open(keyfile, 'r') as f:
    key = f.read().strip()

llm = ChatOpenAI(openai_api_key=key, model="gpt-4", request_timeout=240)

def process_file(input_file):
    output_file = os.path.splitext(input_file)[0] + ".qmd"

    with open(input_file, 'r') as f:
        content = f.read()

    #splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=0)
    splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=1000, chunk_overlap=0)

    docs = splitter.split_text(content)
    print("Split into {} docs".format(len(docs)))
    chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_message_prompt])

    with open(output_file, 'w') as f:
        for doc in docs:
            result = llm(chat_prompt.format_prompt(text=doc).to_messages())
            print(result.content)
            f.write(result.content + '\n')

    print(f"Edited file saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py input_file")
    else:
        input_file = sys.argv[1]
        process_file(input_file)

