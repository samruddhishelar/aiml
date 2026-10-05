# Q14. Rule-Based Expert System

marks = int(input("Enter your marks: "))

if marks >= 75:
    result = "Excellent"
    advice = "Keep up the good work!"

elif marks >= 50:
    result = "Pass"
    advice = "Good job, but try to improve."

else:
    result = "Fail"
    advice = "Work harder and study regularly."

print("\nResult:", result)
print("Advice:", advice)