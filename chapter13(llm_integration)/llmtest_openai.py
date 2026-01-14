

'''
in terminal 
setx OPENAI_API_KEY "your_real_key_here" /M
'''


from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)


