import google.generativeai as genai

class GoogleLLM:
    def __init__(self, api_key: str, system_prompt: str = ""):
        self.api_key = api_key
        self.system_prompt = system_prompt
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')  # or another model name

    def set_system_prompt(self, prompt: str):
        self.system_prompt = prompt

    def generate(self, user_input: str) -> str:
        # Combine system prompt and user input
        prompt = self.system_prompt + "\n" + user_input if self.system_prompt else user_input
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {e}"


