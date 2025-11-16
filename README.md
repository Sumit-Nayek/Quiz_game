# 🎯 Python Quiz Game

A simple and interactive quiz game built with Python, perfect for beginners learning programming fundamentals.

## 📖 Overview

This project contains two versions of a quiz game:
- **Simple Text-Based Version**: Perfect for learning basic Python syntax
- **Streamlit Web Version**: Interactive web-based quiz with beautiful UI

## 🚀 Features

### Text Version
- ✅ Multiple-choice questions
- ✅ Score tracking
- ✅ Instant feedback
- ✅ Play again option
- ✅ Simple text-based interface

### Streamlit Version
- ✅ Beautiful web interface
- ✅ Real-time score updates
- ✅ Progress tracking
- ✅ Timer functionality
- ✅ Category-based questions
- ✅ Performance analytics

## 📁 Project Structure

```
python-quiz-game/
│
├── simple_quiz.py          # Basic text-based version
├── streamlit_quiz.py       # Web version with Streamlit
├── requirements.txt        # Dependencies for Streamlit version
├── README.md              # This file
└── assets/                # Screenshots and demo images
    ├── text-version-demo.png
    └── streamlit-demo.png
```


## 🎮 How to Play

### Simple Text Version
1. Run the script
2. Read each question carefully
3. Type A, B, C, or D to answer
4. Get immediate feedback
5. View your final score at the end
6. Choose to play again or exit

### Streamlit Version
1. Launch the web app
2. Click "Start Quiz"
3. Click on your answer choice
4. See instant correct/incorrect feedback
5. Click "Next Question" to continue
6. View detailed results at the end

## 💻 Code Examples

### Simple Question Structure
```python
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
        "correct": "C"
    }
]
```

### Basic Game Loop
```python
for question_data in questions:
    user_answer = input("Your answer: ")
    if user_answer == question_data["correct"]:
        print("✅ Correct!")
        score += 1
```

## 📚 Learning Objectives

This project helps students learn:
- **Variables and Data Types**
- **Lists and Dictionaries**
- **Functions and Modular Programming**
- **Conditional Statements (if/else)**
- **Loops (for/while)**
- **User Input Handling**
- **Basic Game Development Concepts**

## 🎯 Customization

### Adding New Questions
Edit the `questions` list in either version:

```python
new_question = {
    "question": "Your question here?",
    "options": ["A) Option1", "B) Option2", "C) Option3", "D) Option4"],
    "correct": "A"  # Correct option letter
    "category": "Science"  # For Streamlit version
}
```

### Creating Different Categories
- Science
- Mathematics
- Geography
- History
- Programming

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions
- Add more questions
- Implement different difficulty levels
- Add sound effects
- Create new categories
- Improve the UI/UX
- Add multiplayer functionality

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'streamlit'`
**Solution**: Run `pip install streamlit`

**Issue**: Python not found
**Solution**: Ensure Python is installed and added to PATH

**Issue**: Streamlit app not loading
**Solution**: Check if port 8501 is available, try `streamlit run streamlit_quiz.py --server.port 8502`

## 🎓 Educational Value

This project is perfect for:
- **Classroom teaching** - Programming fundamentals
- **Self-learning** - Python syntax practice
- **Coding clubs** - Group projects and collaborations
- **Homework assignments** - Extend and customize features

## 📊 Future Enhancements

- [ ] Database integration for questions
- [ ] User authentication and score saving
- [ ] Multiplayer mode
- [ ] Mobile app version
- [ ] Voice-based answers
- [ ] Image-based questions
- [ ] Leaderboard system

## 👨‍💻 Author

**Your Name**
- GitHub: [@Sumi-Nayek](https://github.com/Sumit-Nayek)

## 🙏 Acknowledgments

- Python Software Foundation
- Streamlit team for the amazing framework
- Teachers and students who provided feedback

---

<div align="center">

**⭐ Don't forget to star this repository if you found it helpful!**

*Happy Coding! 🐍*

</div>

**Note**: This project is designed for educational purposes. Feel free to modify and expand upon it for your learning journey!