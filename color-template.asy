settings.outformat = "pdf";
size(30cm);
real a = 4.0, b = 1.0;
int m = 5, n = 9;
real w = a*(m+1), h = b*(n+1);
path out = (-1, -1) -- (-1, h+1) -- (w+1, h+1) -- (w+1, -1) -- cycle;
pen color_a = RGB(142, 171, 249), color_b = RGB(68, 255, 58), color_c = RGB(103, 222, 155), color_d = RGB(255, 237, 124), color_e = RGB(243, 165, 88), color_f = RGB(200, 200, 200);

fill(out, RGB(0, 255, 255));

void coloring(int row, int column, pen color)
{
	fill((row*a, (n-column)*b) -- (row*a+a, (n-column)*b) -- (row*a+a, (n-column)*b+b) -- (row*a, (n-column)*b+b) -- cycle, color);
}

draw(out, white);

REPLACE

for (int i = 0; i < n+2; ++i)
{
	draw((0, i*b) -- (w, i*b), linewidth(1.0pt));
}
for (int i = 0; i < m+2; ++i)
{
	draw((i*a, 0) -- (i*a, h), linewidth(1.0pt));
}

