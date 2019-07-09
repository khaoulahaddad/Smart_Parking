function Couleur(id){
console.log(id+" "+$('#'+id).css("background-color"))
	$.ajax({
        type: 'GET',
        url:  'reserver/'+id,
	 	success: 
			function(){
			if($('#'+id).css('background-color') == "rgb(0, 128, 0)")
				$('#'+id).css("background-color", "red");
			else
				$('#'+id).css("background-color", "green");
		 }
		});
};
$(document).ready( function() 
{
	$.ajax({
		type: 'GET',
		url:  'idplace/',
		success: function(data){
			var li = $.parseJSON(data)
			console.log(typeof(li));
			Object.keys(li).forEach(element => {
				if(li[element].etat == true)
					{$('#'+li[element].idplace).css("background-color", "red");}
				else {$('#'+li[element].idplace).css("background-color", "green");}
			});
			/*var count = Object.keys(li).length
			console.log(count)
			for (var i = 0; i < count; i++)
				{
				if(li[i].etat == true)
					{$('#'+li[i].idplace).css("background-color", "red");}
				else {$('#'+li[i].idplace).css("background-color", "green");}
				}*/
		}
});
});
