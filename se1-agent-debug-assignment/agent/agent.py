import logging
from .llm import call_LLM
from agent import tools
from utility.helper import(
    get_temperature,
    get_random_answer,
)

def answer(question: str):
    try: 
        plan = call_LLM(question)
        print(plan)
        
        if plan and isinstance(plan, dict) and "tool" in plan:
            if plan["tool"] == "calc":
                evaluated_result = tools.evaluate(plan["args"]["expr"])

                return evaluated_result
            
            elif plan["tool"] == "weather":
                city = plan["args"]["city"]
                temperature = get_temperature(city)

                return f"{temperature} degree celsius"
            
            elif plan["tool"] == "summarized weather":
                city = plan["args"]["city"]
                summarized_temperature = tools.summarize_temperature(city)

                return summarized_temperature

            elif plan["tool"] == "kb":
                return tools.kb_lookup(plan["args"]["name"])
            
            elif plan["tool"] == "convert": 
                return tools.convert_unit(plan["args"]["expr"])

        return get_random_answer()
    except Exception as e:
        logging.error("Error while preparing answer for the question", exc_info=True)

        return "Error while preparing answer for the question"
