# This program has a user interface that allows the user to select from four options to have the process
# of facial analysis performed on three stored images of Nikola Tesla, Mahatma Gandhi, and John F. Kennedy,
# with fourth option being to quit the program cleanly. It has error handling in the main function and menu
# function to ensure no exceptions are raised. The output of the  program prints the analysis of the pictures
# which includes the person's age, race, emotion and gender and then also displays the image that was analyzed.

# Installed packages and calling the imports. DeepFace is used for facial analysis and Pillow to display
# the images
from deepface import DeepFace
import cv2
from PIL import Image

# importing the images
image1_path = 'gandhi.jpg'
image2_path = 'nikolatesla.jpg'
image3_path = 'JFK.jpg'
# confirming the path of images
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)
image3 = cv2.imread(image3_path)

# Global Constants for Main function
CHOICE_1 = 1
CHOICE_2 = 2
CHOICE_3 = 3
QUIT = 4


# Function that calls the menu with error handling and allows the user
# to keep search tweets until they are ready to quit
def main():
    menu()
    choice = 0
    while choice != QUIT:
        choice = int(input('Please Enter Your Selection: '))
        if choice == CHOICE_1:
            tesla()
        elif choice == CHOICE_2:
            gandhi()
        elif choice == CHOICE_3:
            jfk()
        elif choice == QUIT:
            print('Hasta La Vista! See You Later!')
        else:
            print('Error. Please Enter a valid selection. ')


# main menu function gives, tells the user what the program
def menu():
    print()
    print('Welcome to Facial Recognition')
    print('************************************************')
    print('Enter 1 To Analyze a Picture of Nikola Tesla')
    print('Enter 2 To Analyze a Picture of Mahatma Gandhi')
    print('Enter 3 to Analyze a Picture of JFK')
    print('Enter 4 to Exit the Program')
    print()


# function to analyze image of Nikola Tesla
def tesla():
    # Initialize a variable to analyze the facial features
    face = DeepFace.analyze(img_path="nikolatesla.jpg", actions=['age', 'gender', 'race', 'emotion'])
    # Prints the results of the analysis
    print(face["age"], " years old ", face["dominant_race"], " ", face["dominant_emotion"], " ", face["gender"])
    # Initialize Variable to hold the image for the show function
    display = Image.open('nikolatesla.jpg')
    # Calling the show function to show the image on the user's screen
    display.show()


# function to analyze a image of Gandhi
def gandhi():
    # Initialize a variable to analyze the facial features
    face = DeepFace.analyze(img_path="gandhi.jpg", actions=['age', 'gender', 'race', 'emotion'])
    # Prints the results of the analysis
    print(face["age"], " years old ", face["dominant_race"], " ", face["dominant_emotion"], " ", face["gender"])
    # Initialize Variable to hold the image for the show function
    display = Image.open('gandhi.jpg')
    # Calling the show function to show the image on the user's screen
    display.show()

# function to analyze an image of John F. Kennedy
def jfk():
    # Initialize a variable to analyze the facial features
    face = DeepFace.analyze(img_path="JFK.jpg", actions=['age', 'gender', 'race', 'emotion'])
    # Prints the results of the analysis
    print(face["age"], " years old ", face["dominant_race"], " ", face["dominant_emotion"], " ", face["gender"])
    # Initialize Variable to hold the image for the show function
    display = Image.open('JFK.jpg')
    # Calling the show function to show the image on the user's screen
    display.show()


# Calling the Main Function
main()
