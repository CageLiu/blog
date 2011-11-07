$(document).ready(function(){
	var $content = $("#content");
	$("#head,#foot").css("width",$content.outerWidth());
    $(window).resize(function(){
        $("#head,#foot").css("width",$content.outerWidth());
    })
	setTimeout(function(){
		$("#loading").css("display","none");
	},1000);

	$("#replay_form").submit(function(){
		if($("#id_name").val().length ==0 || $("#id_message").val().length == 0){
			alert("名称和内容是必填项!")
			return false
		}
	})
    $("#artlist a:contains('删除')").click(function(){
        if (!confirm("确认删除？")){
            return false
        }
    })
});
