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

## Harmonic Waves

> $$ y(x,t) = A\cos(\omega t - kx) $$
> where $\phi = kx$.

Definition of Wavelength
> $$ \cos(kx) = \cos[k(x+\lambda)] = \cos(kx + 2\pi) $$
> So
> $$ k\lambda = 2\pi $$

***General Equation***
> $$ y(x,t) = A\cos(kx - \omega t) $$
> Period of Oscillation
> $$ P = \frac{2\pi}{\omega} $$
> Wave Number
> $$ k = \frac{2\pi}{\lambda} $$
> Speed of Wave
> $$ v_{wave} = \frac{\lambda}{P} = \frac{\omega}{k} = f\lambda $$
> $$ v_{average} = \frac{4A}{P} $$

### Dynamic

For a tiny element in a string:
> $$ \Sigma F_x = T(\cos(\theta_1) - \cos(\theta_2)) = 0 $$
> $$ \Sigma F_y = T(\sin(\theta_2) - \sin(\theta_1)) \approx T(\theta_2 - \theta_1) = Td\theta $$
> Therfore
> $$ \Sigma F_y = Td\theta = dma_y = \mu dx a_y $$
> Because $\mu = \frac{dm}{dx}$, the mass density of string.
> Therefore
> $$ T\frac{d\theta}{dx} = \mu a_y $$
> Also:
> $$ \theta \approx \tan(\theta) = \frac{dy}{dx} $$
> $$ F_{Net} = T\frac{d^2y}{dx^2} = \mu a_y = \mu \frac{d^2y}{dt^2} $$
> **Therefore**
> $$ \frac{d^2y}{dx^2} = \frac{\mu}{T}\frac{d^2y}{dt^2} $$
> **Finally** (Go back to Unit26 pre *"The Wave Equation"* and read twice!!!)
> $$ -k^2y = -\frac{\mu}{T}\omega^2y $$
> That is
> $$ \sqrt{\frac{T}{\mu}} = \frac{\omega}{k} $$
> **Therefore**
> $$ v_{wave} = \frac{\lambda}{P} = \frac{\omega}{k} = \sqrt{\frac{T}{\mu}} $$
> $$ v_{wave} = \sqrt{\frac{T}{\mu}} $$

## **Wave Equation**

> $$ \frac{d^2y}{dx^2} = \frac{1}{v^2}\frac{d^2y}{dt^2} $$
> Where $v$ (the speed of the wave) depends only on the properties of the Wave's Medium($T$, and$\mu$.)

## Waves and Superposition

> Because $v = \frac{\omega}{k}$,
> $$ y(x,t) = A \cos(kx - \omega t) = A\cos[k(x - vt)] $$
> Therefore
> $$ y(x,t) = f(x - vt) $$
> Which is the solution to the wave equation.
> $$ \frac{d^2y}{dx^2} = \frac{1}{v^2}\frac{d^2y}{dt^2} $$

By differentiating this solution respect to x or t and plug them into the wave equation, we have
> $$ f'' = \frac{1}{v^2}v^2f''\ \ \ \ \checkmark $$

**Notice** this function $$ y(x,t) = f(x - vt) $$ can represented for waves with **any shape** (not only harmonic).

## Superposition

Observations

1. The sum of the waves appear to stand still (**standing waves**)
2. THe waves do not interact.

### **Standing waves**

> $$ y(x,t) = A\cos(kx-\omega t) + A\cos(kx + \omega t) \\ = 2A\cos(kx)\cos(\omega t) $$
> therefore
> $$ y(x,t) = 2A\cos(kx)\cos(\omega t) $$

#### Example: Turning a Guitar

> Because
> $$ \lambda_{fundamental} = 2L $$
> $$ v_{wave} = \lambda f $$
> $$ T = \mu v^2_{wave} $$
> Because T is almost the same.

***Therefore**
> $$ f_i = \frac{v_i}{\lambda} = \frac{1}{\lambda}\sqrt{\frac{T}{\mu_i}} $$
> **smaller $f_i$, larger $\mu_i$**.