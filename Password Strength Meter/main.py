# 🚀 Password Pro | By Muzna Amir Zubairi
import re
import streamlit as st

st.title("🚀🔒 Password Pro")
st.write("🧠 Test your password strength here!")

def strength_check(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append('⏳ Must be """8+ chars"""')

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append('🔠 Mix """UPPER & lower"""')

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append('🔢 Add """1+ digit"""')

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append('✨ Use """special char (!@#$...)"""')

    if score == 4:
        st.success('✅ Strong! Great job 💪')
    elif score == 3:
        st.info('⚠️ Medium! Almost there 🚀')
    else:
        st.error("❌ Weak! Needs work 💡")

    if feedback:
        with st.expander('🛠 Fix Tips'):
            for item in feedback:
                st.write(item)

password = st.text_input("🔑 Type Password:", type="password", help="Make sure it's strong!")

if st.button("🚨 Check Now"):
    if password:
        strength_check(password)
    else:
        st.warning("✋ First, enter your password.")


st.markdown("---")
st.markdown("Built with ❤️ by Muzna Amir Zubairi")
