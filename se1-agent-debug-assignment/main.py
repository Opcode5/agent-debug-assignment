import sys
import logging
from agent.agent import answer

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("app.log"),   # store logs in a file
            ]
    )

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Please provide a question as an argument\"")
        sys.exit(1)

    question = " ".join(sys.argv[1:])
    output = answer(question)

    print(output)

if __name__ == "__main__":
    setup_logging()
    main()
