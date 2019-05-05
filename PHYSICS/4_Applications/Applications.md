# Applications

## Simple Harmonic Motion

A mass plus a string:
> $$ -kx = ma $$
the diferential form of the displacement
> $$ a = \frac{d^2x}{dt^2} = -\frac{k}{m} x = -\omega^2 x $$
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

</br>
</br>
</br>
</br>
</br>

## Torsion Pendula

> **Restoring** Torque for a *Torsion Pendulum*:
> $$ \tau = -\kappa \theta $$
> Therefore
> $$ \alpha = \frac{\tau_{Net}}{I} = \frac{-\kappa \theta}{I} = \frac{d^2 \theta}{d t^2} = - \omega ^2 \theta $$
> where
> $$ \omega = \sqrt{\frac{\kappa}{I}} $$

So the **General Solution** is:
> $$ \theta(t) = \theta_{max} \cos(\omega t + \phi)

## The Physical Pendula

Torque due to Weight:
> $$ \tau_{Weight} = MgX_{CM} $$

Newton's 2nd Law for Rotations:
> $$ \tau = -MgX_{CM} = I\alpha $$
> For **small $\theta$s**:
> $$ X_{CM} = R_{CM} \theta $$
> So
> $$ -MgR_{CM} \theta = I \alpha = I \frac{d^2 \theta}{d t^2} $$
In general
> $$ -\omega^2 \theta = \frac{d^2 \theta}{d t^2} $$
> where
> $$ \omega = \sqrt{\frac{MgR_{CM}}{I}}

## The Simple Pendula

A point mass m, attached to a massless string.

As being discussed before:
> $$ \omega = \sqrt{\frac{Mg R_{CM}}{I}} = \sqrt{\frac{MgL}{ML^2}} = \sqrt{\frac{g}{L}}