

easy_answers = ["learn","skill","information",\
                "mastery","quitting"]

easy_blanks = ["[1]-----","[2]-----","[3]-----------","[4]-------",\
               "[5]--------"]


easy = ["The best way to ",easy_blanks[0]," a new ",easy_blanks[1],
       " , like computer programming,","is to find the correct information to ",easy_blanks[0]," and then begin to ",
       "practice applying the new ",easy_blanks[2],".  When you first start out,",
       "the road to ",easy_blanks[3]," of  the ",easy_blanks[1]," is going to look never ending.",
       "If you are able to keep trying and failing without ",easy_blanks[4]," you","will continue to improve."]




medium_answers = ["always", "uncertain", "learning", "change",\
                  "intentional", "quitter"]

medium_blanks = ["[1]------","[2]---------","[3]--------","[4]------",\
                 "[5]-----------","[6]-------"]

medium = ["When you first begin a new task there are " , medium_blanks[0] ,
         medium_blanks[1] , "ties.", "The true challenge to becoming what you want to be is not ",
          medium_blanks[2], " how to do it, but rather ",medium_blanks[2],
          " how not to quit.  Your mind can", "and will ", medium_blanks[0], " ", medium_blanks[3],
          ", so make sure that you ", medium_blanks[3], " it the way you",
         "want it to be. Without ", medium_blanks[5], " and directional ", medium_blanks[3],
         ", your doubt", "will make you into an uncertain ", medium_blanks[5], "."]


hard_answers = ["direction", "deterrents", "concentrate",\
                "consecrate", "interaction"]

hard_blanks = ["[1]---------","[2]----------","[3]-----------","[4]----------",\
               "[5]-----------"]



hard = ["To determine your ", hard_blanks[0], " you must terminate all ", hard_blanks[1], " from",
       "terrorizing your intention.  If you don't mindfully ", hard_blanks[2], " on your",
       "intended reaction, then you blind-fully ", hard_blanks[3], " your emotional distractions,",
       "because every man, woman and child wants to be right in every ", hard_blanks[4], "."]


def intro():
    prompt = "***CHOOSE A LEVEL***\n--1-- : easy\n--2-- : medium\n--3-- : hard\n"
    valid_answer = ['1','2','3']
    error_message = "YOU MUST ENTER A 1, 2, or 3"
    level = check_for_number(prompt,valid_answer,error_message)
    return level

def check_for_number(prompt,valid_answer,error_message):
    user_input = raw_input(prompt)
    while True:
        try:
            int(user_input)
        except ValueError:
            print "nope"
            user_input = raw_input(error_message+'\n'+prompt)
            continue
        if user_input not in valid_answer:
            user_input = raw_input(error_message+"\n"+prompt)
            continue
        else:
            return user_input

        
level = int(intro())-1
levels = [easy,medium,hard]
current_board = levels[level]
answers = [easy_answers,medium_answers, hard_answers]
list_of_answers = answers[level]
blanks = [easy_blanks, medium_blanks, hard_blanks]
list_of_blanks = blanks[level]
        


def fill_in_blank(answer,L,blanks):
    levels[level][1] = answer
    print current_board
        
    
    

def check_for_answer(guess,correct_answer):
    if str.lower(guess) == correct_answer:
        return True
    else:
        return False


def update_blank(answer,L):
    blank = list_of_blanks[list_of_answers.index(answer)]
    new_blank = list(blank)
    while True:
        try:
            new_blank[L] = answer[L-3]
            blank = ''.join(new_blank)
        except IndexError:
            break
        else:
            break
    return blank


def display(instructions,answer,blanks):
    board = ''.join(levels[level])
    guess = raw_input("\n"+("+"*100)+"\n"+board+instructions)
    L = 3
    while check_for_answer(guess,answer) is False:
        print "HERE IS A HINT: ", update_blank(answer,L)
        L += 1
        print "\n----- WRONG! TRY AGAIN! -----\n"
        if L > len(answer)+3:
            print "TRY THE NEXT ONE"
            return
        else:
            guess = raw_input(board+instructions)
            continue
        
            
        
    else:
        L = list_of_answers.index(answer)
        new_board = fill_in_blank(answer,L,blanks)
        
        print "\n******CORRECT!********\n"
        return
        
    """find the current blank in levels update dashes with letters from """


def play_game(answers,level,blanks):
    answer_number = 1
    space_number = "["+str(answer_number)+"]"
    answer = list_of_answers[answer_number-1]
    instructions = "\n\nFILL IN THE MISSING WORD FOR SPACE #"+space_number+"\n"
    for blank in list_of_answers:
        display(instructions,answer,blanks)
        answer_number += 1
        

play_game(answers,level,blanks)







    
