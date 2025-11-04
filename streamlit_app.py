import streamlit as st

# 1. Define the quiz data structure
# This list holds all the questions, options, and correct answers
questions_data = [
    {
        "question": "In the following code, what is `username`?\n\n```python\ndef create_user(username, age):\n  # code to create user\n  pass\n```",
        "options": [
            {"text": "An actual argument", "rationale": "Actual arguments are the values passed during a function call, not the placeholders in the definition.", "isCorrect": False},
            {"text": "A formal argument (parameter)", "rationale": "`username` is a variable name listed in the function's definition, acting as a placeholder for a value.", "isCorrect": True},
            {"text": "A named argument", "rationale": "Named arguments are part of a function call, where the parameter name is explicitly used.", "isCorrect": False},
            {"text": "A function call", "rationale": "This is part of the function definition, not the line of code that executes the function.", "isCorrect": False}
        ]
    },
    {
        "question": "In the following code, what is `'b_wayne'`?\n\n```python\ndef create_user(username, age):\n  # code...\n\ncreate_user('b_wayne', 42)\n```",
        "options": [
            {"text": "An actual argument", "rationale": "`'b_wayne'` is the real value being passed into the function when it is called.", "isCorrect": True},
            {"text": "A formal argument (parameter)", "rationale": "Formal arguments are the placeholders (`username`, `age`) in the function definition, not the values passed in.", "isCorrect": False},
            {"text": "A default value", "rationale": "A default value would be specified in the function definition, like `age=30`.", "isCorrect": False},
            {"text": "A data type", "rationale": "`'b_wayne'` is a string value, but its role in this context is as an argument.", "isCorrect": False}
        ]
    },
    {
        "question": "What is the primary benefit of using named arguments?",
        "options": [
            {"text": "They make the function run faster.", "rationale": "How arguments are passed does not typically impact the execution speed of the function's logic.", "isCorrect": False},
            {"text": "They allow you to pass arguments in any order.", "rationale": "By explicitly naming the parameter, the position no longer matters, which improves code readability.", "isCorrect": True},
            {"text": "They use less memory.", "rationale": "The memory used is for the values themselves, not for the method of passing them.", "isCorrect": False},
            {"text": "They are the only way to pass numbers.", "rationale": "Numbers can be passed as both positional and named arguments.", "isCorrect": False}
        ]
    },
    {
        "question": "Given this function:\n\n```python\ndef set_config(volume, brightness, contrast=0.5):\n  # code...\n```\n\nWhich of the following function calls is **invalid**?",
        "options": [
            {"text": "`set_config(7, 0.8)`", "rationale": "This is a valid call using two positional arguments, mapping to `volume` and `brightness`.", "isCorrect": False},
            {"text": "`set_config(brightness=0.9, volume=10)`", "rationale": "This is a valid call using only named arguments, and their order does not matter.", "isCorrect": False},
            {"text": "`set_config(volume=5, 0.6)`", "rationale": "This is a syntax error. Positional arguments (like `0.6`) cannot come after named arguments (like `volume=5`).", "isCorrect": True},
            {"text": "`set_config(7, contrast=0.9, brightness=0.8)`", "rationale": "This is a valid call, mixing positional and named arguments. The positional `7` maps to `volume`, and the rest are named.", "isCorrect": False}
        ]
    },
    {
        "question": "In this call, what is `speed=50`?\n\n```python\nmove_player(x=10, y=30, speed=50)\n```",
        "options": [
            {"text": "A formal argument", "rationale": "This is part of the function *call*, not the function *definition*.", "isCorrect": False},
            {"text": "A positional argument", "rationale": "A positional argument would not explicitly state the parameter's name (`speed=`).", "isCorrect": False},
            {"text": "A named argument", "rationale": "The value `50` is explicitly assigned to the parameter named `speed`.", "isCorrect": True},
            {"text": "A syntax error", "rationale": "Assuming `move_player` is defined to accept these parameters, this syntax is perfectly valid.", "isCorrect": False}
        ]
    },
        {
        "question": "The terms 'formal argument' and 'parameter' are...",
        "options": [
            {"text": "Often used interchangeably.", "rationale": "Both terms refer to the variable placeholder in the function's definition.", "isCorrect": True},
            {"text": "Complete opposites.", "rationale": "They refer to the same concept, not opposite ones.", "isCorrect": False},
            {"text": "Related, but 'parameter' is the value and 'formal argument' is the placeholder.", "rationale": "Both terms refer to the placeholder; the value passed in is the 'actual argument'.", "isCorrect": False},
            {"text": "An old term and a new term for different things.", "rationale": "They are largely synonymous, with 'parameter' being the more common modern term.", "isCorrect": False}
        ]
    },
    {
        "question": "The terms 'actual argument' and 'argument' are...",
        "options": [
            {"text": "Complete opposites.", "rationale": "They refer to the same concept, not opposite ones.", "isCorrect": False},
            {"text": "Often used interchangeably.", "rationale": "Both terms refer to the real value or expression passed to a function when it is called.", "isCorrect": True},
            {"text": "Related, but 'argument' is the placeholder and 'actual argument' is the value.", "rationale": "Both terms refer to the value being passed in; the placeholder is the 'parameter' or 'formal argument'.", "isCorrect": False},
            {"text": "Only used in different programming languages.", "rationale": "Both terms are widely understood in the context of function calls across many languages.", "isCorrect": False}
        ]
    },
    {
        #"question": "Given this function:\n\n```python\ndef print_banner(text, border=\"-\"):\n  # code...\n```\n\nHow would you call this function to print \"Hello\" with a \"*\" border?",
        #"options": [
         #   {"text": "`print_banner(\"Hello\", \"*\")`", "rationale": "This positional call correctly passes \"Hello\" for `text` and \"*\" for `border`, overriding the default.", "isCorrect": True},
         #   {"text": "`print_banner(text=\"Hello\")`", "rationale": "This call only provides the `text` argument, so the `border` argument would use its default value of \"-\".", "isCorrect": False},
          #  {"text": "`print_banner(\"*\")`", "rationale": "This positional call would assign \"*\" to the first parameter, `text`, which is not what is intended and would be missing the required `text` argument.", "isCorrect": False},
          #  {"text": "`print_banner(border=\"*\", \"Hello\")`", "rationale": "This is a syntax error. A positional argument (\"Hello\") cannot follow a named argument (`border=\"*\"`).", "isCorrect": False}
        ]
    },
    {
        "question": "What is another common name for 'Named Arguments'?",
        "options": [
            {"text": "Keyword Arguments", "rationale": "This term is used, especially in Python, because you use the parameter name (the 'keyword') in the function call.", "isCorrect": True},
            {"text": "Formal Arguments", "rationale": "Formal arguments (or parameters) are the placeholders in the function definition.", "isCorrect": False},
            {"text": "Positional Arguments", "rationale": "Positional arguments are the opposite; their meaning is determined by their order, not their name.", "isCorrect": False},
            {"text": "Default Arguments", "rationale": "A default argument is a value given in the function definition, not a way of calling the function.", "isCorrect": False}
        ]
    },
    {
        "question": "Consider this function call:\n\n```python\ncalculate_interest(1000, rate=0.05, time=2)\n```\n\nHow is the value `1000` being passed?",
        "options": [
            {"text": "As a named argument", "rationale": "A named argument would look like `principal=1000`.", "isCorrect": False},
            {"text": "As a positional argument", "rationale": "The value `1000` is passed without a name, so its position (first) determines which parameter it maps to.", "isCorrect": True},
            {"text": "As a formal argument", "rationale": "Formal arguments are part of the function definition, not the call.", "isCorrect": False},
            {"text": "As a default value", "rationale": "A default value is defined in the `def` line, not passed in the call.", "isCorrect": False}
        ]
    }
]

