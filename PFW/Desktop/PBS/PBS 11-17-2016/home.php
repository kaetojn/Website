<?php
   include('db/sessions/session.php');
?>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     <html>
<head>
<meta charset="UTF-8">
<title>Homepage</title>
<link rel="shortcut icon" href="">

<link href="stylesheets72.css" rel="stylesheet" type="text/css"/>
<link href="themes/default/style.min.css" rel="stylesheet" type="text/css" />
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<script src="scripts/jquery-3.0.0.min.js"></script>
<script src="scripts/jstree.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script> 
<script src='scripts/userloading.js' type="text/javascript"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>



</head>

<body oncontextmenu="return false">
<button id="myButton" class="float-left submit-button" >Sign Out</button>
<div class="centers" id="img">
	<img src="thales-logo.jpg" width="100%" height=100%>
</div>
<br>
<div class="centers" id="tree">
	<div id="container1" class="demo" style="overflow-y: scroll;"></div>
</div>


<div id="content2" style="display: none;"></div>
<div id="content3" style="display: none;"></div>
<div id="key" name="formdiv" style="display: none;"></div>


<div class="centers" id="footer">
	
	
	<table style="width: 100%;" align="center" id="table">
		<tbody>
			<tr>
				<td style="width: 25%;" align="center"><hdr><strong>Assigned</strong></hdr></td>
				<td style="width: 50%;"><text><div id="assigned"></div></text></td>
			</tr>
			<tr>
				<td style="width: 25%;" align="center"><hdr><strong>Due Date</strong></hdr></td>
				<td style="width: 50%;"><text><div id="due"></div></text></td>
			</tr>
			<tr>
				<td style="width: 25%;" align="center"><hdr><strong>Priority</strong></hdr></td>
				<td style="width: 50%;"><text><div id="priority"></div></text></td>
			</tr>
			<tr>
				<td style="width: 25%;" align="center"><hdr><strong>Status</strong></hdr></td>
				<td style="width: 50%;"><text><div id="status"></div></text></td>
			</tr>
		</tbody>
	</table>
</div>

<script type="text/javascript">
    document.getElementById("myButton").onclick = function () {
        location.href = "db/sessions/logout.php";
    };
</script>

</body>
</html>

