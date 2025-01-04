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

coloring(1, 1, RGB(236, 218, 59));
coloring(1, 2, RGB(166, 43, 188));
coloring(1, 3, RGB(1, 191, 153));
coloring(1, 4, RGB(187, 49, 48));
coloring(1, 5, RGB(133, 43, 217));
coloring(1, 6, RGB(160, 250, 230));
coloring(1, 7, RGB(151, 188, 9));
coloring(1, 8, RGB(129, 251, 46));
coloring(1, 9, RGB(10, 58, 226));
coloring(2, 1, RGB(6, 136, 245));
coloring(2, 2, RGB(253, 163, 253));
coloring(2, 3, RGB(6, 55, 29));
coloring(2, 4, RGB(40, 8, 59));
coloring(2, 5, RGB(90, 253, 75));
coloring(2, 6, RGB(198, 7, 136));
coloring(2, 7, RGB(211, 105, 0));
coloring(2, 8, RGB(60, 187, 2));
coloring(2, 9, RGB(97, 201, 58));
coloring(3, 1, RGB(71, 32, 141));
coloring(3, 2, RGB(239, 14, 12));

for (int i = 0; i < n+2; ++i)
{
	draw((0, i*b) -- (w, i*b), linewidth(1.0pt));
}
for (int i = 0; i < m+2; ++i)
{
	draw((i*a, 0) -- (i*a, h), linewidth(1.0pt));
}

