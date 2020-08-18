# Problem: If you had deposited a coin on the cryptocurrency exchange that brought 7% fixed profit daily for a week, how much would your $ 1000 reach at the end of the 7th day?

rate = .07
present_value = 1000
periods = 7

future_value = present_value * (1 + rate)**periods  # future value
future_value_str = str(round(future_value, 2))
answer=f"At the end of the {periods}th day my original investment of ${present_value} at {rate} rate will have a value of ${future_value_str}."
print(answer) 
