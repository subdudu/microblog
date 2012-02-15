String.format = function(src){
	if (arguments.length == 0) return null;
	var args = Array.prototype.slice.call(arguments, 1);
	return src.replace(/\{(\d+)\}/g, function(m, i){
		return args[i];
	});
};

$(document).ready(function() {
	$.getJSON("/posts/latest_posts", function(data, status, xhr) {
		var s = "";
		for (p in data) {
			tpl = '<div class="clear p_wrapper"><a href="#"><img src="{0}" class="l" width="60" style="margin-bottom:10px;"/></a><div style="margin-left:70px;"><div><a href="#">{1}</a>&nbsp;-&nbsp;<span>{2}</span>&nbsp;-&nbsp;<span>{3}</span></div><div>{4}</div></div><hr class="clear" style="margin-top:10px;" /></div>';
			s += String.format(tpl, data[p].user_image, data[p].user_name, data[p].last_mod_time, data[p].publicly, data[p].content);
		};
		$("#realtime_posts").html(s);
		setTimeout(add_realtime_posts, 1);
	});
	$("#id_commit").click(function(){
		$.ajax({
			type: "POST",
			url: "/posts/add/",
			data: $("#form_post_ajax").serialize(),
			success: function(msg) {
				$("#id_content").val("");
				alert("提交成功");
			}
		});
	});
});

function add_realtime_posts() {
	$.getJSON("/posts/realtime_posts", function(data, status, xhr) {
		var s = "";
		for (p in data) {
			tpl = '<div class="clear p_wrapper"><a href="#"><img src="{0}" class="l" width="60" style="margin-bottom:10px;"/></a><div style="margin-left:70px;"><div><a href="#">{1}</a>&nbsp;-&nbsp;<span>{2}</span>&nbsp;-&nbsp;<span>{3}</span></div><div>{4}</div></div><hr class="clear" style="margin-top:10px;" /></div>';
			s += String.format(tpl, data[p].user_image, data[p].user_name, data[p].last_mod_time, data[p].publicly, data[p].content);
		};
		$("#realtime_posts div:first").before(s);
		setTimeout("add_realtime_posts()", 4000);
	})
}
