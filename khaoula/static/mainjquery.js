function Couleur(id){
console.log(id+" "+$('#'+id).css("background-color"))
	$.ajax({
         type: 'GET',
         url:  'reserver/'+id
		})
 	.done(function ()
		{
		if($('#'+id).css('background-color') == "rgb(0, 128, 0)")
			$('#'+id).css("background-color", "red");
		else
			$('#'+id).css("background-color", "green");
		 });
};
$(document).ready( function() 
{
    var refreshId = setInterval( function() 
    {
	liste = [10,11,12,13,14,15,20,21,22,23,24,25,30,31,32,33,34,35];
	liste.forEach(function(id)
	{
		$.ajax({
         	 type: 'GET',
         	 url:  'color/'+id
		})
 		.done( function (responseText)
			{
			var donnee=JSON.parse(responseText);
			if(donnee.etat== 0)
			{$('#'+id).css("background-color", "red");}
			else {$('#'+id).css("background-color", "green");}
		
		});
})
}, 5000);
});
