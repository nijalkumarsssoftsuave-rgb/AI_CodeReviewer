# from config.ai_config import MAX_RETRIES, TARGET_FILE
# from utils.file_utils import (
#     read_file,
#     write_file,
#     is_syntax_valid,
#     is_code_valid,
#     backup_file,
#     file_exists
# )
# from agents.fixer_agents import request_fix
#
# def run_fix_loop():
#
#     if not file_exists(TARGET_FILE):
#         print(f"Target file not found: {TARGET_FILE}")
#         return
#
#     retries = 0
#
#     while retries < MAX_RETRIES:
#
#         code = read_file(TARGET_FILE)
#         valid, message = is_code_valid(code)
#
#         if valid:
#             print("\nSyntax valid. No fixes required.")
#             return
#
#         print(f"\nIteration {retries + 1}")
#         print("Detected Syntax Error:", message)
#
#         backup_path = backup_file(TARGET_FILE)
#         print("Backup created:", backup_path)
#
#         fixed_code = request_fix(code, message)
#
#         if not fixed_code:
#             print("LLM returned empty response. Aborting.")
#             return
#
#         write_file(TARGET_FILE, fixed_code)
#
#         revalid, reval_msg = is_syntax_valid(fixed_code)
#
#         if revalid:
#             print("Fix successful. Syntax is now valid.")
#             return
#         else:
#             print("Fix did not resolve syntax:", reval_msg)
#
#         retries += 1
#
#     print("\nMax retries reached. Manual repair required.")
#
# if __name__ == "__main__":
#     run_fix_loop()

from fastapi import FastAPI
from routes.route import router as agentic_router

app = FastAPI()
app.include_router(agentic_router)
