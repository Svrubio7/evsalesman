import streamlit as st

# Set page configuration
st.set_page_config(page_title="Your EV Online", page_icon=":electric_plug:", layout="wide")

def main():
    st.title("Welcome to Your EV Online!")
    st.image("C:/Users/svrub/Documents/IE STUFF/2nd year/2nd semester/PERSONALITY FOR AI/Evsalesman/evsalesman/elements/yeologo.jpg", width=300)

    st.markdown("""
    ## Explore the Future of Driving
    YEO offers top-tier electric vehicles designed for the modern era at the best prices. Experience sustainability, power, and cutting-edge technology with our range of EVs. Whether you're looking for city commuting or adventurous road trips, we've got you covered.
    """)

    # Company Values
    st.header("Why Choose YEO?")
    st.markdown("""
    - **Sustainability:** Our EVs are designed with the planet in mind, ensuring you drive clean.
    - **Affordability:** Start saving with your new EV for the best prices in the whole industry.
    - **Support:** Contact us at any time! Our army of customer support agents will always respond.
    """)

    # Contact Form
    st.header("Get in Touch")
    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            # Here, you can handle the form submission (e.g., sending an email or storing it in a database)
            st.success("Thank you for getting in touch! We'll get back to you soon.")

if __name__ == "__main__":
    main()

