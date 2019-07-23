<?php
   include('config.php');
   session_start();
   
   if(!isset($_SESSION['privelage'])){
      header("location: privilege.php");
   }
?>