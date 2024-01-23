import streamlit as st
from main import get_pdf_text,get_chunks,get_vector_db,get_conversation_chain

def get_response(querry):
    response=st.session_state.conversation(querry)
    return(response["result"])


def main():


    if "conversation" not in st.session_state:
        st.session_state.conversation= None

    st.header("Ask your PDF 📜💬")
    
    ## for input text and LLM response message thread:
    querry=st.chat_input("Type your question here")
    if querry:
        with st.chat_message("AI"):
            st.write(get_response(querry))
            
    
    with st.sidebar:
        st.subheader("Drop your pdfs here:")
        
        pdf_file=st.file_uploader("Upload files here")
        if st.button("Upload"):         ## Button logic
            with st.spinner('In progress'):
        
            # Get raw text
                pdf_text= get_pdf_text(pdf_file)
                st.write("Source document compiled ✅")      
            
            # Get txt chunks 
                text_chunks=get_chunks(pdf_text)
                st.write("Chunks Generated ✅")    
            # Vector database
                vector_db= get_vector_db(text_chunks)
                st.write("Establised Vector Database ✅")  
            # # Conversation Chain
                st.session_state.conversation= get_conversation_chain(vector_db)
                st.write("LLM Chain Established ✅")
    
if __name__=="__main__":
    main()