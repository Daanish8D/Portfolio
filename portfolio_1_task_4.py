matches_played = int(input("Enter number of matches played "))
times_batted = int(input("Enter number of times batted "))
not_out = int(input("Enter number of times not out "))
runs_scored = int(input("Enter number of runs scored "))

batting_average = runs_scored/(times_batted-not_out)

print("Your batting average is", batting_average)
