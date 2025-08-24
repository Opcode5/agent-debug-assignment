import re
from utility.constants import (
    TEMPS,
)
from utility.helper import (
    get_operator,
    has_unit_in_question,
)

def call_LLM(question: str) -> dict:
    question = question.lower()

    if "weather" in question or "temperature" in question and 'average' not in question:
        # default city: dhaka
        city_name = "dhaka" 

        for city in TEMPS.keys():
            if city in question:
                city_name=city
        
        if "summarize" in question or "words" in question:
            return {"tool":"summarized weather","args":{"city": city_name}}
    
        return {"tool":"weather","args":{"city": city_name}}

    
    elif "%" in question or  get_operator(question) in ["+","-","*","/"]:
        return {"tool":"calc","args":{"expr": question}}
    
    elif "who is" in question:
        name = question.split("who is",1)[1].strip().rstrip("?")
        name_list = [x.strip() for x in re.split(r"\s*and\s*|,", name)]

        return {"tool":"kb","args":{"name":name_list}}
    
    elif has_unit_in_question(question):
        return {"tool":"convert","args":{"expr":question}}
    
    return {}

