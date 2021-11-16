<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
      <title>
        Cat_Or_Dog_Prediction
      </title>
  </head>
  <body>
   <section id="main">
     <nav>
      <a href="#" class="logo">
        <img src="dog_pred.jpg">
       </a>
     
      <a href="#" class="hey"><strong>Say hi!</strong></a>
     </nav>
   </section> 

   <div class="content">
     <div class="image">
       <img src="dwayne_jhonson.jpg" alt="Rock">
     </div> 
     <div class="main-text">
       <h1> Hello, I am The <br> Rock</h1>
       <p> Hey in This Video I am Going to show how to build a website using only HTML and CSS</p>
       <a href="#" class="resume-btn">See My Resume</a>
     </div> 
   </div>
  </body>
</html>

import streamlit as st
       st.title("Cat_Or_Dog_Prediction") 
       st.write('This Model Predicts whether it is a Cat Or Dog for image uploaded by user')
       st.image("dog_pred.jpg", width=500)
       st.write('To Open View This App in Streamlit Click The Link Below')
       https://share.streamlit.io/raiyan1437/cat_or_dog_prediction/main/cdmain.py
