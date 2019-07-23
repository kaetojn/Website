<?php
include('sessions/adminsession.php');
include('config.php');

$test = $_POST["data"];
$obj = json_decode($test, true);
$data = $obj["myarray"];

$ids_array4 = array();
$ids_array3 = array();
$ids_array2 = array();
$ids_array1 = array();
$finals = array();

/*
foreach($data as $va2l){
   
}
*/

foreach ($data['id'] as $va2l){
	
        $finals = array_push($ids_array1, $va2l);
        var_dump($finals);
        ob_flush();
        flush();
}
    
//$finals = array("1","2");

$sq2l = "select id from pbs";
$resultser = mysqli_query($connection, $sq2l) or die("Error in Selecting " . mysqli_error($connection));
$emparraye = array();
mysqli_query($connection, "DELETE FROM pbs WHERE id NOT IN ('".join("','", $finals)."')");
//$delete = "DELETE FROM `pbs` WHERE id NOT IN (".implode(',',$deletes).");";
//mysqli_query($connection, $delete);
/*
    $sql = "select id from pbs";
    
    $results = mysqli_query($connection, $sql) or die("Error in Selecting " . mysqli_error($connection));
    $emparray = array();
    

    while($row =mysqli_fetch_assoc($results))
    {
        $emparray[] = $row;
    }
    
    while($row1 =mysqli_fetch_assoc($resultser))
    {
        $emparraye[] = $row1;
    }
    
    $final = json_encode($emparray);
    $final2 = json_encode($emparraye);
    echo $finals;
    var_dump($finals);
    echo "<html><p><pre><span class='inner-pre' style='font-size: 25px'> echo $finals; </></p><br><p><pre><span class='inner-pre' style='font-size: 25px'>$final2</></p></html>";
*/
foreach($data as $val){
/*
   $ids_array3[] = $val["id"];
   array_push($ids_array1, $val["id"]);
   $ids_array2 = implode(",", $ids_array3);
   $ids_array4 = implode(",", $ids_array1);
   
   
   mysqli_query($connection, "DELETE FROM pbs WHERE id NOT IN ($ids_array4)");
   
   //*/
   $check = mysqli_query($connection,"SELECT * FROM `pbs` WHERE `id`='".$val["id"]."'");
   
    if(mysqli_num_rows($check)==1){
        //Update the row
        $sql2 = "UPDATE `pbs` SET `parent`='".$val["parent"]."', `text`='".$val["text"]."' WHERE `id`='".$val["id"]."'";
        $update = mysqli_query($connection, $sql2) or die("Error in Selecting " . mysqli_error($connection));
    }
    else
    {
         $sql = "INSERT INTO pbs(id,parent,text) VALUES('".$val['id']."', '".$val['parent']."', '".$val['text']."')";
    	 $result = mysqli_query($connection, $sql) or die("Error in Selecting " . mysqli_error($connection));
    }
}


mysqli_close($connection);

?> 