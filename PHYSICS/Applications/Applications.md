# Applications

## Simple Harmonic Motion

A mass plus a string:
> $$ -kx = ma $$
the diferential form of the displacement
> $$ \frac{d^2x}{dt^2} = -\frac{k}{m} x = -\omega^2 x $$
>
> Because considering sin() and cos(), the second derivative of them are the negative themselves. So we assume:
> $$ x(t) = Asin(\omega t)$$
> or
> $$ Acos(\omega t) $$

So: **General Solution**:
> $$ x(t) = Asin(\omega t - \phi) + Acos(\omega t - \phi) $$
>**$\phi$ is the phase angle**
>
>$$ \omega = \sqrt{\frac{k}{m}} = \frac{2 \pi}{T} $$
>
> If $x(t) = D cos(\omega t)$,
> $$v(t) = -\omega D sin(\omega t) $$
> $$a(t) = -\omega^2 D cos(\omega t)$$

### Initial Conditions

> $$x(0) = Acos(\phi) = x_0 $$
> $$v(0) = -\omega A sin(\phi) = v_0 $$
> $$cot(\phi) = -\frac{\omega x_0}{v_0} $$
> $$ A = \frac{x_0}{cos(\phi)} $$

### Energy

> $$ E = \frac{1}{2}k A^2 $$