from groq import Groq

class CloudPilot:
    def predict(self,prompt,context):
        print(context)
        client = Groq(api_key="")
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                    {
                        "role": "system",
                        "content": "You are a AWS website helper."+
                        "This is the list of objects which are the ui elements"+ context +
                        """Give me the 1 most relevent object only that can help to progress in the given task and
                        extract the object from the list give me only the className with respect to the textName in that object from it.
                        (dont use \ in the format above)
                        (dont give additional description or opinion just the answer format)
                        (dont answer any question that is outside the AWS website)"""
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
