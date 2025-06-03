import streamlit as st
import requests

# Page config
st.set_page_config(page_title="HR Assistant", layout="wide")

# Set custom CSS for background and card styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .reportview-container {
            background-color: #f0f2f6;
        }
        .stApp {
            background-color: #f0f2f6;
        }
        .employee-card {
            background-color: white;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #e0e0e0;
            margin-bottom: 16px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        }
        .employee-card h4 {
            margin-top: 0;
            color: #3b3b3b;
        }
        .available {
            color: green;
            font-weight: bold;
        }
        .unavailable {
            color: red;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 HR Resource Query Chatbot")
st.markdown("Ask something like: _“Looking for a React developer with AWS experience”_")

# Query input
query = st.text_input("💬 **Enter your query**", placeholder="Type your requirement here...")

# Button
if st.button("🔍 Search") and query.strip():
    with st.spinner("🔎 Searching for best matches..."):
        try:
            res = requests.post("http://localhost:8000/chat", json={"query": query})
            res.raise_for_status()
            out = res.json()

            # Show response
            st.markdown("### ✅ Response")
            st.success(out["response"])

            # Show matched employees
            st.markdown("### 👥 Top Matches")
            for emp in out["matches"]:
                st.markdown(
                    f"""
                    <div class="employee-card">
                        <h4>🧑 {emp['name']}</h4>
                        <p>🛠️ <strong>Skills:</strong> {', '.join(emp['skills'])}</p>
                        <p>📅 <strong>Experience:</strong> {emp['experience_years']} years</p>
                        <p>📁 <strong>Projects:</strong> {', '.join(emp['projects'])}</p>
                        <p>📌 <strong>Availability:</strong> 
                            <span class="{ 'available' if emp['availability'] == 'available' else 'unavailable' }">
                                {emp['availability'].capitalize()}
                            </span>
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using LLaMA 3, FAISS, and Streamlit")