# --- App Layout ---

st.title("🐍 Python: Arguments & Parameters Quiz")
st.markdown("Test your knowledge! Select one answer for each question and click 'Submit' at the bottom.")

# We will store the user's answers in a list
user_answers = []

# Use a form to group all questions. This way, the app only reruns
# when the user clicks the "Submit" button, not every radio button.
with st.form("quiz_form"):
    
    # Loop through each question dictionary
    for i, q in enumerate(questions_data):
        st.markdown(f"--- \n **Question {i+1}:** {q['question']}")
        
        # Get just the text of the options
        option_texts = [opt['text'] for opt in q['options']]
        
        # Create the radio button. The `key` is crucial for Streamlit
        # to identify each widget uniquely within the form.
        answer = st.radio(
            label="Your answer:",
            options=option_texts,
            key=f"q{i}"
        )
        user_answers.append(answer) # Store the selected text

    # The submit button for the form
    submitted = st.form_submit_button("Submit Quiz")


# --- Grading Logic ---

# This code block only runs AFTER the user has clicked "Submit"
if submitted:
    st.header("✨ Your Results")
    
    score = 0
    total_questions = len(questions_data)
    
    # Loop through the questions and the user's answers simultaneously
    for i, (q, user_answer_text) in enumerate(zip(questions_data, user_answers)):
        
        # Find the dictionary for the option the user selected
        selected_option_data = next(opt for opt in q['options'] if opt['text'] == user_answer_text)
        
        # Find the dictionary for the correct option
        correct_option_data = next(opt for opt in q['options'] if opt['isCorrect'])

        # Display the question again
        st.markdown(f"--- \n **Question {i+1}:** {q['question']}")
        
        if selected_option_data['isCorrect']:
            score += 1
            st.success(f"Your answer: {user_answer_text} (Correct!)")
            st.info(f"Rationale: {selected_option_data['rationale']}")
        else:
            st.error(f"Your answer: {user_answer_text} (Incorrect)")
            st.success(f"Correct answer: {correct_option_data['text']}")
            st.info(f"Rationale: {correct_option_data['rationale']}")

    # --- Final Score Display ---
    st.header(f"🏁 Your Final Score: {score} / {total_questions}")
    
    if score == total_questions:
        st.balloons()
        st.success("Perfect score! You're an expert!")
    elif score >= total_questions * 0.7:
        st.success("Great job! You have a solid understanding of these concepts.")
    else:
        st.warning("Good effort! You might want to review the concepts and try again.")
