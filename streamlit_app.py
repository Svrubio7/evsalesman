import streamlit as st

# Use the "light" theme as a base and customize from there
st.set_page_config(page_title="Your EV Online", page_icon=":electric_plug:", layout="wide")

def main():
    
    #centering the title
    st.markdown("<h1 style='text-align: center; color: black;'>Welcome to Your EV Online!</h1>", unsafe_allow_html=True)
    #adding spacing
    st.markdown("<h3 style='text-align: center; color: black;'> </h3>", unsafe_allow_html=True)
    # Container for company logo and introduction
    with st.container():
        l1, left_col, mid, right_col, r1 = st.columns(5)
        with left_col:
            st.image("elements/yeologo.jpg", width=300)
        with mid:
            st.empty()
        with right_col:
            st.markdown("""
            ## Explore the Future of Driving
            YEO offers top-tier electric vehicles designed for the modern era at the best prices. Experience sustainability, power, and cutting-edge technology with our range of EVs. Whether you're looking for city commuting or adventurous road trips, we've got you covered.
            """)


    st.markdown("---")  # Horizontal line to visually separate sections

    # Section for company values
    with st.container():
        #centering the header
        st.markdown("<h2 style='text-align: center; color: black;'>Why Choose YEO?</h2>", unsafe_allow_html=True)
        #adding spacing
        st.markdown("<h3 style='text-align: center; color: black;'> </h3>", unsafe_allow_html=True)
        left, middle, right = st.columns(3) 
        with left:
            st.markdown("<h3 style='text-align: center; color: black;'>Sustainability</h3>", unsafe_allow_html=True)
            st.markdown("<h4 style='text-align: center; color: black;'>Our EVs are designed with the planet in mind, ensuring you drive clean.</h4>", unsafe_allow_html=True)
        
        with right:
            st.markdown("<h3 style='text-align: center; color: black;'>Affordability</h3>", unsafe_allow_html=True)
            st.markdown("<h4 style='text-align: center; color: black;'>Start saving with your new EV for the best prices in the whole industry.</h4>", unsafe_allow_html=True)

        with middle:
            st.markdown("<h3 style='text-align: center; color: black;'>Support</h3>", unsafe_allow_html=True)
            st.markdown("<h4 style='text-align: center; color: black;'>Contact us at any time! Our army of customer support agents will always respond.</h4>", unsafe_allow_html=True)

            
        
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
