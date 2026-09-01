import json
from litellm import completion
# 1. Collect responses from multiple candidate models
prompt = "Analyze this image and explain the primary bottleneck."
image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"

candidate_models = ["gpt-4o", "claude-3-5-sonnet-20241022", "gemini/gemini-2.5-flash"]
candidates = []

for model in candidate_models:
    res = completion(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            }
        ],
    )
    candidates.append({"model": model, "response": res.choices[0].message.content})

# 2. Define the LLM Judge prompt to compare and rank
judge_prompt = f"""
You are an expert judge evaluating responses to the following user prompt:
"{prompt}"

Below are candidate responses from different models:
{json.dumps(candidates, indent=2)}

Evaluation Criteria:
1. Grounding & Accuracy: Correctly reflects the visual context.
2. Relevance: Directly answers the user's question without fluff.
3. Clarity: Clear, well-structured explanation.

Return ONLY a valid JSON object with:
{{
  "selected_model": "<model_name>",
  "best_response": "<full text of chosen response>",
  "reasoning": "<short rationale for selection>"
}}
"""

# 3. Run the Judge model (e.g., using GPT-4o or Claude 3.5 Sonnet)
judge_decision = completion(
    model="gpt-4o",
    messages=[{"role": "user", "content": judge_prompt}],
    response_format={"type": "json_object"},
)

result = json.loads(judge_decision.choices[0].message.content)

print(f"Selected: {result['selected_model']}")
print(f"Reason: {result['reasoning']}\n")
print(f"Final Output:\n{result['best_response']}")