 var carn;
 var coun;


$("#show_form").click(function(){
    $(this).css("display", "none")
    $("#new_car_form").css("display", "block")
})



$("#b").click(function(){
	$("#tb").append('<tr>' + '<td>' + $('#car_name').val() + '</td>' 
	 								+ '<td>' + $('#country').val() + '</td>' 
	 								+ '<td>' + '<button id="btn" class="btn btn-danger">Delete</button>' + '</td>' 
	 								+ '<td><button id="edit" type="button" class="btn btn-primary glyphicon glyphicon-edit" data-toggle="modal" data-target="#myModal"></button></td>' 
	 							 + '</tr>');
	$("#new_car_form").css("display", "none")
	$("#show_form").css("display", "block")
	})
	$("#tb").on('click', '#btn', (function(){
			$(this).parent().parent().remove() 
	}))

	$('#tb').on('click', '#edit', function(){
		 carn = $(this).parent().parent().find('td').first();
		 coun = carn.next();
			$ ('#carn').val(carn.html());
			$ ('#coun').val(coun.html());
		$('#myModal').on('click', '#save', function(){
			carn.html($('#carn').val());
			coun.html($('#coun').val());

		})	
})



	
	


	
	 

	