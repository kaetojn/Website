<?php
include('adminsession.php');
include('config.php');
    
$test = $_POST["data"];
$obj = json_decode($test, true);
$data = $obj["myarray"];


$check = mysqli_query($connection,"SELECT * FROM `info` WHERE `key`='".$data["key"]."'");

if(mysqli_num_rows($check)==1){
	$sql2 = "UPDATE `info` SET `status`='".$data["status"]."', `assigned`='".$data["assigned"]."', `due`='".$data["due"]."', `priority`='".$data["priority"]."' WHERE `key`='".$data["key"]."'";
        $update = mysqli_query($connection, $sql2) or die("Error in Selecting " . mysqli_error($connection));

}
else{
	$sql = "INSERT INTO info(`key`,status,assigned,due,priority) VALUES('".$data['key']."', '".$data['status']."', '".$data['assigned']."', '".$data['due']."', '".$data['priority']."')";
	$result = mysqli_query($connection, $sql);
}



mysqli_close($connection);

?> 