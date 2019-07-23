$(document).ready(function() {
  document.getElementById('button3').style.visibility = 'hidden';
  document.getElementById('button2').style.visibility = 'hidden';
  document.getElementById('button1').style.visibility = 'hidden';
  $('#container1').jstree({
  "plugins" : ["contextmenu", "dnd", "wholerow", "state"],
  'core' : {
  	"check_callback" : true,
	"themes": {"default" : true, "dots" : true},   
	"multiple" : false,
	'data' : {
        	"url" : "db/read.php",
        	"dataType" : "JSON",
        }},

    "contextmenu":{         
	    "items": function($node) {
	        var tree = $("#container1").jstree(true);
	        return {
	            "Create": {
	                "separator_before": false,
	                "separator_after": false,
	                "label": "Create",
	                "action": function (obj) { 
	                    $node = tree.create_node($node);
	                    tree.edit($node);
	                    document.getElementById('button3').style.visibility = 'visible';
	                }
	            },
	            "Rename": {
	                "separator_before": false,
	                "separator_after": false,
	                "label": "Rename",
	                "action": function (obj) { 
	                    tree.edit($node);
	                    document.getElementById('button3').style.visibility = 'visible';
	                }
	            },
	            "Nick Rules": {
	                "separator_before": false,
	                "separator_after": false,
	                "label": "Nick Rules",
	                "action": function (obj) { 
	                    tree.rename_node($node, 'Nick Rules');
	                    document.getElementById('button3').style.visibility = 'visible';
	                }
	            },                         
	            "Remove": {
	                "separator_before": false,
	                "separator_after": false,
	                "label": "Remove",
	                "action": function (obj) { 
	                    tree.delete_node($node);
	                    document.getElementById('button3').style.visibility = 'visible';
	                }
	            }
	        };
	    }
	}
  }).on("select_node.jstree", function (e, data) {
  	var x = $('#container1').jstree('get_selected');
  	document.getElementById("key").innerHTML = x[0];
  	myFunction();
  	myFunction2();

  	
  	
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
    function myFunction2(){
    $.ajax({
        type: 'POST',
        url: 'db/info.php',
        success: function(result) {
            var data = jQuery.parseJSON(result);
            var keys = [];
            
            for(var i = 0; i<data.length; i++){
            	keys.push(data[i].key);
            }
            var x = document.getElementById("key").innerHTML;
            savedKeys();
            var z = document.getElementById("content2").innerHTML;
            
            var a = keys.indexOf(x);
            var b = z.includes(x);

            if(b == true){
            	if(a == -1){
            		document.getElementById('button2').style.visibility = 'visible';
            		document.getElementById('table').style.visibility = 'hidden';
            		document.getElementById('button1').style.visibility = 'hidden';
            	}
            	else{
            		document.getElementById('button2').style.visibility = 'hidden';
            		document.getElementById('table').style.visibility = 'visible';
            		document.getElementById('button1').style.visibility = 'visible';
            		
            	}
            }
            else{
            	document.getElementById('button2').style.visibility = 'hidden';
            	document.getElementById('button1').style.visibility = 'hidden';
            	
            	if(a == -1){
			document.getElementById('button2').style.visibility = 'hidden';
			document.getElementById('button1').style.visibility = 'hidden';
            	}
            }

        }
    });
};
function savedKeys(){
    $.ajax({
    	type: 'POST',
        url: 'db/read.php',
        success: function(results){
            var data = jQuery.parseJSON(results);
            var keys2 = [];
            for(var i = 0; i<data.length; i++){
            	keys2.push(data[i].id);
            }
            document.getElementById("content2").innerHTML = keys2;
        }
    });
};
});