import json
import os
from openai import OpenAI

# 1. Initialize client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# 2. Define actual tools (functions) the agent can execute
def get_order_status(order_id: str) -> str:
    """Mock database lookup for an order status."""
    database = {
        "ORD-101": {"item": "Wireless Headphones", "status": "Processing", "address": "123 Main St"},
        "ORD-202": {"item": "Mechanical Keyboard", "status": "Shipped", "address": "456 Oak Ave"}
    }
    order = database.get(order_id)
    if not order:
        return json.dumps({"error": "Order not found."})
    return json.dumps(order)

def calculate_discount(price: float, percentage: float) -> str:
    """Calculates discounted price."""
    discounted = price * (1 - percentage / 100)
    return json.dumps({"original_price": price, "discounted_price": round(discounted, 2)})

# Map function names to their actual Python callable
AVAILABLE_TOOLS = {
    "get_order_status": get_order_status,
    "calculate_discount": calculate_discount
}

# 3. Define the tool schemas for OpenAI Function Calling
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "get_order_status",
            "description": "Retrieve current status, items, and address for a given order ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {"type": "string", "description": "The order identifier, e.g., 'ORD-101'"}
                },
                "required": ["order_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_discount",
            "description": "Calculate the price of an item after applying a percentage discount.",
            "parameters": {
                "type": "object",
                "properties": {
                    "price": {"type": "number", "description": "Base price of the product"},
                    "percentage": {"type": "number", "description": "Discount percentage to apply (0-100)"}
                },
                "required": ["price", "percentage"],
            },
        },
    }
]

# 4. The Agent Execution Loop
def run_agent(user_query: str, max_turns: int = 5):
    messages = [
        {"role": "system", "content": "You are an intelligent customer support agent capable of checking database records and calculating discounts."},
        {"role": "user", "content": user_query}
    ]

    for turn in range(max_turns):
        print(f"\n--- Turn {turn + 1} ---")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools_schema,
            tool_choice="auto"
        )
        
        response_message = response.choices[0].message
        messages.append(response_message)

        # If model returned no tool calls, it has finished reasoning and produced the final response
        if not response_message.tool_calls:
            print("\n[Agent Final Response]:")
            print(response_message.content)
            return response_message.content

        # Handle tool calls dynamically
        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            print(f"[Tool Execution] Calling '{function_name}' with arguments: {function_args}")
            
            # Execute Python function
            tool_fn = AVAILABLE_TOOLS.get(function_name)
            if tool_fn:
                tool_output = tool_fn(**function_args)
            else:
                tool_output = json.dumps({"error": "Tool not implemented."})

            # Send tool execution result back into the agent context
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": tool_output
            })

if __name__ == "__main__":
    prompt = "Can you check the status of order ORD-101? Also, if the base price is $120, what would it cost with a 15% promotional discount applied?"
    run_agent(prompt)