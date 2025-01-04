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

coloring(0, 1, "\#666c4c", RGB(102, 108, 76));
coloring(1, 1, "\#eeeab6", RGB(238, 234, 182));
coloring(2, 1, "\#ef70dc", RGB(239, 112, 220));
coloring(3, 1, "\#7e39ce", RGB(126, 57, 206));
coloring(4, 1, "\#7c845", RGB(124, 132, 5));
coloring(0, 2, "\#cc746", RGB(12, 199, 70));
coloring(1, 2, "\#163c5e", RGB(22, 60, 94));
coloring(2, 2, "\#2a82db", RGB(42, 130, 219));
coloring(3, 2, "\#954f89", RGB(149, 79, 137));
coloring(4, 2, "\#c7ce18", RGB(199, 206, 24));

for (int i = 0; i < n+1; ++i)
{
	draw((0, i*b) -- (w, i*b), linewidth(1.0pt));
}
for (int i = 0; i < m+1; ++i)
{
	draw((i*a, 0) -- (i*a, h), linewidth(1.0pt));
}

