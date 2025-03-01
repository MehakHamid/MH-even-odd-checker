import streamlit as st

# Set Streamlit Page Configuration
st.set_page_config(page_title="Even or Odd Checker", page_icon="🔢", layout="centered")

# Custom Styling with a Vibrant Theme
st.markdown(
    """
    <style>
        /* Gradient Background */
        .stApp {
            background: #FCB9B2;
            padding: 20px;
        }
        
        /* Main Title Styling */
        .title {
            color: white;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        
        /* Input Box */
        .stTextInput > div > div > input {
            border-radius: 10px;
            border: 2px solid #ff6f61;
            padding: 10px;
            font-size: 18px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }

        /* Result Message */
        .result-box {
            background: #ffffff;
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2);
            margin-top: 10px;
            color: #333;
        }

        /* History Section */
        .history-box {
            background: rgba(255, 255, 255, 0.8);
            padding: 15px;
            border-radius: 12px;
            margin-top: 15px;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2);
        }

        .history-title {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            color: #1A5276;
            margin-bottom: 10px;
        }

        /* Buttons */
        .btn-check, .btn-clear {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            font-weight: bold;
            color: #B23A48;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            text-align: center;
            margin-top: 10px;
            transition: 0.3s ease-in-out;
        }

        .btn-check {
            background: linear-gradient(90deg, #ff6f61, #ff3d3d);
        }
        .btn-check:hover {
            background: linear-gradient(90deg, #ff3d3d, #ff1e1e);
        }

        .btn-clear {
            background: linear-gradient(90deg, #3b5998, #1a2a6c);
        }
        .btn-clear:hover {
            background: linear-gradient(90deg, #1a2a6c, #000);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<p class="title">🎯 Even or Odd Checker 🔢</p>', unsafe_allow_html=True)

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# User Input
number = st.text_input("Enter a number:", placeholder="Type a number and press Enter...", key="user_input")

# Check Even or Odd
if number:
    try:
        num = int(number)
        result_text = f"✅ {num} is an Even number." if num % 2 == 0 else f"⚠️ {num} is an Odd number."

        st.markdown(f'<div class="result-box">{result_text}</div>', unsafe_allow_html=True)

        # Save to history
        st.session_state.history.append(f"🔢 {num} ➝ {'Even' if num % 2 == 0 else 'Odd'}")

    except ValueError:
        st.error("❌ Invalid input! Please enter a valid number.")

# Display History
if st.session_state.history:
    st.markdown('<p class="history-title">📜 History</p>', unsafe_allow_html=True)
    st.markdown('<div class="history-box">', unsafe_allow_html=True)
    
    for item in reversed(st.session_state.history):  # Show recent first
        st.write(item)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Buttons Section
col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 Check Another Number", key="check_another"):
        st.rerun()

with col2:
    if st.button("🗑️ Clear History", key="clear_history"):
        st.session_state.history = []  # Clear history
        st.rerun()
