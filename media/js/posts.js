$(document).ready(function() {
	$.getJSON("/posts/realtime_posts", function(data, status, xhr) {
		$("#realtime_posts").html(show_posts(data));
	});
});

var show_posts = function(posts) {
	var s = "";
	for (p in posts) {
		s += "<div><span>" + posts[p].content + "</span><span>" + posts[p].last_mod_time + "</span></div>";
	}
	return s;
}
