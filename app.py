import streamlit as st
import random
import time

# Set page configuration
st.set_page_config(
    page_title="Quiz Game",
    page_icon="❓",
    layout="centered"
)

# Initialize session state variables
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'game_active' not in st.session_state:
    st.session_state.game_active = False

# Quiz questions database
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris",
        "category": "Geography"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars",
        "category": "Science"
    },
    {
        "question": "What is 15 + 27?",
        "options": ["32", "42", "52", "38"],
        "correct_answer": "42",
        "category": "Math"
    },
    {
        "question": "Which programming language is known for its use in data science?",
        "options": ["Java", "Python", "C++", "Ruby"],
        "correct_answer": "Python",
        "category": "Programming"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
        "correct_answer": "Blue Whale",
        "category": "Animals"
    }
]

def start_quiz():
    """Reset and start the quiz"""
    st.session_state.score = 0
    st.session_state.current_question = 0
    st.session_state.answered = False
    st.session_state.start_time = time.time()
    st.session_state.game_active = True

def next_question():
    """Move to the next question"""
    st.session_state.current_question += 1
    st.session_state.answered = False

def check_answer(selected_option, correct_answer):
    """Check if the answer is correct"""
    if not st.session_state.answered:
        st.session_state.answered = True
        if selected_option == correct_answer:
            st.session_state.score += 1
            return True
    return False

def calculate_time_taken():
    """Calculate time taken for the quiz"""
    if st.session_state.start_time:
        return round(time.time() - st.session_state.start_time, 2)
    return 0

def main():
    st.title("🎯 Quiz Game")
    st.markdown("Test your knowledge with this fun quiz!")
    
    # Sidebar for game info
    with st.sidebar:
        st.header("Game Info")
        st.write(f"**Total Questions:** {len(quiz_questions)}")
        st.write(f"**Current Score:** {st.session_state.score}")
        
        if st.session_state.game_active:
            time_taken = calculate_time_taken()
            st.write(f"**Time Elapsed:** {time_taken} seconds")
        
        st.header("Categories")
        categories = set(q['category'] for q in quiz_questions)
        for category in categories:
            st.write(f"• {category}")
    
    # Start game or show quiz
    if not st.session_state.game_active:
        st.subheader("Welcome to the Quiz Game!")
        st.write("""
        **How to play:**
        - Answer all questions to the best of your ability
        - You'll get immediate feedback after each answer
        - Try to get the highest score!
        """)
        
        if st.button("🎮 Start Quiz", type="primary"):
            start_quiz()
            st.rerun()
    
    else:
        # Check if quiz is completed
        if st.session_state.current_question >= len(quiz_questions):
            time_taken = calculate_time_taken()
            
            st.balloons()
            st.success("🎉 Quiz Completed!")
            st.subheader(f"Final Score: {st.session_state.score}/{len(quiz_questions)}")
            st.write(f"⏱️ Time Taken: {time_taken} seconds")
            
            # Calculate percentage
            percentage = (st.session_state.score / len(quiz_questions)) * 100
            st.write(f"📊 Percentage: {percentage:.1f}%")
            
            # Performance message
            if percentage >= 80:
                st.success("🏆 Excellent! You're a quiz master!")
            elif percentage >= 60:
                st.info("👍 Good job! Well done!")
            elif percentage >= 40:
                st.warning("💪 Not bad! Keep practicing!")
            else:
                st.error("📚 Keep learning! You'll do better next time!")
            
            if st.button("🔄 Play Again", type="primary"):
                start_quiz()
                st.rerun()
            
            return
        
        # Display current question
        current_q = quiz_questions[st.session_state.current_question]
        
        st.subheader(f"Question {st.session_state.current_question + 1}/{len(quiz_questions)}")
        st.write(f"**Category:** {current_q['category']}")
        st.write(f"**{current_q['question']}**")
        
        # Display options as buttons
        col1, col2 = st.columns(2)
        
        for i, option in enumerate(current_q['options']):
            if i % 2 == 0:
                with col1:
                    if st.button(option, key=f"option_{i}", use_container_width=True):
                        is_correct = check_answer(option, current_q['correct_answer'])
                        if is_correct:
                            st.success("✅ Correct!")
                        else:
                            st.error(f"❌ Incorrect! The correct answer is: {current_q['correct_answer']}")
            else:
                with col2:
                    if st.button(option, key=f"option_{i}", use_container_width=True):
                        is_correct = check_answer(option, current_q['correct_answer'])
                        if is_correct:
                            st.success("✅ Correct!")
                        else:
                            st.error(f"❌ Incorrect! The correct answer is: {current_q['correct_answer']}")
        
        # Next question button (only after answering)
        if st.session_state.answered:
            if st.button("➡️ Next Question", type="primary"):
                next_question()
                st.rerun()
        
        # Progress bar
        progress = (st.session_state.current_question + 1) / len(quiz_questions)
        st.progress(progress)
        st.write(f"Progress: {st.session_state.current_question + 1}/{len(quiz_questions)}")

if __name__ == "__main__":
    main()