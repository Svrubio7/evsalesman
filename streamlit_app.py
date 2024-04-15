import streamlit as st
import openai
import os

# Use the "light" theme as a base and customize from there
st.set_page_config(page_title="Your EV Online", page_icon=":electric_plug:", layout="wide")


"""OPENAI INTEGRATION"""
# Setting the API key
openai.api_key = os.environ['OPENAI_API_KEY']

system_message = "You are an Electric Vehicle salesman. The cars you are selling are included in the JSON file you have access to and you are only selling those as they are the ones in our company. Your personality traits consist of the following: high extraversion, high agreeableness and low neuroticism. \
From the client you are talking to, you will need to detect 2 personality traits: agreeableness and openness to experience. You must also be able to detect 3 emotions: fear, happiness and frustration.\
You must also be able to react in a certain way to the clients emotions and personality traits. You must react in the following way:\
Low agreeableness- Be professional and serious.\
High agreeableness- Throw in some jokes anda happy tone.\
High openness to experience - Be more relaxed and let the person ask you more questions without revealing every detail.\
Low openness to experience- Have a reassuring character and repeat the qualities of the car comparing it in a positive way to the rest of the market.\
If you detect fear, repeat the best qualities of the car comparing them in a positive way to the rest of the car market.\
If you detect happiness, it is the right moment to close the sale. Only do this if you have spoken a bit before about the car. If you detect happiness from the beginning, do not try to close the sale right away.\
If you detect frustration, mention how the price compares in terms of being cheaper to the rest of the car market. Also it might be a good moment to offer another car as they might not be happy with the one you offered."

messages = [{"role": "assistant", "content": system_message}]


def display_chat_history(messages):
    for message in messages:
        print(f"{message['role'].capitalize()}: {message['content']}")


def get_response_from_bot(message):
    if len(message) < 2 or message.isnumeric():
        return "Please send a valid message"

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": message}
        ]
    )

    print(completion.choices[0].message)
    return completion.choices[0].message


get_response_from_bot("HOW ARE YOU TODAY?")


def main():
    # centering the title
    st.markdown("<h1 style='text-align: center; color: black;'>Welcome to Your EV Online!</h1>", unsafe_allow_html=True)
    # adding spacing
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
        # centering the header
        st.markdown("<h2 style='text-align: center; color: black;'>Why Choose YEO?</h2>", unsafe_allow_html=True)
        # adding spacing
        st.markdown("<h3 style='text-align: center; color: black;'> </h3>", unsafe_allow_html=True)
        left, middle, right = st.columns(3)
        with left:
            st.markdown("<h3 style='text-align: center; color: black;'>Sustainability</h3>", unsafe_allow_html=True)
            st.markdown(
                "<h4 style='text-align: center; color: black;'>Our EVs are designed with the planet in mind, ensuring you drive clean.</h4>",
                unsafe_allow_html=True)

        with right:
            st.markdown("<h3 style='text-align: center; color: black;'>Affordability</h3>", unsafe_allow_html=True)
            st.markdown(
                "<h4 style='text-align: center; color: black;'>Start saving with your new EV for the best prices in the whole industry.</h4>",
                unsafe_allow_html=True)

        with middle:
            st.markdown("<h3 style='text-align: center; color: black;'>Support</h3>", unsafe_allow_html=True)
            st.markdown(
                "<h4 style='text-align: center; color: black;'>Contact us at any time! Our army of customer support agents will always respond.</h4>",
                unsafe_allow_html=True)

    st.markdown("---")  # I IMPLEMENTED THE CHATBOT HERE

    with st.container():
        while True:
            # Display chat history
            display_chat_history(messages)
        
            # Get user input
            prompt = input("User: ")
            messages.append({"role": "user", "content": prompt})
        
            # Get assistant response
            response = get_assistant_response(messages)
            messages.append({"role": "assistant", "content": response})


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
