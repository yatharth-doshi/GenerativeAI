from generate_response import generate_response
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Initialize the model
tokenizer = AutoTokenizer.from_pretrained("lmsys/fastchat-t5-3b-v1.0")
model = AutoModelForSeq2SeqLM.from_pretrained("lmsys/fastchat-t5-3b-v1.0")

def gen_ai(knowledge_level, repo_info, question):
        
        response = generate_response(knowledge_level, repo_info, question)

        # Specify model parameters
        input_ids = tokenizer.encode(response, return_tensors="pt")
        attention_mask = torch.ones_like(input_ids)
        output = model.generate(
            input_ids,
            max_length=512,
            temperature=0.1,
            num_return_sequences=1,
            do_sample=True,
            attention_mask=attention_mask
        )
        answer = tokenizer.decode(output[0], skip_special_tokens=True)
        answer = answer.replace("<pad>", "")

        return answer