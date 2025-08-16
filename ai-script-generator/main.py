import os
from openai import OpenAI

# 🔑 Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_api_key_here"

client = OpenAI()

def generate_test(scenario):
    prompt_template = open("prompts/playwright_prompt.txt").read()
    prompt = prompt_template.replace("{scenario}", scenario)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    test_code = response.choices[0].message.content

    # Save generated test to file
    output_file = "outputs/generated_test.js"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(test_code)

    print(f"✅ Test generated and saved to {output_file}")

if __name__ == "__main__":
    scenario = input("Enter your test scenario: ")
    generate_test(scenario)