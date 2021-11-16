<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
      <title>The Rock Resume</title>
    <link href="style.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
   <section id="main">
     <nav>
      <a href="#" class="logo">
        <img src="build_logo.png" alt="the logo of project The Rock">
      </a>

      <span class="menu-space"></span>
      
      <ul class="menu">
        <li><a href="#">Home</a></li>
        <li><a href="#">Skill</a></li>
        <li><a href="#">Recent</a></li>
        <li><a href="#">Client</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
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
