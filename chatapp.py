from transformers import pipeline 
qa_bot=pipeline("question-answering")
pc_context = """
A computer's CPU (Central Processing Unit) is often called the brain of the computer.
It performs calculations, runs programs, and processes instructions. RAM (Random Access Memory)
is the memory used to store active tasks, which helps the computer multitask smoothly.
An SSD (Solid State Drive) is a storage device that is much faster than traditional HDDs.
For gaming, at least 16GB of RAM is recommended. A GPU (Graphics Processing Unit) handles
graphics rendering, especially important for gaming and video editing tasks. A power supply unit (PSU)
converts electricity from the wall into usable power for the internal components.
"""

print("welcome to PC Helpdesk chatbot")
print("Type your Question below")
while True:
    ques=input("you:")
    if ques.lower() in ['exit','quit']:
        print("Thank you for using chat bot")
        break
    result==qa_bot(question=ques,context=pc_context)
    answer=result['answer']
    print(f"Bot:{answer}\n")


