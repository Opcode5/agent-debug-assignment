import re
import json
import random
from unit_converter.converter import UnitConverter
from utility.constants import (
    OPERATOR,
    TEMPS,
)

def get_temperature(city: str):
    city = (city or "").strip()

    return TEMPS.get(city, 20)

def has_unit_in_question(expression: str)-> bool: 
    all_units = list(UnitConverter._CONVERSION_FACTORS.keys()) + list(UnitConverter._TEMP_UNITS)
    
    for curr in all_units: 
        if re.search(rf"\b{curr}\b", expression):
            return True
        
    return False

def evaluate_percent_of_expression(expression: str):
    try:
        numbers = re.findall(r'[+-]?\d+(?:\.\d+)?', expression)

        percentage = float(numbers[0])
        base_value = float(numbers[1])

        return (percentage/100.0)*base_value
    except Exception:
        return eval(expression)

def get_operator(expression: str)->str: 
    for key, symbol in OPERATOR.items():
        if key in expression:
            return symbol
    
    return ""

def calculate_expression_value(expression: str)->str:
    cities = [city for city in TEMPS.keys() if city in expression]

    sum_of_temperatures = 0
    for city in cities:
        sum_of_temperatures += get_temperature(city)

    average_temperature = sum_of_temperatures / len(cities)

    match = re.search(r"[-+]?\d*\.?\d+", expression)
    num = 0

    if match:
        num = float(match.group())

    temp_expression_str = str(average_temperature) + get_operator(expression) + str(num)

    return str(eval(temp_expression_str)) + " degree celsius"

def get_random_answer()->str: 
    with open("data/random.json", "r") as file:
        data = json.load(file)
        random_answer = random.choice(data["answers"])

        return random_answer