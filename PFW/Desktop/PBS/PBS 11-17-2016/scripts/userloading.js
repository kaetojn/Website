$(document).ready(function() {
  $('#container1').jstree({
  "plugins" : ["wholerow"],
  'core' : {
  	"check_callback" : true,
	"themes": {"default" : true, "dots" : true},   
	"multiple" : false,
	'data' : {
        	"url" : "db/read.php",
        	"dataType" : "JSON",
        }},
  }).on("select_node.jstree", function (e, data) {
  	var x = $('#container1').jstree('get_selected');
  	document.getElementById("key").innerHTML = x[0];
  	myFunction();

  	
  	
    });
    
    function myFunction(){
    $.ajax({
        type: 'POST',
        url: 'db/info.php',
        success: function(result) {
            var data = jQuery.parseJSON(result);
            for(var i = 0; i<data.length; i++){
            	if(document.getElementById("key").innerHTML == data[i].key){
            		document.getElementById("assigned").innerHTML = data[i].assigned;
            		document.getElementById("due").innerHTML = data[i].due;
            		document.getElementById("priority").innerHTML = data[i].priority + " priority";
            		document.getElementById("status").innerHTML = data[i].status;
            	}

            }

        }
    });
};
});