# import ast
# import shutil
# import os
#
# def read_file(path: str) -> str:
#     with open(path, "r", encoding="utf-8") as f:
#         return f.read()
#
# def write_file(path: str, content: str):
#     with open(path, "w", encoding="utf-8") as f:
#         f.write(content)
#
# def backup_file(path: str):
#     backup_path = path + ".bak"
#     shutil.copy(path, backup_path)
#     return backup_path
#
# def is_syntax_valid(code: str):
#     try:
#         ast.parse(code)
#         return True, "OK"
#     except SyntaxError as e:
#         return False, f"{e.msg} (line {e.lineno})"
#
# def is_code_valid(code: str):
#     try:
#         compiled = compile(code, "<string>", "exec")
#         exec(compiled, {})
#         return True, "OK"
#     except Exception as e:
#         return False, str(e)
#
#
# def file_exists(path: str) -> bool:
#     return os.path.exists(path)

import os

def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path: str, content: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def file_exists(path: str) -> bool:
    return os.path.exists(path)
