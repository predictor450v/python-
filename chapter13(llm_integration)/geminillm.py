from google import genai

client = genai.Client(api_key="AIzaSyC7xU1fFOIRpCjCAsNSV3uz-gyTRXXXXXXX")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="whp is ayushman sikder"
)
print(response.text)