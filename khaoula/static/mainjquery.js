function money(){
	
	$.ajax({
		type: 'GET',
		url:  '/money',
	 	success: 
			function(resultat){
					var result = $.parseJSON(resultat)
					console.log(result)
					if (window.confirm(result.money))
					{
					}
				
					}
				});
}
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

