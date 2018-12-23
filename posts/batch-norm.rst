.. title: Batch Normalization Backpropagation
.. slug: batch-norm
.. date: 2018-05-12 19:02:02 UTC
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. has_math: yes


.. default-role:: math

Batch normalization is a technique for making neural networks easier to train.
Although these days, any deep learning framework will implement batch norm and its derivative for you, it is useful to see how to derive the gradient of batch norm. It seems to be often left as "an exercise for the reader" in deep learning courses. I had some trouble getting the correct derivation of the gradient on the first try so I've outlined the derivation here.

Notation:

- `z_{ij}`: Values after affine transformation (matrix multiplication by parameter `\mathbf{W}`).
- `\hat{z}_{ij}`: Values after normalization.
- `\tilde{z}_{ij}`: Values after scaling by parameters `\gamma_i` and `\beta_i`.
  `f`: Scalar cost function.

where `i = 1...n_\rm{out}` (number of layer outputs) and `j = 1...m` (number of examples in batch).


Equations for batch normalization:

.. math::
   \mu_i = \frac{1}{m} \sum_j z_{ij}

.. math::
   \sigma_i^2 = \frac{1}{m} \sum_j^m (z_{ij} - \mu_i)^2

.. math::
   \hat{z}_{ij} = \frac{z_{ij} - \mu_i}{\sqrt{\sigma_i^2 + \epsilon}}

.. math::
   \tilde{z}_{ij} = \gamma_i \hat{z}_{ij} + \beta_i

Goal
----

- Given: `\partial f / \partial \tilde{z}_{ij}` the array of derivatives of the scalar loss `f` with respect to the *output* `\tilde{z}_{ij}`.
- Derive: `\partial f / \partial \gamma_i`, `\partial f / \partial \beta_i`, the vectors of derivatives with respect to our parameters and `\partial f / \partial z_{ij}`, the array of derivatives with respect to the layer *inputs*.

We will start with the last equation, and derive the gradient with respect to the two parameters `\gamma_i` and `\beta_i`.

Derivation: `\partial f / \partial \gamma_i`
--------------------------------------------

We'll use the derivation of `\partial f / \partial \gamma_i` to demonstrate the general method of using the chain rule. Using the chain rule, the parital derivative we're after can be written in terms of the partial derivative we are given, and one we will derive from the above equations:

.. math::

   \frac{\partial f}{\partial \gamma_i} = \sum_{i'j'} \frac{\partial f}{\partial \tilde{z}_{i'j'}} \frac{\partial \tilde{z}_{i'j'}}{\partial \gamma_i}

Note that, in general, we must always sum over `i'` and `j'` in ths manner, as `\gamma_i` can affect `f` through any entry in `\tilde{z}_{i'j'}`. **This is the key point**: even though `\tilde{z}` and `\gamma` both have the same size in the first dimension (indexed by `i`), any entry in `\tilde{z}` might depend on any entry in `\gamma`: `\tilde{z}_{11}` might depend on `\gamma_1`, `\gamma_2`, `\gamma_3`, etc. and all these partial derivatives must be summed.

In this particular case, it happens to be simpler. We can see from the equation for `\tilde{z} that changing `\gamma_i` has no effect on `\tilde{z}_{i'j'}` for `i' \ne i`.
Or in other words, `\partial \tilde{z}_{i'j'} / \partial \gamma_i = 0` for `i' \ne i`.
So, only terms with `i' = i` actually contribute to the sum `\sum_{i'j'}`, and we can take `i'` out of the sum and replace `i'` with `i` everywhere:

