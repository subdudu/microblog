$(document).ready(function() {
	$.getJSON("/posts/latest_posts", function(data, status, xhr) {
		var s = "";
		for (p in data) {
			s += "<div><span>" + data[p].content + "</span><span>" + data[p].last_mod_time + "</span></div>";
		};
		$("#realtime_posts").html(s);
		setTimeout(add_realtime_posts, 1);
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
