import google.generativeai as genai

genai.configure(api_key="AlzaSyBIXM-Pi3vl6l8wRhQmmGo54-Ol_yfEOkU")
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("say hi")
print(response.text)