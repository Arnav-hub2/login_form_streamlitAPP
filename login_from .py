import streamlit as st 
#header
st.header("Student Records Management")
#TITLE
st.title(" Welcome to student Management System")
#SUBHEADER
st.subheader(" Manage student record efficiently and effectively")
#TEXT
st.text("HELLO DATABASE")
# MARKDOWN
st.markdown("---------------")
st.markdown("**ARNAV**")
st.markdown("*ARNAV**")
st.markdown("<h3 style=color:red>Arnav Misra </h3>",unsafe_allow_html=True)
#WRITE
st.write("Hello Arnav")
#CAPTION
st.caption(" THIS is the caption")
#CODE
st.code("""
        def add(a,b):
        return a + b""", language = "python")
st.latex(r'''
         a^2 + b^2 = c^2 
         ''')
#DIVIDER
st.divider()  
if st.button("CLICK ME"):
    st.write("BUTTON CLICKED")
    st.success(" THIS IS SUCCESS MESSAGE")
    st.snow()
else:
    st.write("BUTTON NOT CLICKED")
    st.error(" THIS IS ERROR MESSAGE")
name = st.text_input(" Enter your name")
st.write(f"Hello, {name}")
if name == "":
        st.warning(" Name cannot be empty")
elif not name.isalpha():
     st.warning(" Name must contain only letters")
else:
        st.success(f" Welcome, {name}!")
age = st.number_input(f"Enter your age",min_value=0,max_value=120,step=1)
st.write(f"You are {age} years old")
# CHECKBOX
st.divider()
if st.checkbox("I agree to the terms and conditions"):
        st.write("Thank you for agreeing to the terms and conditions.")
# RADIO BUTTON
st.divider()
gender = st.radio("Select your gender",("Male","Female",  "Other"))
st.write(f"You selected: {gender}")
# SELECTBOX METHOD TO CREATE A DROPDOWN
st.divider()
course = st.selectbox("Select your course",("Math","Science","History","Art"))
st.write(f"You selected: {course}")
skills = st.multiselect(" Select your skills",("Python","Java","C++","JavaScript"))
st.write(f"You selected: {', '.join(skills)}")
# SLIDER METHOD TO CREATE A SLIDER
st.divider()
rating = st.slider("Rate our service", 1, 10, 5)
st.write(f"You rated us: {rating}")
#FILE UPLOAD
st.divider()
upload_file = st.file_uploader("Upload your profile picture", type=["jpg","png","jpeg"])
if upload_file is not None:
        st.success("File uploaded successfully")
        st.image(upload_file, caption="Profile Picture", use_column_width=True)
address = st.text_area("Enter your address")
st.write(f"Your address is: {address}")
st.divider()
#FORM METHOD TO CREATE A FORM
with st.form("my_form"):
      name = st.text_input("Enter your name")
      age = st.number_input(" Enter your age",min_value=0,max_value=120,step=1)
      submit = st.form_submit_button("Submit")
if submit:
      st.write(f"Name {name}, Age is {age}")
      st.write("form submitted successfully")
st.divider()
#LOGIN FORM USING FORM METHOD
with st.form("login_form"):
      user = st.text_input(" Enter your username")
      password = st.text_input(" Enter your password", type="password")
      login = st.form_submit_button("Login")
if login:
      st.write(f"Username: {user}")
      st.write("Login successful")
#columns method to create multiple columns
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
      st.subheader("First Column ")
      st.text("This is column 1")
with col2:
      st.subheader("Second Column")
      st.text("This is column 2")
with col3:
      st.header("Third Column")
      st.text("This is column 3")
st.divider()
container = st.container()
container.write("Help me i am under the water ")
container.button("Save me")
st.divider()
#USING TABLE METHOD TO DISPLAY DATA IN TABULAR FORMAT
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)
st.divider()
#SIDEBAR METHOD TO CREATE A SIDEBAR
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")
st.divider()
@st.cache_data
def load_data():
      return[1,2,3,4]
data = load_data()
st.write(data)
