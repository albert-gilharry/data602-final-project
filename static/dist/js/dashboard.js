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
				
				if(result.aisles.success == true){
					
					Highcharts.chart('aisles', {
						chart: {
							type: 'column'
						},
						title: {
							text: ''
						},
						xAxis: {
							type: 'category',
							labels: {
								rotation: -45,
								style: {
									fontSize: '13px',
									fontFamily: 'Verdana, sans-serif'
								}
							}
						},
						yAxis: {
							min: 0,
							title: {
								text: 'Orders'
							}
						},
						legend: {
							enabled: false
						},
						tooltip: {
							pointFormat: 'Instacart orders: <b>{point.y:.1f}</b>'
						},
						series: [{
							name: 'Aisles',
							data: result.aisles.data,
							dataLabels: {
								enabled: true,
								rotation: -60,
								color: '#FFFFFF',
								align: 'right',
								format: '{point.y:.1f}', // one decimal
								y: 10, // 10 pixels down from the top
								style: {
									fontSize: '13px',
									fontFamily: 'Verdana, sans-serif'
								}
							}
						}]
					});					
				}
				
				if(result.hour_of_day.success == true){
					var chart = Highcharts.chart('tod', {
						title: {
							text: ''
						},
						xAxis: {
							categories: result.hour_of_day.hour
						},
						series: [{
							type: 'column',
							colorByPoint: true,
							data: result.hour_of_day.orders,
							showInLegend: false
						}]
					});
				} 
				
				if(result.doweek.success == true){		
					Highcharts.chart('dow', {
						chart: {
							plotBackgroundColor: null,
							plotBorderWidth: null,
							plotShadow: false,
							type: 'pie'
						},
						title: {
							text: ''
						},
						tooltip: {
							pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
						},
						plotOptions: {
							pie: {
								allowPointSelect: true,
								cursor: 'pointer',
								dataLabels: {
									enabled: true,
									format: '<b>{point.name}</b>: {point.percentage:.1f} %',
									style: {
										color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
									}
								}
							}
						},
						series: [{
							name: 'Orders',
							colorByPoint: true,
							data: result.doweek.data
						}]
					});					
				}
				$("#num_orders").text(result.num_orders);
				$("#num_users").text(result.num_users)
				$("#num_products").text(result.num_products)
				$("#top_product").text(result.top_product)
				
				$("#loading,#loading-overlay").hide();
			},
			error: function(error) {
				$("#loading,#loading-overlay").hide();
			}
		});
	}	
	$("#loading,#loading-overlay").hide();
	initializeDashboard();
});