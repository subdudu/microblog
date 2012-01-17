$(document).ready(function() {
	$.get("/posts/realtime_posts", function(data, status, xhr) {
		data = eval("(" + data + ")");
		$("#realtime_posts").html(data);
	});
});
