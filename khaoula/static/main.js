function afficherArgent(id)
{
	var http = new XMLHttpRequest();
	var url = 'money/'+id;
	http.open('GET', url, true);
	http.onreadystatechange = function() 
	{//Call a function when the state changes.
		var donnee=JSON.parse(http.responseText);
		if(window.confirm(donnee.money))
		{
			print('ok')
		}
	}
	http.send();
			
}
function Couleur(id)
{
	if(document.getElementById(id).style['background-color']=="green")
	{
		var http = new XMLHttpRequest();
		var url = 'reserver/'+id;
		http.open('GET', url, true);
		http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
		http.onreadystatechange = function() 
		{//Call a function when the state changes.
		    if(http.readyState == 4 && http.status == 200)
			{document.getElementById(id).style['background-color']="red"}
		}
		http.send();
		
	}
	else
	{
		var http = new XMLHttpRequest();
		var url = 'reserver/'+id;
		http.open('GET', url, true);
		http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
		http.onreadystatechange = function() 
		{//Call a function when the state changes.
		    if(http.readyState == 4 && http.status == 200)
			{document.getElementById(id).style['background-color']="green"
			afficherArgent(id)}
		}
		http.send();
	}
	    
}
function init_Couleur()
{
	liste = [10,11,12,13,14,15,20,21,22,23,24,25,30,31,32,33,34,35];
	liste.forEach(function(id)
	{
		var http = new XMLHttpRequest();
		var url= 'color/'+id;
		http.open('GET', url, true);
		//Send the proper header information along with the request
		http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
		http.onreadystatechange = function() 
		{//Call a function when the state changes.
		    if(http.readyState == 4 && http.status == 200)
			{
			var donnee=JSON.parse(http.responseText);
			if(donnee.etat== 0)
				{
				document.getElementById(id).style['background-color']="red";
				}
			else
				{
				document.getElementById(id).style['background-color']="green";
				}
			}
		}
	http.send();	    
	})
	
}
setInterval(init_Couleur, 5000);

