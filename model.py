from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class CloudPilot:
    def instruct(self,prompt,context):
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
                        
                        you need to provide information and instruction about the given option,
                        follow this format:
                        {"instructions": ""}
                        (dont add \, \ n etc)
                        
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

    def navigate(self,prompt,context):
        client = Groq(api_key=os.getenv('MODEL_API'))

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                    {
                       "role": "system",
                        "content": """
                        You are an AWS website navigator and helper. You will be provided with an array of words, each representing a UI element. The elements can be one of the following:
                        1. button
                        2. a
                        3. input
                        4. select
                        5. textarea

                        Your goal is to provide the most relevant UI element name based on the task description. For a given task, give me only the name from the array that is most likely to help progress towards completing the task.

                        Along with the name, you need to provide instructions which describe the element and its purpose. Follow this format:
                        {"instructions": "description about the element", "name": "name of the element", "isCompleted": "false"}

                        **Important**: 
                        - Do not set `isCompleted` to `true` initially.
                        - You should set `isCompleted` to `true` only when you encounter the word that marks the completion of the task (e.g., the word "instance" for a task about creating an EC2 instance).
                        - Continue providing the most relevant UI element until you find the one that completes the task. Only then should `isCompleted` be set to `true`.

                        Example:
                        If the user is asking about creating an EC2 instance and the word "create instance or something like this" appears in the array, then at that point, set `isCompleted` to `true` because the task is complete.
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
