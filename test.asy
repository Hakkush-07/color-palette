settings.outformat = "pdf";
size(30cm);
real a = 4.0, b = 4.0;
int m = 5, n = 2;
real w = a*m, h = b*n;
path out = (-1, -1) -- (-1, h+1) -- (w+1, h+1) -- (w+1, -1) -- cycle;

fill(out, RGB(255, 255, 255));

void coloring(int row, int column, Label entry, pen color)
{
	fill((row*a, (n-column)*b) -- (row*a+a, (n-column)*b) -- (row*a+a, (n-column)*b+b) -- (row*a, (n-column)*b+b) -- cycle, color);
	label(entry, (row*a+a/2, (n-column)*b+b/2), p = fontsize(20pt));
}

draw(out, white);

coloring(0, 1, "\#57b569", RGB(87, 181, 105));
coloring(1, 1, "\#1f7c96", RGB(31, 124, 150));
coloring(2, 1, "\#2b4dbd", RGB(43, 77, 189));
coloring(3, 1, "\#2a1fff", RGB(42, 31, 255));
coloring(4, 1, "\#bb881a", RGB(187, 136, 26));
coloring(0, 2, "\#f9aabf", RGB(249, 170, 191));
coloring(1, 2, "\#20fd15", RGB(32, 253, 21));
coloring(2, 2, "\#d81cac", RGB(216, 28, 172));
coloring(3, 2, "\#eb131", RGB(235, 1, 49));
coloring(4, 2, "\#47613", RGB(71, 6, 19));

for (int i = 0; i < n+1; ++i)
{
	draw((0, i*b) -- (w, i*b), linewidth(1.0pt));
}
for (int i = 0; i < m+1; ++i)
{
	draw((i*a, 0) -- (i*a, h), linewidth(1.0pt));
}

