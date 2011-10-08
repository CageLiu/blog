$(document).ready(function(){
	var $content = $("#content");
	$("#head,#foot").css("width",$content.outerWidth());
	setTimeout(function(){
		$("#loading").css("display","none");
	},1000)
})
