$(document).ready(function(){
	var $content = $("#content");
	$("#head,#foot").css("width",$content.outerWidth());
	setTimeout(function(){
		$("#loading").css("display","none");
	},1000);
	if($.browser.msie){
		if($.browser.version == '6.0'){
			var $img = $("#details img");
			if($img.width() > 840){
				$img.css('width','840px')
			}
		}
	}
});
