function Couleur(id){
//console.log(id+" "+$('#'+id).css("background-color"))
	$.ajax({
        type: 'GET',
        url:  'reserver/'+id,
	 	success: 
			function(etat){
					var state = $.parseJSON(etat)
				if(state.etat==0)
					{console.log(state.etat)
					$('#'+id).css("background-color", "red");}
				else if(state.etat==1)
				{
					if(window.confirm(state.money))
					{
						$('#'+id).css("background-color", "green");
					}
					
				}
					}
				});
};
//function afficherArgent(id)
//{
//	$.ajax({
//		type:'GET',
//		url: 'money/'+id,
//		success:
//		function(money){
//			var state = $.parseJSON(money)

//		}
//	});
			
//};

$(document).ready( function() 
{
	$.ajax({
		type: 'GET',
		url:  'idplace/',
		success: function(data){
			var li = $.parseJSON(data)
			//console.log(typeof(li));
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
