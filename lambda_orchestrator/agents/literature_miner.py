import os
from transformers import BioGptTokenizer, BioGptForCausalLM, pipeline, set_seed

def search_biomedical_literature(query: str):
    """
    Local biomedical literature lookup (replaces external cloud dependencies).
    """
    # Local fallback/mock database chunk for development and testing
    return [
        {
            "content": {"text": "COX-2 selective inhibitors show stable docking profiles with modified salicylic acid cores."},
            "location": {"source": "local_biomed_database"}
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
    # 1. Retrieve context from local source
    results = search_biomedical_literature(query)
    context_text = " ".join([res.get("content", {}).get("text", "") for res in results])
    
    # 2. Combine retrieved literature context with the prompt
    prompt = f"Context: {context_text}\nQuery: {query}"
    
    # 3. Generate text analysis using BioGPT
    set_seed(42)
    generations = generator(prompt, max_length=60, num_return_sequences=1, do_sample=True)
    return generations[0]["generated_text"]

if __name__ == "__main__":
    output = analyze_query_with_biogpt("COX-2 selective inhibitors")
    print("\n--- BioGPT Generated Literature Insight ---")
    print(output)