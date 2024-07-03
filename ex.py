from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()

# Create an instance of HuggingFaceEndpoint
hub_llm = HuggingFaceEndpoint(
    endpoint_url="openai-community/gpt2",
    headers={"Authorization": "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"}  # Replace with your actual Hugging Face API key
)

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="Translate English to SQL: {question}"
)


hub_chain = LLMChain(prompt=prompt, llm=hub_llm, verbose=True)

# Run the chain
result = hub_chain({"question": "what is the median age of the respondents using a mobile device?"})
print(result)
