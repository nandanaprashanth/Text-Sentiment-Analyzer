import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np

# Streamlit App
st.title("📝 Text Sentiment Analyzer")
st.write("Analyze the sentiment of any text you input and visualize the results with graph.")

# User input
text = st.text_area("Enter text here:")

if st.button("Analyze Sentiment"):
    if text.strip():
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        # Determine sentiment
        if sentiment > 0:
            st.success("The sentiment is Positive 😊")
        elif sentiment < 0:
            st.error("The sentiment is Negative 😞")
        else:
            st.info("The sentiment is Neutral 😐")

        # Display detailed polarity and subjectivity
        st.write(f"**Polarity:** {sentiment:.2f}")
        st.write(f"**Subjectivity:** {blob.sentiment.subjectivity:.2f}")

        st.write("### Sentiment Polarity Visualization")
        x = np.linspace(0, 10, 500)  # Simulated time points
        y = np.cos(2 * np.pi * x) * sentiment  
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(x, y, color="#4CAF50", linewidth=2, label="Sentiment Polarity") 
        ax.fill_between(x, y, color="#4CAF50", alpha=0.3)  # Add shading
        ax.axhline(0, color="black", linestyle="--", linewidth=1, alpha=0.8)  # Dashed baseline
        ax.set_title("Sentiment Polarity Graph", fontsize=16, color="#333333")
        ax.set_xlabel("Time (simulated)", fontsize=12, color="#333333")
        ax.set_ylabel("Sentiment Polarity", fontsize=12, color="#333333")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.legend(loc="upper right", frameon=False)
        ax.grid(alpha=0.4)

        # Display the graph
        st.pyplot(fig)
    else:
        st.warning("Please enter some text to analyze!")
