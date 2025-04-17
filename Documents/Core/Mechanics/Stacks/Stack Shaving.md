# Stack Shaving
Stacked units have quantized pools of health according to their stack level.

For example:
A unit has 2 health.
A four stack (4stk) of this unit would have 8 health.

You can then visualise this unit as having 4 distinct health pools of 2hp each.

When a unit takes enough damage such that they would have sustained damage equal to 1x their base stat HP (i.e. 2hp),\
then that unit will now lose one of their stacks.\
Put more simply, whenever they lose enough health that they would deplete a pool of HP, they lose that stack.

So to illustrate:

A 4stk unit has 8hp.
* It takes 4dmg.
* It is now a 2stk unit with 4hp.

A 4stk unit has 8hp.
* It takes 3dmg.
* It is now a 3stk unit with 5hp.

Currently calculating the stacks lost will be done with this function.
```math
\begin{aligned}
&\text{int } \text{stacksLost} = 0; \\
&\text{if (healthLost > baseHealthValue)} \\
&\quad \text{stacksLost} = \left\lfloor \frac{\text{healthLost}}{\text{baseHealthValue}} \right\rfloor; \\
&\text{if ((currentHealth - healthLost) \% \text{baseHealthValue} == 0)} \\
&\quad \text{stacksLost} += 1; \\
&\text{return } \text{stacksLost};
\end{aligned}
```