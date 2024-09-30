import streamlit as st

# Set page configuration for responsive layout
st.set_page_config(page_title="Navratri 2024 - Passes", layout="wide")

# App title and description
st.title("Celebrate Navratri 2024 - Secure Your Passes Now!")
st.subheader("Enjoy exclusive Garba nights at different locations with exciting passes for a magical experience.")

# Displaying Kora Kendra events in a responsive layout
st.markdown("### Events:")
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("✨ **Kora Kendra Season Pass**: ₹1000")
    st.markdown("✨ **Bhoomi Trivedi Night Season Pass**: ₹900")
with col2:
    st.markdown("✨ **Aishwarya Majumdar Night Season Pass**: ₹1900")
    st.markdown("✨ **Falguni Pathak Night Season Pass**: ₹5000")

# Expandable list for Nesco events
with st.expander("Nesco (Click to Expand)"):
    st.markdown("✨ **Season Pass (All Days)**: ₹6000")
    st.markdown("✨ **3rd Oct (Thu)**: ₹1000")
    st.markdown("✨ **4th Oct (Fri)**: ₹1500")
    st.markdown("✨ **5th Oct (Sat)**: ₹2000")
    st.markdown("✨ **6th Oct (Sun)**: ₹1500")
    st.markdown("✨ **7th Oct (Mon)**: ₹950")
    st.markdown("✨ **8th Oct (Tue)**: ₹950")
    st.markdown("✨ **9th Oct (Wed)**: ₹850")
    st.markdown("✨ **10th Oct (Thu)**: ₹1000")
    st.markdown("✨ **11th Oct (Fri)**: ₹1500")
    st.markdown("✨ **Nilesh Thakkar Pass**: ₹6500")

# Error handling for pass selection
try:
    num_passes = st.slider("Select number of passes", 1, 10)
    if num_passes < 1:
        st.error("You must select at least one pass!")
except Exception as e:
    st.error(f"An error occurred: {e}")

# Emotional call to action
st.markdown(f"**Don't miss out on an unforgettable Navratri experience!** Secure your {num_passes} pass(es) now and enjoy nights full of music, dance, and joy!")

# Button to redirect to WhatsApp with error handling
if st.button("Book Your Passes "):
    st.markdown("[Click here to book your passes](https://wa.link/zvksqm)")

# Optimize performance for faster loading (Streamlit caches components)
@st.cache_data
def load_event_data():
    # Simulated event data (e.g., could be pulled from a database or API)
    return {
        "Kora Kendra": {
            "Season Pass": 1000,
            "Bhoomi Trivedi Night": 900,
            "Aishwarya Majumdar Night": 1900,
            "Falguni Pathak Night": 5000,
        },
        "Nesco": {
            "Season Pass (All Days)": 6000,
            "3rd Oct (Thu)": 1000,
            "4th Oct (Fri)": 1500,
            "5th Oct (Sat)": 2000,
            "6th Oct (Sun)": 1500,
            "7th Oct (Mon)": 950,
            "8th Oct (Tue)": 950,
            "9th Oct (Wed)": 850,
            "10th Oct (Thu)": 1000,
            "11th Oct (Fri)": 1500,
            "Nilesh Thakkar Pass": 6500,
        },
    }

# Load event data (caching for performance)
event_data = load_event_data()

