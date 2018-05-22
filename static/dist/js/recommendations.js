$(document).ready(function(){
	function initializeUsers(){	
		$.ajax({
			url: 'sampleUsers',
			type: 'GET',
			beforeSend: function() {
				$("#loading,#loading-overlay").show();
			},
			complete: function(){
				//$("#loading,#loading-overlay").hide();
			},
			success: function(response) {
				result = JSON.parse(response);
				
				if(result.success == true){	
				
					var output = [];
					for(i=0;i < result.data.length;i++){					
						output.push('<option value="'+ result.data[i][0] +'"> Customer '+ result.data[i][0] + '</option>');	
					}
					
					$('#users').html(output.join(''));
					$('#users').val(result.data[0][0]);
					$('#recommendations').html('');
					loadRecommendations();
				}	
				
			},
			error: function(error) {
				$("#loading,#loading-overlay").hide();
			}
		});
	}	
	
	function loadRecommendations(){
		var data = {"user":$("#users").val()};
		$('#recommendations').html('');
		$.ajax({
			data:data,
			url: 'getRecommendations',
			type: 'POST',
			beforeSend: function() {
				$("#loading,#loading-overlay").show();
			},
			complete: function(){
				$("#loading,#loading-overlay").hide();
			},
			success: function(response) {
				result = JSON.parse(response);
				
				if(result.success == true){	
				
					var output = [];
					for(i=0;i < result.data.length;i++){					
						output.push('<tr><td>' + result.data[i][0] + '</td><td>' + result.data[i][1] + '</td><td>' + result.data[i][2] + '</td><td>' + result.data[i][3] + '</td></tr>');	
					}
					
					$('#recommendations').html(output.join(''));
				}	
				
				$("#loading,#loading-overlay").hide();
			},
			error: function(error) {
				$("#loading,#loading-overlay").hide();
			}
		});	
	}
	
	$("#users").change(function(){
		loadRecommendations();	
	});
	
	$("#resample").click(function(){
		$('#recommendations').html('');
		initializeUsers();	
	});
	
	$("#loading,#loading-overlay").hide();
	initializeUsers();
});