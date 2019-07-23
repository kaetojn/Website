<?php
include('adminsession.php');
include('config.php');

$test = $_POST["data"];
$obj = json_decode($test, true);
$data = $obj["myarray"];

$check = mysqli_query($connection,"SELECT * FROM `users` WHERE `tgi`='".$data["tgi"]."'");


if(mysqli_num_rows($check)==0){
        
        $sql= "INSERT INTO users (tgi, password, firstname, lastname, type) VALUES('".$data['tgi']."','".crypt($data['password'], '$1$dgg438')."','".$data['firstname']."', '".$data['lastname']."', '".$data['type']."')";
	$result = mysqli_query($connection, $sql)or die("Error in Selecting " . mysqli_error($connection));

}
    
mysqli_close($connection);
?> 