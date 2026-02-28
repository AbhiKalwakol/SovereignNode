import os
from llama_cpp import Llama

# 1. Safely locate the model using relative paths
script_dir = os.path.dirname(os.path.abspath(__file__))
model_filename = "Llama3.3-8B-Instruct-Thinking-Heretic-Uncensored-Claude-4.5-Opus-High-Reasoning.i1-Q4_K_M.gguf"
model_path = os.path.join(script_dir, "models", model_filename)

# 2. Check if the model exists before trying to load it
if not os.path.exists(model_path):
    print(f"Error: Model not found at {model_path}")
    print("Please download the model and place it in the 'models' directory.")
    exit(1)

# 3. Load the model
print("Loading SovereignNode AI...")
llm = Llama(
    model_path=model_path,
    n_ctx=2048, # Context window
    verbose=False
)

# 4. Run a quick test
print("\n--- Model Loaded. Testing Inference ---\n")
response = llm(
    "Explain the concept of open-source software in one sentence.",
    max_tokens=100
)

print(response['choices'][0]['text'])