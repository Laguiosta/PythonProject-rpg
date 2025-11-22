user_rate = float(input("Enter your rating: "))

if user_rate >= 4.5:
  print("Extraordinary")
elif user_rate >= 4:
  print("Excellent")
elif user_rate >= 3:
  print("Good")
elif user_rate >= 2:
  print("Fair")
else:
  print("Poor")