$(document).ready(function(){
	var $content = $("#content");
	$("#head,#foot").css("width",$content.outerWidth());
    $(window).resize(function(){
        $("#head,#foot").css("width",$content.outerWidth());
    })
	setTimeout(function(){
		$("#loading").css("display","none");
	},1000);
    /*
	 *if($.browser.msie){
	 *    if($.browser.version == '6.0'){
	 *        var $img = $("#details img");
	 *        if($img.width() > 840){
	 *            $img.css('width','840px')
	 *        }
	 *    }
	 *}
     */
	$("#replay_form").submit(function(){
		if($("#id_name").val().length ==0 || $("#id_message").val().length == 0){
			alert("名称和内容是必填项!")
			return false
		}
	})
});
