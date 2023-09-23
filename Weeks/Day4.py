score=0
height=1.8
isWinning=True

#f-String

print(f"your score is {score},your height is {height},you are winning is {isWinning}")

#create a program using math and f-String that tell us how many days ,
# weeks,months we have left if we live until 90 year old ,


age=input("What is your current age?")
age_as_int=int(age)
years_remaining=90-age_as_int
days_remaining=years_remaining*363
week_remaining=years_remaining*52
months_remaining=years_remaining*12

message=f"You have {days_remaining} days,{week_remaining} weeks,and {months_remaining} months left"
print(message)