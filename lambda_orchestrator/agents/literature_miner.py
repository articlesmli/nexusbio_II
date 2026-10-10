import os
import boto3
from transformers import BioGptTokenizer, BioGptForCausalLM, pipeline, set_seed

# Initialize Bedrock client
bedrock_agent_runtime = boto3.client('bedrock-agent-runtime')
KNOWLEDGE_BASE_ID = os.getenv("BEDROCK_KB_ID", "MOCK_KB_ID")

def search_biomedical_literature(query: str):
    """
    Queries Amazon Bedrock Knowledge Base backed by OpenSearch Serverless.
    """
    try:
        response = bedrock_agent_runtime.retrieve(
            knowledgeBaseId=KNOWLEDGE_BASE_ID,
            retrievalQuery={'text': query},
            retrievalConfiguration={
                'vectorSearchConfiguration': {'numberOfResults': 3}
            }
        )
        return response.get('retrievalResults', [])
    except Exception as e:
        print(f"Bedrock KB retrieval fallback triggered: {str(e)}")
        # Fallback mock data chunk for development safety
        return [
            {
                "content": {"text": "COX-2 selective inhibitors show stable docking profiles with modified salicylic acid cores."},
                "location": {"s3Location": {"uri": "s3://nexusbio-datalake/raw_documents/sample_biomed.pdf"}}
            }
        ]

# Load free open-source BioGPT model and tokenizer directly from Hugging Face
print("Loading local BioGPT model...")
model_name = "microsoft/biogpt"
tokenizer = BioGptTokenizer.from_pretrained(model_name)
model = BioGptForCausalLM.from_pretrained(model_name)

# Create local text generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def analyze_query_with_biogpt(query: str):
    # 1. Retrieve context from Bedrock KB (or mock fallback)
    results = search_biomedical_literature(query)
    context_text = " ".join([res.get("content", {}).get("text", "") for res in results])
    
    # 2. Combine retrieved literature context with the prompt
    prompt = f"Context: {context_text}\nQuery: {query}"
    
    # 3. Generate text analysis using BioGPT
    set_seed(42)
    generations = generator(prompt, max_length=60, num_return_sequences=1, do_sample=True)
    return generations[0]["generated_text"]

if __name__ == "__main__":
    # Test run combining retrieval and local model generation
    output = analyze_query_with_biogpt("COX-2 selective inhibitors")
    print("\n--- BioGPT Generated Literature Insight ---")
    print(output)