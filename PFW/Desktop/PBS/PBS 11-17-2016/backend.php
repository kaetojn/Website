<?php
   include('db/sessions/adminsession.php');
?> 
<html>
<head>
<title>Admin Page</title>
<link href="stylesheets/backend.css" rel="stylesheet" type="text/css"/>
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script src="scripts/jquery-3.0.0.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

<style>

</style>
</head>


<body>
<input type="submit" value="Sign Out" id="myButton">

<div>
    <table style="text-align:center;">
	<tbody>
	<tr>
		<th style="text-align: center" colspan = "2">Views</th>
	</tr>
	<tr>
		<td><input type="button" onclick="location.href='admin.php';" value="Admin Tree View" /></td>
		<td><input type="button" onclick="location.href='home.php';" value="User Tree View" /></td>
	</tr>
	<tr>
		<td><input type="button" onclick="location.href='dir.php';" value="Directory View" /></td>
		<td><input type="button" onclick="location.href='db/adminer-4.2.5.php';" value="Database View" /></td>
	</tr>
	<tr>
		<th style="text-align: center" colspan = "2">Admin Actions</th>
	</tr>
	<tr>
		<td><input type="button" onclick="location.href='db/readtext.php';" value="View All Tasks" /></td>
		<td><input type="button" onclick="location.href='db/infotext.php';" value="View All Tasks Info" /></td>
	</tr>
	<tr>
		<th style="text-align: center" colspan = "2">User Actions</th>
	</tr>
	<tr>
		<td><input type="button" onclick="location.href='db/usertext.php';" value="View All Users" /></td>
		<td><button type="button" data-toggle="modal" data-target="#myModal" id="newuser" class="button">Create New User</button></td>
	</tr>
	</tbody>
    </table>
</div>

<div class="container">
  <div class="modal fade" id="myModal" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-body">
		<form action="" method="post" autocomplete="off">
			<legend>Register</legend>
			First Name:<br> <input type="text" name="firstname"><br>
			Last Name:<br> <input type="text" name="lastname"><br><br>
			TGI:<br> <input type="text" name="tgi" maxlength="8" value="T01" onkeypress='return event.charCode >= 48 && event.charCode <= 57'><br>
			Password:<br> <input type="password" name="password"><br><br>
			Type:<br>
			<select name="type">
  			<option value="admin">admin</option>
  			<option value="user">user</option>
			</select>
			<br><br>
			<input type="submit">
		</form>
	</div>
     </div>
   </div>
 </div>
</div>


<script type="text/javascript">
    document.getElementById("myButton").onclick = function () {
        location.href = "db/sessions/logout.php";
    };
</script>

<script type="text/javascript">
$.fn.serializeObject = function(){
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};

$(function() {
    $('form').submit(function() {
        var x = JSON.stringify($('form').serializeObject());
	var myarray = $.parseJSON(x);
        $('#result').text(x);
        console.log(x);
        
        var params = { myarray: myarray };
	var paramJSON = JSON.stringify(params);

        $.post('db/newuser.php', {data: paramJSON});
        location.reload();
        return false;
    });
});
</script>



</body>
</html>
