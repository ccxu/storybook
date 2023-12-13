import os

chat_language = os.getenv("INIT_LANGUAGE", default = "en")

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 7))
LANGUAGE_TABLE = {
  "en": "Hello!"
}

AI_GUIDELINES = "You are an AI teaching assistant who will use the Socratic teaching method instead of the teacher's initial response. If necessary, you will remind students to confirm with the teacher"

class Prompt:
    def __init__(self):
        self.msg_list = []
        self.msg_list.append(
            {
                "role": "system", 
                "content": f"{LANGUAGE_TABLE[chat_language]}, {AI_GUIDELINES})"
             })    
    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.msg_list.pop(0)
        self.msg_list.append({"role": "user", "content": new_msg})

    def generate_prompt(self):
        return self.msg_list