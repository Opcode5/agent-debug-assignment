import logging
import json
import re
import time
from unit_converter.converter import UnitConverter
from utility.helper import (
    evaluate_percent_of_expression,
    get_temperature,
    calculate_expression_value,
)

def evaluate(expr: str) -> float:
    start = time.perf_counter()

    expression = expr.lower().replace("what is","").strip().rstrip('?')

    if "% of" in expression:
        return evaluate_percent_of_expression(expression)
    
    result = calculate_expression_value(expression)

    end = time.perf_counter()

    logging.info(f"evaluate function takes {end - start:.4f} seconds")

    return result
    
def summarize_temperature(city: str) -> str:
    start = time.perf_counter()

    temp_desc=""
    condition=""

    temperature = get_temperature(city)

    if temperature < 10:
        temp_desc = "Cold"
    elif temperature < 20:
        temp_desc = "Mild"
    elif temperature < 30:
        temp_desc = "Warm"
    else:
        temp_desc = "Hot"

    if temperature < 15:
        condition = "cloudy"
    elif temperature < 25:
        condition = "clear"
    else:
        condition = "sunny"

    end = time.perf_counter()
    logging.info(f"summarize_temperaturefunction takes {end - start:.4f} seconds")

    return f"{temp_desc} and {condition}"

def kb_lookup(topics: str) -> str:
    try:
        start = time.perf_counter()

        data={}
        answer ={}

        with open("data/kb.json","r") as file:
            data = json.load(file)

        for topic in topics:
            # Default value if no match found
            answer[topic] = "Currently we don’t have any information on this topic."

            for item in data.get("topics", []):
                name = item.get("name", "").lower()
                summary = item.get("summary", "")

                if topic in name:
                    answer[topic] = summary
                    break

        result_str = "\n".join(f"{topic}: {summary}" for topic, summary in answer.items())

        end = time.perf_counter()
        logging.info(f"knowledge base lookup function takes {end - start:.4f} seconds")

        return result_str
    except Exception as e:
        logging.error("Error while preparing knowledge base answer", exc_info=True)
        
        return f"KB error: {e}"
    
def convert_unit(expression: str):
    try:
        start = time.perf_counter()
        converter = UnitConverter()

        numbers = re.findall(r"\d+", expression)
        numbers = [int(num) for num in numbers]

        sum_of_numbers = sum(numbers)
        value = sum_of_numbers

        if 'average' in expression: 
            value = value / len(numbers)
        
        all_units = list(converter._CONVERSION_FACTORS.keys()) + list(converter._TEMP_UNITS)

        pattern = r'\b(' + '|'.join(all_units) + r')\b'
        matches = re.findall(pattern, expression)

        units= [curr.strip() for curr in matches]

        end = time.perf_counter()

        logging.info(f" convert_unit function took {end - start:.4f} seconds")

        if len(units)==2: 
            from_unit = units[0]
            to_unit= units[1]

            return converter.convert(value, from_unit, to_unit)
        
        logging.error("Unable to convert. It needs two units to convert from one to another")

        return "We are unable to convert it"
    except Exception as e:
        logging.error("Error while converting unit", exc_info=True)
        
        return f"Error while converting unit: {e}"