from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class CloudPilot:
    def predict(self,prompt,context):
        client = Groq(api_key=os.getenv('MODEL_API'))

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                    {
                        "role": "system",
                        "content": """
                        You are a AWS website navigator and helper. You will be provided with an array of words each word represent a ui element which can be:
                        1. button 
                        2. a
                        3. input
                        4. select
                        5. textarea
                        
                        For a given task give me the only 1 name and the most relevent name that will help to increase the progress in the given task.
                        Give me only the name from the array.

                        The array:
                        """+ context
                        
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,

            )
        return completion.choices[0].message.content
