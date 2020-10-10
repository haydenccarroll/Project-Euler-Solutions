import time
start = time.time()
#one thousand four hundred and seventy two
int_to_letter_count = {
                        0:'',
                        1:'one',
                        2:'two',
                        3:'three',
                        4:'four',
                        5:'five',
                        6:'six',
                        7:'seven',
                        8:'eight',
                        9:'nine',
                        10:'ten',
                        11:'eleven',
                        12:'twelve',
                        13:'thirteen',
                        14:'fourteen',
                        15:'fifteen',
                        16:'sixteen',
                        17:'seventeen',
                        18:'eighteen',
                        19:'nineteen',
                        20:'twenty',
                        30:'thirty',
                        40:'forty', 
                        50:'fifty',
                        60:'sixty',
                        70:'seventy',
                        80:'eighty',
                        90:'ninety',
                        'hundred':'hundred',
                        'thousand':'thousand',
                        'and':'and'

                    }

running_length = ''
for i in range(1, 1001):
    if i <= 20:
        running_length += int_to_letter_count[i]
    elif 20 < i < 100:
        running_length += int_to_letter_count[int(str(i)[0])*10]
        if i % 10 != 0:
            running_length += int_to_letter_count[int(str(i)[1])]
    elif 100 <= i < 1000:
        running_length += int_to_letter_count[int(str(i)[0])]
        running_length += int_to_letter_count['hundred']
        if i % 100 != 0:
            running_length += int_to_letter_count['and']
            if int(str(i)[1:]) <= 20:
                running_length += int_to_letter_count[int(str(i)[1:])]
            else:
                running_length += int_to_letter_count[int(str(i)[1])*10]
                running_length += int_to_letter_count[int(str(i)[2])]
                
    elif i == 1000:
        running_length += int_to_letter_count[1]
        running_length += int_to_letter_count['thousand']
    #running_length += ' '


print(len(running_length))
print('runtime:',time.time()-start)
