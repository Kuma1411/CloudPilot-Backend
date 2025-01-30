from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class CloudPilot:
    def predict(self,prompt,context):
        print(context)
        client = Groq(api_key=os.getenv('MODEL_API'))
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                    {
                        "role": "system",
                        "content": "You are a AWS website helper."+
                        """Give me the 1 most relevent object only that can help to progress in the given task and
                        extract the object from the list give me ONLY the className

                        DONT give in this format:
                        UI(className='awsui_trigger_lpshu_v9srd_145 awsui_trigger-button-styles_lpshu_v9srd_145 awsui_drawers-trigger_1kzri_g64w2_250 awsui_drawers-trigger_1fj9k_z5zo8_18 awsui_drawers-trigger-global_1fj9k_z5zo8_19', textContent='') 
                        className: awsui_drawers-trigger-global_1fj9k_z5zo8_19

                        GIVE like this format:
                        awsui_trigger_lpshu_v9srd_145 czxcvzx   xzcvzxc v xczzvs
                        
                        (Never give anything else other than className)
                        (dont use \ in the format above)
                        (dont give additional description or opinion just the answer format)
                        (dont answer any question that is outside the AWS website)""" +
                        "This is the list of objects which are the ui elements"+ context 
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