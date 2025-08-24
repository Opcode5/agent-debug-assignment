# Refactor & Extend: Simple Tool-Using Agent

**Goal:** Turn a brittle, partially working agent into production-quality code, then extend it with a new tool and real tests.

---
You must **refactor for robustness**, **add one new tool** (translator / unit converter), and **add proper tests**.
---

## Your Tasks (Summary)

1. **Refactor**
2. **Improve**
3. **Add ONE new tool** 
4. **Write tests**
5. **Improve Documentation**

See the assignment brief for full details (shared in the job post).

---

## Quick Start

### Python 3.10+ recommended

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run

```bash
python main.py "What is 12.5% of 243?"
python main.py "Summarize today's weather in Paris in 3 words"
python main.py "Who is Ada Lovelace?"
python main.py "Add 10 to the average temperature in Paris and London right now."
```

### Test

```bash
pytest -q
```

> Note: The fake LLM sometimes emits malformed JSON to simulate real-world flakiness.

---

## What we expect you to change

- Split responsibilities into modules/classes.
- Add a schema for tool plans; validate inputs and tool names.
- Make tool calls resilient and typed;
- Add one new tool and tests that prove your design is extensible.
- Update this README with an architecture diagram (ASCII ok) and clear instructions.
- You can use Real LLMs or a fake one, but ensure your code is robust against malformed responses.

Good luck & have fun!

<!-- -------------------------------------------------------------------- -->

## Folder Structure
- agent 
    - agent.py -> call answer function  for the question
    - llm.py -> LLM will prepare a dictionary based on the question
    - tools.py -> There are 4 types of tools we have used. 
        - 1. evaluate
        - 2. summarize_temperature
        - 3. kb_lookup
        - 4. convert_unit
- data -> there are some predetermined answers and knowledge based informations
- tests -> All the unit tests files will be here. 
- unit converter -> All the necessary utility functions for the converter are placed in this folder
- utility 
    - constants.py -> Constant files are placed here. 
    - helper.py -> All the helper function will be here
- app.log -> logging information will be stored here

## How to use ask questions to LLM ?
- You need to ask question via command line interface
    - ask your question like: python main.py "Your question"

## Which types of questions LLM can answer?
- Currently LLM can answer some predetermined questions and for others, it will reponse like "There's no enough data to get answer"
- LLM can calculate the percentage of a number
    - LLM can answer the following types of questions: 
        - What is 12.5% of 243?
        - Tell me 18% of 2000
        - 30% of 200

- LLM can tell us the temperature of dhaka, london, paris, amsterdam
    - LLM can answer the following types of questions: 
        - Temperature of dhaka
        - Tell me the temperature of dhaka
    - LLM can summarize the temperature of a city
        - Summarize today's weather in Paris in 3 words
        - Summarize today's weather in Paris
        - tell me the  weather of dhaka in words
    - LLM can do arithmatic operation with the average temperature of some cities
        - Add 5  to the average temperature of  Paris, London and dhaka right now
        - subtract 3  to the average temperature of  Paris, London and dhaka right now
        - please multiply 2  to the average temperature of London and dhaka

- LLM can answer some knowledge based question
    - LLM can answer the following types of questions: 
        - Who is Ada Lovelace?
        - Who is Ada Lovelace and alan turin?
        - Who is Ada Lovelace, Shakib and alan turin?

# New feature
- We have integrated unit coverted as a new feature with this assignment
    - Unit converter can convert the following units
        - conversion between meter, kilometer, mile, foot
        - conversion between kilogram, gram
        - conversion between liter, mili liter
        - conversion between usd, eur
        - conversion between celsius, fahrenheit, kelvin temperature
    - LLM can answer the following types of questions: 
        - convert 2 kg to gram
        - 2 kg to gram
        - convert 2 kilogram to gram
        - 2 kilogram to g
        - 500 g to kg
        - please convert 500 meter to km
        - convert 500 meter to kilometer
        - convert 0.5 km to meter
        - 2 usd to eur
        - 2.5 eur to usd
        - 10 degree celsius to kelvin
        - 10 c to kelvin
        - 10 c to k
        - 500 kelvin to fahrenheit
        - 100 c to fahrenheit
## unit test
- To run the unit test , please run this command: pytest -v
- Currently We have unit test for only call_LLM function


