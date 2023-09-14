"""
1) break: terminates execution of the loop immediately
    a) it terminates only the innermost loop in which it's contained; In a nested loop, a break statement inside the
     inner loop will terminate only the inner loop
2) continue: skips ahead to the next iteration
    b) all statements in the loop body that appear after continue are skipped no matter its in inner loop or outer
"""
# ---------------------------------------- break: finish before iteration ----------------------------------------
s = 'He1nr8y'
digit_index1 = -1  # This will be -1 until we find a digit

for i in range(len(s)):
    if digit_index1 == -1 and s[i].isdigit():
        digit_index1 = i

# Even though the work of a loop is done, it still finishes until the end of string is reached
print(digit_index1)

# terminate the loop early by using a break statement
digit_index2 = -1
for i in range(len(s)):
    if s[i].isdigit():
        digit_index2 = i
        break

print(digit_index2)

# ---------------------------------------- continue: skip to next iteration ----------------------------------------
total = 0
count = 0
for i in range(len(s)):
    if s[i].isalpha():
        continue
    total += int(s[i])
    count += 1

print(total)
print(count)
