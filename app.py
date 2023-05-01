import openai
import streamlit as st
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')


def latex_to_pdf(latex_expression):
    # Prepare prompt for GPT-3
    prompt = f"Acting as a Latex professional,convert the following expression using the given senerio: If it is LaTeX expression convert to its corresponding PDF representation and vice verse:\n\n{latex_expression}"
    
    # Generate PDF representation using GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15,
    )
    
    # Extract PDF representation from GPT-3 response
    pdf_expression = response.choices[0].text.strip()
    
    return pdf_expression

def main():
    # Set up input and output interfaces
    st.title("ChatGPT-3: Latex to PDF Converter")
    st.markdown("This application compiles latex commands into pdf using ChatGPT-3 API")
    input_text= st.text_area('''Enter Latex commands:''')
    if st.button("Compile"):
        output_text = latex_to_pdf(input_text)
        st.write("Output:")
        st.write(output_text)
  



if __name__ == "__main__":
    main()
    