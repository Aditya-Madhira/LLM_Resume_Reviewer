# LLM.py
import google.generativeai as genai

class GoogleLLM:
    def __init__(self, api_key: str):
        self.api_key = api_key
        # Hardcoded system prompt for all reviews
        self.system_prompt = (
            "You are an expert career coach. Review the following resume and provide detailed feedback "
            "on formatting, structure, grammar, and content, including actionable suggestions to improve impact:\n\n"
            "{resume_text}"
        )
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.5-pro')

    def generate(self, resume_text: str) -> str:
        # Format the prompt with the resume text
        prompt = self.system_prompt.format(resume_text=resume_text)
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            # Propagate as runtime error for FastAPI to handle
            raise RuntimeError(f"Error generating response: {e}")
