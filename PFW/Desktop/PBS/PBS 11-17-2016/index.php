<?php
   include("db/sessions/config.php");
   session_start();
   
   if($_SERVER["REQUEST_METHOD"] == "POST") {
      // tgi and password sent from form 
      
      $mytgi = mysqli_real_escape_string($db,$_POST['tgi']);
      $mypassword = mysqli_real_escape_string($db,$_POST['password']); 
      
      $word = crypt($mypassword, '$1$dgg438');
     
      $sql = "SELECT tgi, type FROM users WHERE tgi = '$mytgi' and password = '$word'";
      
      $result = mysqli_query($db,$sql);
      $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
      $active = $row['active'];
      
      $count = mysqli_num_rows($result);
      
      // If result matched $mytgi and $mypassword, table row must be 1 row
		
      if($count == 1) {
         session_register("mytgi");
         $_SESSION['login_user'] = $mytgi;
         if($row['type'] == "admin"){
         	$_SESSION['privelage'] = "admin";
         	header("location: backend.php");
         	
         }
         else{
         	header("location: home.php");
         }
         
      }else {
         $error = "Your Login Name or Password is invalid";
      }
   }
?>
<html>
   
   <head>
      <title>Login Page</title>
      <link href="stylesheets72.css" rel="stylesheet" type="text/css"/>
      
   </head>
   <?php echo $word; ?>
   <body bgcolor = "#FFFFFF">
   
   	<div class="centers" id="img">
		<img src="thales-logo.jpg" id="logo" width = "100%" height= "100%">
	</div>
	
      <div align = "center" class="test" id="whole">
         <div id="loginform">
            <div id="topheader"><b>Login</b></div>	
            <div id="margins">
               
               <form action = "" method = "post" autocomplete="off">
                  <label>TGI:<br></label><input type = "text" name = "tgi" value="T01" maxlength="8" class = "box" onkeypress='return event.charCode >= 48 && event.charCode <= 57'/><br /><br />
                  <label>Password  :<br></label><input type = "password" name = "password" class = "box" /><br/><br />
                  <input type = "submit" value = " Log In"/><br />
               </form>
               
               <div style = "font-size:11px; color:#cc0000; margin-top:10px"><?php echo $error; ?></div>
					
            </div>
				
         </div>
			
      </div>
     
   </body>
</html>