#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random, os, shutil
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

dirPath = os.path.join(os.getcwd(), "quizzes")
if(os.path.exists(dirPath)):
    shutil.rmtree(dirPath, ignore_errors=True)
    os.makedirs(dirPath)
else:
    os.makedirs(dirPath)

# Generate 35 quiz files.
for quizNum in range(35):
    quizName = "quiz" + str(quizNum + 1) + ".txt"   
    answerKeyName = "answerkey" + str(quizNum + 1) + ".txt" 
    
    quizPath = os.path.join(os.getcwd(), "Quizzes", quizName)
    keyPath = os.path.join(os.getcwd(), "Quizzes", answerKeyName)

    # Create the quiz and answer key files.
    tempQuiz = open(quizPath, 'w')
    tempKey = open(keyPath, "w")

    # TODO: Write out the header for the quiz.
    tempQuiz.write(str(quizNum + 1) + "\n")
    tempQuiz.write("Name: __________________________\n")
    tempQuiz.write("Date: __/__/____\n")
    tempQuiz.write("\nDirections: This is a multiple choice test. Please select the letter, writing it in the space allotted, corresponding to the U.S. state name given. Good luck!\n")

    tempKey.write("Answer Key\n")
    tempKey.write("Quiz Version: " + str(quizNum + 1))

    tempKey.write("\n")
    tempQuiz.write("\n")

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        tempQuiz.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            tempQuiz.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i])) 
        tempQuiz.write('\n')

        # Write the answer key to a file.
        tempKey.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(correctAnswer)]))
    tempKey.close()
    tempQuiz.close()