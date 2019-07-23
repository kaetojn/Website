<?php
   include('db/sessions/adminsession.php');
?>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <html>
<head>
<meta charset="UTF-8">
<title>Admin View</title>
<link rel="shortcut icon" href="">

<link href="stylesheets72.css" rel="stylesheet" type="text/css"/>
<link href="themes/default/style.min.css" rel="stylesheet" type="text/css" />
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<script src="scripts/jquery-3.0.0.min.js"></script>
<script src="scripts/jstree.js"></script>
<script src="scripts/jstreegrid.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script> 
<script src='scripts/jquery-sortable.js'></script>
<script src='scripts/tloading.js' type="text/javascript"></script>
<script src='scripts/saver2.js' type="text/javascript"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>



</head>

<body>

<button id="myButton" class="float-left submit-button" >Sign Out</button>


<div class="centers" id="img">
	<img src="thales-logo.jpg" width="100%" height="100%">
</div>
<br><br><br>
<div class="centers" id="tree">
	<div id="container1" class="demo" style="overflow-y: scroll;"></div>
	<br>
	
	<div style="text-align:center;">
    		<button class="btn btn-info btn-lg" id="button3">Save Changes</button>
    		<button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal" id="button2">Add Attributes</button>
    		<button class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal" id="button1">Edit Attributes</button>
	</div>
</div>


<div id="content2" style="display: none;"></div>
<div id="content3"></div>

<div class="container">
  <div class="modal fade" id="myModal" role="dialog">
    <div class="modal-dialog">
    
      <!-- Modal content-->
      <div class="modal-content">
        <div class="modal-body">
        <form id="form" action="" method="post" onsubmit="div2form('form')" autocomplete="off">
          ID: <strong><div id="key" name="formdiv" ></div></strong>
          <br> 
  	  Assigned:<br>
  	    <input list="users" name="assigned">
  	    <datalist id="users">
    		<option value="N/A">
    		<option value="Mary Iafrate">
    		<option value="Nick Peppas">
    		<option value="David Zhou">
    		<option value="Kaeto Ndu">
    		<option value="Sam Yang">
    		<option value="Victoria Paykin">
  	</datalist>
  	  <br>
  	  Due Date:<br>
  	  <input type="date" name="due">
  	  <br>
  	  Priority:<br>
  	  <select name="priority">
    		<option value="Low">Low</option>
    		<option value="Medium">Medium</option>
    		<option value="High">High</option>
  	  </select>
  	  <br>
  	  Status:<br>
  	  <select name="status">
    		<option value="Unassigned">Unassigned</option>
    		<option value="Queue">Queue</option>
    		<option value="Assigned">Assigned</option>
    		<option value="Accepted">Accepted</option>
    		<option value="In Progress">In Progress</option>
    		<option value="On Hold">On Hold</option>
    		<option value="Submitted">Submitted</option>
    		<option value="Review">Review</option>
    		<option value="Completed">Completed</option>
  	  </select>
  	  <br><br>
  	  <input type="submit" value="Submit">
	</form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        </div>
      </div>
      
    </div>
  </div>
  
</div>

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
    function div2form(id){
        var form=document.getElementById(id);
        if(!form){
            return;
        }
        var divs = document.getElementsByName(id+'div');
        for(var i=0; i<divs.length; i++){
            if(document.getElementById('textarea'+divs[i].id)){
               document.getElementById('textarea'+divs[i].id).value=divs[i].innerHTML; 
            } else {
                var texta=document.createElement('TEXTAREA');
                texta.name=divs[i].id;
                texta.id='textarea'+divs[i].id;
                texta.value=divs[i].innerHTML;      
                texta.style.display='none';
                form.appendChild(texta);                
            }                  
        }          
    }
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

        $.post('db/attribute.php', {data: paramJSON}, function(){alert("Atributes Saved");});
        return false;
    });
});
</script>

<script type="text/javascript">
    document.getElementById("myButton").onclick = function () {
        location.href = "db/sessions/logout.php";
    };
</script>


</body>
</html>

