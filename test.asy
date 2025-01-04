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

coloring(1, 1, RGB(188, 45, 19));
coloring(1, 2, RGB(14, 222, 83));
coloring(1, 3, RGB(40, 46, 134));
coloring(1, 4, RGB(217, 123, 24));
coloring(1, 5, RGB(227, 255, 20));
coloring(1, 6, RGB(57, 68, 228));
coloring(1, 7, RGB(52, 254, 236));
coloring(1, 8, RGB(245, 41, 5));
coloring(1, 9, RGB(45, 123, 251));
coloring(2, 1, RGB(21, 238, 161));
coloring(2, 2, RGB(13, 221, 22));
coloring(2, 3, RGB(120, 56, 205));
coloring(2, 4, RGB(144, 22, 227));
coloring(2, 5, RGB(43, 217, 16));
coloring(2, 6, RGB(218, 48, 86));
coloring(2, 7, RGB(230, 203, 56));
coloring(2, 8, RGB(235, 23, 215));
coloring(2, 9, RGB(50, 9, 6));
coloring(3, 1, RGB(191, 127, 238));
coloring(3, 2, RGB(41, 119, 1));

for (int i = 0; i < n+2; ++i)
{
	draw((0, i*b) -- (w, i*b), linewidth(1.0pt));
}
for (int i = 0; i < m+2; ++i)
{
	draw((i*a, 0) -- (i*a, h), linewidth(1.0pt));
}

