import random

# 生成随机变量名
def generate_variable_name():
    return f"var{random.randint(1, 100)}"

# 生成随机的数值
def generate_random_value():
    return random.randint(0, 100)

# 生成随机的操作符
def generate_random_operator():
    return random.choice(['+', '-', '*', '/'])

# 生成随机的条件操作符
def generate_random_condition_operator():
    return random.choice(['==', '!=', '>', '<', '>=', '<='])

# 生成随机的赋值语句
def generate_assignment():
    return f"{generate_variable_name()} = {generate_random_value()}"

# 生成随机的条件语句
def generate_if_statement():
    var1 = generate_variable_name()
    var2 = generate_variable_name()
    condition = generate_random_condition_operator()
    return f"if {var1} {condition} {var2}:\n    {generate_assignment()}"

# 生成随机的循环语句
def generate_for_loop():
    var = generate_variable_name()
    return f"for {var} in range({generate_random_value()}):\n    {generate_assignment()}"

# 生成代码行
def generate_code_line():
    return random.choice([generate_assignment(), generate_if_statement(), generate_for_loop()])

# 生成指定行数的代码
def generate_code(lines):
    code = ""
    for _ in range(lines):
        code += generate_code_line() + "\n"
    return code

# 生成指定行数的代码并打印
def main():
    lines = int(input("Enter the number of lines of code to generate: "))
    code = generate_code(lines)
    print("Generated Code:\n")
    print(code)

if __name__ == "__main__":
    main()
