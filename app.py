import streamlit as st
from PIL import Image
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
img_contact_form = Image.open("images/Image1.png")
# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Rashmi :wave:")
    st.title("A Data Science Intern at Scifor Technologies")
    st.write(
        "I am a passionate Artificial Intelligence, Machine Learning and Data Science learner."
    )
    

# ---- About Me ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write(
            """
            - I am a final year student based in Bangalore, currently pursuing a Bachelor's degree in Artificial Intelligence and Machine Learning. 
            - Throughout my academic journey, I have actively participated in various training programs focused on artificial intelligence, machine learning, and data science. 
            - My skill set includes proficiency in programming languages such as Python, Java, and SQL, with specialized knowledge in AI, ML, data science, NLP, and deep learning. 
            - I have applied my expertise through practical projects.
            """
        )

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Hand-Written Digit Recognition")
        st.write(
            """
            The objective of the Handwritten Digit Recognition Project is to create a robust Convolutional Neural Network (CNN) capable of accurately identifying and classifying handwritten digits. 
            Utilizing the MNIST dataset, the project aims to achieve high accuracy. 
            The focus is on designing a model that can handle diverse writing styles and contribute to advancements in image recognition.

            """
        )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/rashmi.15ar@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

