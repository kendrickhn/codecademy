import random 

name = ""
question = ""
random_number = random.randint(1,9)

# Determine the answer based on the random number
answers = {
  1: 'Yes - definitely',
  2: 'It is decidedly so',
  3: 'Without a doubt',
  4: 'Reply hazy, try again',
  5: 'Ask again later',
  6: 'Better not tell you now',
  7: 'My sources say no',
  8: 'Outlook not so good',
  9: 'Very doubtful'
}
answer = answers.get(random_number, 'Error')

# Determine the output based on the input
if question == (''):
  print('No self-doubt shall lead you to being ignorant')
elif name == (''): 
  print('Question: ',question)
  print(answer)
else: 
  print(name,' asks: ',question)
  print(answer)


