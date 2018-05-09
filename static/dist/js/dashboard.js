$(document).ready(function(){
	function initializeDashboard(){
		$.ajax({
			url: 'getGraphics',
			type: 'GET',
			beforeSend: function() {
				$("#loading,#loading-overlay").show();
			},
			complete: function(){
				$("#loading,#loading-overlay").hide();
			},
			success: function(response) {
				result = JSON.parse(response);
				if(result.dept.success == true){
					var chart = Highcharts.chart('departmentChart', {
						title: {
							text: ''
						},
						xAxis: {
							categories: result.dept.departments
						},
						series: [{
							type: 'column',
							colorByPoint: true,
							data: result.dept.orders,
							showInLegend: false
						}]
					});
				} 
				else{
					
				}
				
				$("#loading,#loading-overlay").hide();
			},
			error: function(error) {
				$("#loading,#loading-overlay").hide();
			}
		});
	}	
	
	initializeDashboard();
});