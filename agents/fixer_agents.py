from llm_client import request_fix
from runner import run_code
from config import MAX_RETRIES

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def autonomous_fix_loop(filepath: str):
    retries = 0

    while retries < MAX_RETRIES:
        retries += 1

        code = read_file(filepath)
        success, output = run_code(filepath)

        if success:
            print(f"\n✔ Code executed successfully (iteration {retries})")
            print(output)
            return

        print(f"\n✖ Failure detected (iteration {retries})")
        print(output)

        fixed_code = request_fix(code, output)

        write_file(filepath, fixed_code)
        print("\n↺ Applied LLM fix")

    print("\n⚠ Max retries reached. Manual review required.")
