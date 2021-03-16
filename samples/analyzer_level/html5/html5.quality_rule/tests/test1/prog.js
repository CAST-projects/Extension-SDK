function f() {
	g(a, function() { });
	i = 0;
	while (i < 6) {
		i = i + 1;
		if ( i == 6)
			break;
	}
}