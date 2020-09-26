
a = str(input("Enter string :"))
number = '0123456789'
answer = ''
counterNumber = 0
answerInt = 0
counter = 0

for c in a:
    counter += 1

n = 0
while n < counter:
    i = 0
    while i < 10:
        if a[n] == number[i]:
            answer += a[n]
        i += 1
    n += 1

for cn in answer:
    counterNumber += 1

j = 0
while j < counterNumber:
    if j == 0:
        if answer[j] == '1':
            answerInt += 1
        elif answer[j] == '2':
            answerInt += 2
        elif answer[j] == '3':
            answerInt += 3
        elif answer[j] == '4':
            answerInt += 4
        elif answer[j] == '5':
            answerInt += 5
        elif answer[j] == '6':
            answerInt += 6
        elif answer[j] == '7':
            answerInt += 7
        elif answer[j] == '8':
            answerInt += 8
        elif answer[j] == '9':
            answerInt += 9

    if j == 1:
        if answer[j] == '0':
            answerInt = ((10**j)*answerInt)
        elif answer[j] == '1':
            answerInt = ((10**j)*answerInt)+1
        elif answer[j] == '2':
            answerInt = ((10**j)*answerInt)+2
        elif answer[j] == '3':
            answerInt = ((10**j)*answerInt)+3
        elif answer[j] == '4':
            answerInt = ((10**j)*answerInt)+4
        elif answer[j] == '5':
            answerInt = ((10**j)*answerInt)+5
        elif answer[j] == '6':
            answerInt = ((10**j)*answerInt)+6
        elif answer[j] == '7':
            answerInt = ((10**j)*answerInt)+7
        elif answer[j] == '8':
            answerInt = ((10**j)*answerInt)+8
        elif answer[j] == '9':
            answerInt = ((10**j)*answerInt)+9

    if j > 1:
        if answer[j] == '0':
            answerInt = ((10**j)*answerInt)//(10**(j-1))
        elif answer[j] == '1':
            answerInt = ((10**j)*answerInt)//(10**(j-1))+1
        elif answer[j] == '2':
            answerInt = ((10**j)*answerInt)//(10**(j-1))+2
        elif answer[j] == '3':
            answerInt = ((10**j)*answerInt)//(10**(j-1))+3
        elif answer[j] == '4':
            answerInt = ((10**j)*answerInt)//(10**(j-1))+4
        elif answer[j] == '5':
            answerInt = ((10**j)*answerInt)//(10**(j-1))+5
        elif answer[j] == '6':
            answerInt = ((10**j)*answerInt)//(10**(j-1))+6
        elif answer[j] == '7':
            answerInt = ((10**j)*answerInt)//(10**(j-1))+7
        elif answer[j] == '8':
            answerInt = ((10**j)*answerInt)//(10**(j-1))+8
        elif answer[j] == '9':
            answerInt = ((10**j)*answerInt)//(10**(j-1))+9
    j += 1

print('answer :', answer)
print('answerInt :', answerInt)
print('Type answerInt :', type(answerInt))
