settings.outformat = "pdf";
size(30cm);
real a = 4.0, b = 4.0;
int m = 5, n = NNN;
real w = a*m, h = b*n;
path out = (-1, -1) -- (-1, h+1) -- (w+1, h+1) -- (w+1, -1) -- cycle;

fill(out, RGB(255, 255, 255));

void coloring(int row, int column, Label entry, pen color)
{
	fill((row*a, (n-column)*b) -- (row*a+a, (n-column)*b) -- (row*a+a, (n-column)*b+b) -- (row*a, (n-column)*b+b) -- cycle, color);
	label(entry, (row*a+a/2, (n-column)*b+b/2), p = fontsize(20pt));
}

draw(out, white);

REPLACE

for (int i = 0; i < n+1; ++i)
{
	draw((0, i*b) -- (w, i*b), linewidth(1.0pt));
}
for (int i = 0; i < m+1; ++i)
{
	draw((i*a, 0) -- (i*a, h), linewidth(1.0pt));
}

