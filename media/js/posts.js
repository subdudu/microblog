$(document).ready(function() {
	$.getJSON("/posts/latest_posts", function(data, status, xhr) {
		var s = "";
		for (p in data) {
			s += "<div><span>" + data[p].content + "</span><span>" + data[p].last_mod_time + "</span></div>";
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
			s += "<div><span>" + data[p].content + "</span><span>" + data[p].last_mod_time + "</span></div>";
		};
		$("#realtime_posts div:first").before(s);
		setTimeout("add_realtime_posts()", 3000);
	})
}
