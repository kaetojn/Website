$(document).ready(function(){
    $("#button3").click(function(){
	var objtree = $("#container1").jstree(true).get_json('#', { 'flat' : true });
        var fulltree = JSON.stringify(objtree);
        var myarray = $.parseJSON(fulltree);
        var params = { myarray: myarray };
	var paramJSON = JSON.stringify(params);
        $.post('db/update.php',{ data: paramJSON }, function(data){alert(data);});
        alert("Tree Saved");
        location.reload();
        
    });
});