.. math::

   \frac{\partial f}{\partial \gamma_i} &= \sum_{j'} \frac{\partial f}{\partial \tilde{z}_{ij'}} \frac{\partial \tilde{z}_{ij'}}{\partial \gamma_i} \\
                                        &= \boxed{ \sum_{j'} \frac{\partial f}{\partial \tilde{z}_{ij'}}  \hat{z}_{ij'} }

Or in Python::

    dgamma = np.sum(dZtilde * Zhat, axis=1, keepdims=True)


Derivation: `\partial f / \partial \beta_i`
-------------------------------------------

This one is easy. Following the same logic as above,

.. math::

   \frac{\partial f}{\partial \beta_i} &= \sum_{j'} \frac{\partial f}{\partial \tilde{z}_{ij'}} \frac{\partial \tilde{z}_{ij'}}{\partial \beta_i} \\
                                       &=  \boxed{ \sum_{j'} \frac{\partial f}{\partial \tilde{z}_{ij'}} }

In Python::

    dbeta = np.sum(dZtilde, axis=1, keepdims=True)


Derivation: `\partial f / \partial z_{ij}`
------------------------------------------

First, get the derivative with respect to `\hat{z}_{ij}`:

.. math::

   \frac{\partial f}{\partial \hat{z}_{ij}} &= \sum_{i'j'} \frac{\partial f}{\partial \tilde{z}_{i'j'}} \frac{\partial \tilde{z}_{i'j'}}{\partial \hat{z}_{ij}} \\
                                            &= \sum_{i'j'} \frac{\partial f}{\partial \tilde{z}_{i'j'}}  \delta_{ii'} \delta{jj'} \gamma_i' \\
                                            &= \boxed{ \frac{\partial f}{\partial \tilde{z}_{ij}} \gamma_i }

In Python::

    dZhat = dZtilde * gamma

Now, **the final and most tedious part**: given `\partial f / \partial \hat{z}_{ij}`, go the rest of the way.

.. math::
   \frac{\partial f}{\partial z_{ij}} = \sum_{i'j'} \frac{\partial f}{\partial \hat{z}_{i'j'}} \frac{\partial \hat{z}_{i'j'}}{\partial z_{ij}}


Changing `z_{ij}` has no effect on `\hat{z}_{i'j'}` for `i' \ne i`.
Or in other words, `\frac{\partial \hat{z}_{i'j'}}{\partial z_{ij}} = 0` for `i' \ne i`.
So, only terms with `i' = i` actually contributes to the sum `\sum_{i'j'}`, and we can take `i'` out of the sum and replace `i'` with `i` everywhere:

.. math::
   \frac{\partial f}{\partial z_{ij}} = \sum_{j'} \frac{\partial f}{\partial \hat{z}_{ij'}} \frac{\partial \hat{z}_{ij'}}{\partial z_{ij}}


Substitute in the equation for `\hat{z}_{ij}`:

.. math::
   \frac{\partial f}{\partial z_{ij}} = \sum_{j'=1}^m \frac{\partial f}{\partial \hat{z}_{ij'}} \frac{\partial}{\partial z_{ij}} \left( (z_{ij'} - \mu_i)(\sigma_i^2 + \epsilon)^{-1/2} \right)

Expand the parital:

.. math::
   \frac{\partial f}{\partial z_{ij}} = \sum_{j'=1}^m \frac{\partial f}{\partial \hat{z}_{ij'}} \left( \frac{\partial z_{ij'}}{\partial z_{ij}} (\sigma_i^2 + \epsilon)^{-1/2} - \frac{\partial \mu_i}{\partial z_{ij}} (\sigma_i^2 + \epsilon)^{-1/2} - \frac{1}{2} (z_{ij'} - \mu_i)(\sigma_i^2 + \epsilon)^{-3/2} \frac{\partial \sigma_i^2}{\partial z_{ij}} \right)

For the first term, we realize that `\partial z_{ij'} / \partial z_{ij}` is 1 if `j' = j`, otherwise 0, so we can replace it with `\delta_{j,j'}`:

.. math::
   \frac{\partial z_{ij'}}{\partial z_{ij}} = \delta_{j, j'}

For the second and third terms, we will need `\partial \mu_i / \partial z_{ij}` and `\partial \sigma_i^2 / \partial z_{ij}`. Substituting in the equations for `\mu_i` and `\sigma_i^2`,

.. math::
   \frac{\partial \mu_i}{\partial z_{ij}}      &= \frac{1}{m} \sum_{j'=1}^m \frac{\partial z_{ij'}}{\partial z_{ij}} = \frac{1}{m} \\
   \frac{\partial \sigma_i^2}{\partial z_{ij}} &= \frac{2}{m} \sum_{j'=1}^m (z_{ij'} - \mu_i)\left(\frac{\partial z_{ij'}}{\partial z_{ij}} - \frac{\partial \mu_i}{\partial z_{ij}} \right) \\
                                               &= \frac{2}{m} \sum_{j'=1}^m (z_{ij'} - \mu_i) \delta_{j,j'} - \frac{2}{m} \sum_{j'=1}^m  (z_{ij'} - \mu_i) \frac{1}{m} \\
                                               &= \frac{2}{m} (z_{ij} - \mu_i) - \frac{2}{m^2} \Big( \sum_{j'=1}^m  z_{ij'} - \sum_{j'=1}^m \mu_i \Big) \\
                                               &= \frac{2}{m} (z_{ij} - \mu_i) - \frac{2}{m^2} (m \mu_i - m \mu_i) \\
                                               &= \frac{2}{m} (z_{ij} - \mu_i)


Plug these intermediate partial derivatives back into our main equation and then simplify:

.. math::
   \frac{\partial f}{\partial z_{ij}} &= \sum_{j'=1}^m \frac{\partial f}{\partial \hat{z}_{ij'}} \left( \delta_{j,j'} (\sigma_i^2 + \epsilon)^{-1/2} - \frac{1}{m} (\sigma_i^2 + \epsilon)^{-1/2} - \frac{1}{2} (z_{ij'} - \mu_i)(\sigma_i^2 + \epsilon)^{-3/2} \left(\frac{2}{m}\right)(z_{ij} - \mu_i) \right) \\
                                      &= \frac{\partial f}{\partial \hat{z}_{ij}} (\sigma_i^2 + \epsilon)^{-1/2} - \frac{1}{m} \sum_{j'=1}^m \frac{\partial f}{\partial \hat{z}_{ij'}}  (\sigma_i^2 + \epsilon)^{-1/2} - \frac{1}{m} \sum_{j'=1}^m \frac{\partial f}{\partial \hat{z}_{ij'}} (z_{ij'} - \mu_i)(\sigma_i^2 + \epsilon)^{-3/2} (z_{ij} - \mu_i)

Realizing that some expressions in the last term can be replaced by `\hat{z}_{ij}` and `\hat{z}_{ij'}`, we finally get

.. math::
   \boxed{ \frac{\partial f}{\partial z_{ij}} = \frac{1}{m \sqrt{\sigma_i^2 + \epsilon}} \left( m \frac{\partial f}{\partial \hat{z}_{ij}} - \sum_{j'=1}^m \frac{\partial f}{\partial \hat{z}_{ij'}} - \hat{z}_{ij} \sum_{j'=1}^m \frac{\partial f}{\partial \hat{z}_{ij'}} \hat{z}_{ij'} \right) }


In Python::

    mu = np.mean(Z, axis=1, keepdims=True)
    sigma2 = np.mean((Z - mu)**2, axis=1, keepdims=True)
    dZ = (1. / (m * np.sqrt(sigma2 + epsilon))
             * (m * dZhat
                - np.sum(dZhat, axis=1, keepdims=True)
                - Zhat * np.sum(dZhat * Zhat, axis=1, keepdims=True)))
