import streamlit as st

st.title('AI Spotify playlist generator')


with st.sidebar:
    Mood = st.slider(
        'Around what would you rate your mood from 0 (Sad/Somber) to 1 (Happy/Cheerful)?',
        0.0, 1.0, (0.2, 0.5))

    Tempo = st.slider(
        'What Tempo music are you looking for?',
        0.0, 150.0, (25.0, 75.0))
    
    status = st.radio('Select the type of music you want: ',
		('Instrumental', 'Vocal'))
    options = st.radio('options', ('High Energy', 'Relaxed/Mellow'), label_visibility='collapsed')
    

    if st.button('Save Configuration'):
        st.write('We will try to find music that matches your preferences:')
        st.write('Mood: ', Mood)
        st.write('Tempo: ', Tempo)
        st.write('Type: ', options, status, "music")
        Mud = Mood
        Tump = Tempo
        Stump = status
        Optump = options

    else:
        st.write('Please save a configuration')
        

user_input = st.text_input('What would you like to listen to?')
st.write('boo boo', user_input)










#Example code

# #TAKE INPUT 

# # TAKE WEIGHT INPUT in kgs
# weight = st.number_input("Enter your weight (in kgs)")

# # TAKE HEIGHT INPUT
# # radio button to choose height format
# status = st.radio('Select your height format: ',
# 				('cms', 'meters', 'feet'))

# # compare status value
# if(status == 'cms'):
# 	# take height input in centimeters
# 	height = st.number_input('Centimeters')

# 	try:
# 		bmi = weight / ((height/100)**2)
# 	except:
# 		st.text("Enter some value of height")

# elif(status == 'meters'):
# 	# take height input in meters
# 	height = st.number_input('Meters')

# 	try:
# 		bmi = weight / (height ** 2)
# 	except:
# 		st.text("Enter some value of height")

# else:
# 	# take height input in feet
# 	height = st.number_input('Feet')

# 	# 1 meter = 3.28
# 	try:
# 		bmi = weight / (((height/3.28))**2)
# 	except:
# 		st.text("Enter some value of height")

# # check if the button is pressed or not
# if(st.button('Calculate BMI')):

# 	# print the BMI INDEX
# 	st.text("Your BMI Index is {}.".format(bmi))

# 	# give the interpretation of BMI index
# 	if(bmi < 16):
# 		st.error("You are Extremely Underweight")
# 	elif(bmi >= 16 and bmi < 18.5):
# 		st.warning("You are Underweight")
# 	elif(bmi >= 18.5 and bmi < 25):
# 		st.success("Healthy")
# 	elif(bmi >= 25 and bmi < 30):
# 		st.warning("Overweight")
# 	elif(bmi >= 30):
# 		st.error("Extremely Overweight")
