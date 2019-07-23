<?php
include('adminsession.php');
$connection = mysqli_connect("www.cooeeuas.com","cooeeuas_npeppas","Npep8338AL","cooeeuas_actiontracker") or die("Error " . mysqli_error($connection));

$sql2 = "select firstname, lastname, type from users";
$result2 = mysqli_query($connection, $sql2) or die("Error in Selecting " . mysqli_error($connection));
$emparray = array();
    

while($row =mysqli_fetch_assoc($result2)){
        $emparray[] = $row[firstname] . " " .$row[lastname];
}
    
$final = json_encode($emparray);
$other = prettyPrint( $final);
    
echo "<html><p><pre><span class='inner-pre' style='font-size: 25px'>$other</></p></html>";
    
mysqli_close($connection);



function prettyPrint( $json ){
    $result = '';
    $level = 0;
    $in_quotes = false;
    $in_escape = false;
    $ends_line_level = NULL;
    $json_length = strlen( $json );

    for( $i = 0; $i < $json_length; $i++ ) {
        $char = $json[$i];
        $new_line_level = NULL;
        $post = "";
        if( $ends_line_level !== NULL ) {
            $new_line_level = $ends_line_level;
            $ends_line_level = NULL;
        }
        if ( $in_escape ) {
            $in_escape = false;
        } else if( $char === '"' ) {
            $in_quotes = !$in_quotes;
        } else if( ! $in_quotes ) {
            switch( $char ) {
                case '}': case ']':
                    $level--;
                    $ends_line_level = NULL;
                    $new_line_level = $level;
                    break;

                case '{': case '[':
                    $level++;
                case ',':
                    $ends_line_level = $level;
                    break;

                case ':':
                    $post = " ";
                    break;

                case " ": case "\t": case "\n": case "\r":
                    $char = "";
                    $ends_line_level = $new_line_level;
                    $new_line_level = NULL;
                    break;
            }
        } else if ( $char === '\\' ) {
            $in_escape = true;
        }
        if( $new_line_level !== NULL ) {
            $result .= "\n".str_repeat( "\t", $new_line_level );
        }
        $result .= $char.$post;
    }

    return $result;
}



?> 