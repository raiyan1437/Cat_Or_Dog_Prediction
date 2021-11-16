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
* {
  box-sizing: border_box; 
}

body {
  margin: 0px;
  padding: 0px;
  font: poppins;
}

#main {
  width: 100%;
  height: 50vh;
  position: relative;
}

nav {
 display: flex;
 justify-content: space-around;
 align-items: center;
 position: fixed;
 top: 0;
 left: 0;
 width: 100%;
 background-color: white;
 box-shadow: 5px 10px 30px rgba(0, 0, 0, 0.02);
 z-index: 1;
}

.logo img{
  height: 45px;
}

.menu{
  list-style: none;
  display: flex; 
} 

.menu li a{
  height: 40px;
  line-height: 43px;
  margin: 3px;
  padding: 0px 22px;
  display: flex;
  font-size: 0.8em;
  text-transform: uppercase;
  font-weight: 500;
  letter-spacing: 1px;
  color: gray;
}

a {
 text-decoration: none;
}

.hey{
  color: #39bfbd;
  font-weight: 500;
  font-size: 0.9em;
  border-bottom: 2px solid #39bfbd;
} 

.image {
  width: 500px;
  height: 500px; 
}

.image img{
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.content{
  display: flex;
  width: 90%;
  justify-content: space-around;
  align-items: center;
  position: absolute;
  left: 50%;
  right: 50%;
  transform: translate(-50%, -50%)
}

.main-text{
  width: 500px;
}

.main-text h1{
  font-size: 3.5em;
  color: #1c3548;
  margin: 0px, 0px, 10px, 0px;
  line-height: 60px;
}

.main-text p{
  color: gray;

}

.resume-btn {
  width: 190px; 
  height: 44px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  background-color: #1db096;
  border-radius: 20px;
  box-shadow: 5px, 10px, 30px, rgba(123, 153, 148, 0.2); 
}

.resume-btn:hover{
  background-color: #23cdaf;
  transition: all ease 0.2s;
}

.menu li a:hover{
  background-color:#23cdaf ;
  color: white;
  box-shadow: 5px, 10px, 30px, rgba(123, 153, 148, 0.2);
  transition: all ease 0.2s;
}
import streamlit as st
       st.title("Cat_Or_Dog_Prediction") 
       st.write('This Model Predicts whether it is a Cat Or Dog for image uploaded by user')
       st.image("dog_pred.jpg", width=500)
       st.write('To Open View This App in Streamlit Click The Link Below')
       https://share.streamlit.io/raiyan1437/cat_or_dog_prediction/main/cdmain.py
