import streamlit as st

# Use the "light" theme as a base and customize from there
st.set_page_config(page_title="Your EV Online", page_icon=":electric_plug:", layout="wide")

def main():
    st.title("Welcome to Your EV Online!")

    # Container for company logo and introduction
    with st.container():
        left_col, right_col = st.columns((1, 2))
        with left_col:
            st.image("elements/yeologo.jpg", width=300)
        with right_col:
            st.markdown("""
            ## Explore the Future of Driving
            YEO offers top-tier electric vehicles designed for the modern era at the best prices. Experience sustainability, power, and cutting-edge technology with our range of EVs. Whether you're looking for city commuting or adventurous road trips, we've got you covered.
            """)

    st.markdown("---")  # Horizontal line to visually separate sections

    # Section for company values
    with st.container():
        st.header("Why Choose YEO?")
        st.markdown("""
        **Sustainability:** Our EVs are designed with the planet in mind, ensuring you drive clean.
        **Affordability:** Start saving with your new EV for the best prices in the whole industry.
        **Support:** Contact us at any time! Our army of customer support agents will always respond.
        """, unsafe_allow_html=True)

    st.markdown("---")  # Horizontal line

    # Contact form
    with st.container():
        st.header("Get in Touch")
        with st.form(key='contact_form'):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                # Form submission logic goes here
                st.success("Thank you for getting in touch! We'll get back to you soon.")

if __name__ == "__main__":
    main()
