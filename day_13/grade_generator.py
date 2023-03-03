print("""
Exam Grade Calculator
--------------------------------------------

""")
exam = input("Name of exam: \033[32m")
print()
maxScore = int(input("\033[0mMax. Possible Score: \033[32m"))
print()
yourScore = int(input("\033[0mYour score: \033[32m"))
print()

result = float(yourScore/maxScore * 100)
result = round(result, 2)

if result >= 90 and result <= 100:
  print("\033[0mYou have \033[32m", result, "\033[0m in", exam, "which is an \033[32mA+")
elif result >= 80 and result <= 89:
  print("\033[0mYou have \033[32m", result, "\033[0m in", exam, "which is an \033[32mA")
elif result >= 70 and result <= 79:
  print("\033[0mYou have \033[32m", result, "\033[0m in", exam, "which is an \033[32mB")
elif result >= 60 and result <= 69:
  print("\033[0mYou have \033[32m", result, "\033[0m in", exam, "which is an \033[32mC")
elif result >= 50 and result <= 59:
  print("\033[0mYou have \033[32m", result, "\033[0m in", exam, "which is an \033[32mD")
elif result >= 1 and result <= 49:
  print("\033[0mYou have \033[32m", result, "\033[0m in", exam, "which is an \033[31mE")
else:
  print("Error! Invalid input")
