import streamlit as st
st.set_page_config(page_title='MY  STREAMLIT APPLICATION',page_icon='shark')
mymenu=st.sidebar.selectbox('my menu',('home','form','downloads'))
st.title('python developer')
st.header('by prajyot kinare')
st.text('this is text of stramlit library')
if(mymenu=='home'):
    st.markdown('<center><h1>WELCOME TO ONLEI TECHNOLOGIES</h1></center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=szCAjwTcizE')
elif(mymenu=='form'):
    with st.form('my form'):
        name=st.text_input('enter name')
        dob=st.date_input("choose date of birth")
        marks=st.slider('choose marks')
        k=st.form_submit_button("submit form")
        if(k):
            st.write('name',name,'DOB',dob,'marks',marks)
elif(mymenu=='downloads'):
    st.header("Downloads")
    st.download_button('Download Now','hello this is downloaded data','onlei.txt')
            
