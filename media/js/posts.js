$(document).ready(function() {
	$.getJSON("/posts/realtime_posts", function(data, status, xhr) {
		$("#realtime_posts").html(data[0].content);
	});
});

var show_posts = function(posts) {}
