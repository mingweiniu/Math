import matplotlib.pyplot as plt

ax = plt.axes([0.1, 0.1, 1, 1]) #left,bottom,width,height
ax.axis('off')

ax.invert_yaxis()


a = r'f(x) = \frac{\exp(-x^2/2)}{\sqrt{2*\pi}}'
plt.text(0, 0.2, '$%s$' %a, size=25)

b = r'\vec{r} = \langle x, y, z \rangle'
plt.text(0, 0.4, '$%s$' %b, size=25)

c = r'\int_{-R}^{R} πr^2dy'
plt.text(0, 0.6, '$%s$' %c, size=25)

d = r'\oint_V f(s) \,ds'
plt.text(0, 0.8, '$%s$' %d, size=25)

e = r'\oiiint_V \mu(u,v,w) \,du\,dv\,dw'
plt.text(0, 1.0, '$%s$' %e, size=25)

f = r'\lim_{x\to\infty} f(x)'
plt.text(0.5, 0.2, '$%s$' %f, size=25)

g = r'\sum_{n=1}^{\infty} 2^{-n} = 1'
plt.text(0.4, 0.4, '$%s$' %g, size=25)

h = r'\prod_{i=a}^{b} f(i)'
plt.text(0.5, 0.6, '$%s$' %h, size=25)

i = r'\sqrt[3]{8} * 8^{\frac{isinθ + cosθ}{2}}'
plt.text(0.5, 0.8, '$%s$' %i, size=25)

plt.show()
