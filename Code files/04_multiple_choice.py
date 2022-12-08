# %%
import random
import csv

ch1_terms = []

with open("../sample_data/quiz_terms.csv") as term_file:
    reader_object = csv.reader(term_file)
    for term in reader_object:
        ch1_terms.append(term[0])
term_file.close()

print(ch1_terms)

# %%
import random
import csv

ch1_answers=[]

with open("../sample_data/quiz_answers.csv") as answer_file:
    reader_object = csv.reader(answer_file)
    for ans in reader_object:
        ch1_answers.append(ans[0])
term_file.close()
print(ch1_answers)

# %%
def doQuiz(number_of_questions):

    score = 0

    for i in range(int(number_of_questions)):

        ch1_terms = ['Scientific management',
                        'Theory X',
                        'Theory Y',
                        'Theory Z',
                        'Behavioural science',
                        'Learning organization',
                        'Culture',
                        'Cross-cultural management',
                        'Cultural dimensions']

        ch1_answers = ['Theory of management proposed by Frederick W. Taylor in 1911 to increase industrial efficiency through systematic and data-driven methods.',
                        'Managerial approach assuming that employees are by nature lazy and unwilling to work unless they are closely supervised, controlled, rewarded and punished.',
                        'Managerial approach assuming that employees are willing to work, learn, seek out responsibility and grow in their careers if given the opportunity.',
                        'Managerial approach promoting loyalty and well-being of the employee through long-term employment, sense of cohesion and sense of moral obligation to serve the organization.',
                        'Scientific disciplines including psychology, sociology, cognitive sciences and anthropology exploring the principles of human behaviour and its interaction with its complex environment.',
                        'An organization that facilitates learning and knowledge transfer at all levels to continuously transform itself to meet challenges.',
                        'Values, assumptions, beliefs, norms, and behavioural patterns shared by a group of individuals that differentiate them from others.',
                        'Managerial approach aiming at understanding the extent to which and the ways in which cultural context influences behaviour at multiple levels thus improving the effectiveness of cross-cultural encounters.',
                        'Values, assumptions, beliefs and norms along which cultures (national or organizational level) are shown to differ in scientific research.',
                        ]

        answer_array = []
        ch1_range = range(len(ch1_terms))
        term_num = random.choice(ch1_range)
        
        term = ch1_terms[term_num]
        right_answer = ch1_answers[term_num]
        ch1_answers.remove(ch1_answers[term_num])
        random.shuffle(ch1_answers)
        
        answer_array.append(right_answer)
        answer_array.append(ch1_answers[0])
        answer_array.append(ch1_answers[1])
        answer_array.append(ch1_answers[2])
        answer_array.append(ch1_answers[3])
        random.shuffle(answer_array)

        print("\n")
        print(f"########################### QUESTION #{i+1} ###########################")
        print(f"Term: {term}")

        for i in range(len(answer_array)):
            print(f"{i+1}: {answer_array[i]}") 

        user_answer = input("What is your answer?")
        answer_string = answer_array[int(user_answer)-1]

        if answer_string == right_answer:
            score+=1
            print("Correct")
            print(f"{term} = {right_answer}")
            print("\n")
        else:
            print("False")
            print(f"{term} = {right_answer}")
            print("\n")
    
    return score

# %%

number_of_questions = input("How many questions do you want?")
correct_answers = doQuiz(number_of_questions)

print(f"You answered {correct_answers}/{number_of_questions} correctly")
