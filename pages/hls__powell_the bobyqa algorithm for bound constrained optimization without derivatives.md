file:: [powell_the bobyqa algorithm for bound constrained optimization without derivatives.pdf](file://D:/Dropbox/Study/ZoteroFiles/powell_the bobyqa algorithm for bound constrained optimization without derivatives.pdf)
file-path:: file://D:/Dropbox/Study/ZoteroFiles/powell_the bobyqa algorithm for bound constrained optimization without derivatives.pdf

- No derivatives of F are required.
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63be2963-5688-414c-9837-9e4f8072d815
- objective function F (x), x ∈ Rn, subject to the simple bounds ai ≤ xi ≤ bi, i = 1, 2, . . . , n,
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63be2975-ab65-45dd-a7b8-7c1b00acaece
- The method of BOBYQA is iterative, k and n being reserved for the iteration number and the number of variables,
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63be2c5b-e8f2-4946-98f3-953021bcc29d
- we reserve m for the number of interpolation conditions that are imposed on a quadratic approximation Qk(x), x ∈ Rn, to F (x), x ∈ Rn.
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63be2c7c-e94c-407f-8236-d145df3fce4b
- Qk(yj ) = F (yj ), j = 1, 2, . . . , m,
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63be2c82-3819-4749-bf5c-1391303e5253
- m is a constant integer from the interval [n+2, 12 (n+1)(n+2)], chosen by the user of the software.
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63be2c8a-b377-4dcb-a34a-af4b9e72451b
- These features without the restrictions (1.1) are taken from the NEWUOA software (Powell, 2006) for unconstrained optimization without derivatives, as are several other features that receive attention later.
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63be316b-2f89-4b96-a042-ce6d53aa055a
- x = xk +dk
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63be317b-539e-42a9-9d72-1019c2176e77
- If certain conditions are achieved, as specified later, then termination occurs on the k-th iteration.
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63be3184-5d24-46e0-af5a-597b98cf1ca8
- he new function value F (xk+dk) is calculated, and one of the interpolation points, yt say, is replaced by xk+dk, where yt is different from xk.
  ls-type:: annotation
  hl-page:: 2
  hl-color:: yellow
  id:: 63be3195-d978-40f3-8fd7-dedfbb29d4dd
- In these cases, if F is twice differentiable, one cannot expect ∇2Qk to become a good approximation to ∇2F (x∗), F being far too small.
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63be31e3-a777-4fc0-8337-a3150a553bd6
- provide an initial vector of variables x0 ∈ Rn and the initial trust region radius ∆1, in addition to the bounds of expression (1.1) and the value of m. 
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63be3482-43b5-48ac-8922-641790c99c69
- [:span]
  ls-type:: annotation
  hl-page:: 5
  hl-color:: yellow
  id:: 63be356f-02ba-4c19-83ad-3e949c77f6c4
  hl-type:: area
  hl-stamp:: 1673409901765
- The function values F (yj ), j = 1, 2, . . . , min[m, 2n+1], are calculated.
  ls-type:: annotation
  hl-page:: 5
  hl-color:: yellow
  id:: 63be357f-2604-4d9e-a2c1-3b2e4463dbb8
- yi+1 and F (yi+1) are exchanged with yn+i+1 and F (yn+i+1) for all integers i in [1, n] that satisfy both ai < (x0)i < bi and F (yn+i+1) < F (yi+1), which provides a bias towards lower values of F in the following construction.
  ls-type:: annotation
  hl-page:: 5
  hl-color:: yellow
  id:: 63be371b-bb89-4081-a712-cc03fe340809
- first quadratic model
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63be4be7-bd3e-432c-88e1-c1ef362ea5c9
- [:span]
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63be4bf5-dca6-4039-8fa1-7e864fbda289
  hl-type:: area
  hl-stamp:: 1673415668521
- (g0)i is defined by Q1(x0) = F (y1) and Q1(yi+1) = F (yi+1)
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63be4cb3-4569-4ee1-99b8-a0bb0346303a
- he inverse of the matrix of a linear system of equations is employed on each iteration to assist the calculation of the next quadratic model Qk+1 from Qk
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63be4d02-3107-4077-bdf3-079418bb924e
- This increase in generality preserves the validity of every statement in the paragraph that includes equation (2.5).
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63be5a22-dba9-45cc-b9da-87d476761b3a
- hus BOBYQA postpones the use of short steps, because smaller steplengths ‖dk‖ in the conditions Qk+1(xk) = F (xk) and Qk+1(xk +dk) = F (xk +dk) tend to increase the damage to Qk+1 from various possible errors.
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63be5b1c-19e3-49bb-b9b3-b95ca27249ce
- The calculation of the “trust region” step dk is done by subroutine TRSBOX of BOBYQA
  ls-type:: annotation
  hl-page:: 9
  hl-color:: yellow
  id:: 63be5b75-8acf-4b71-87e3-4f49d7ad1a19
- [:span]
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63be5bbf-025b-434a-956d-4079c869c214
  hl-type:: area
  hl-stamp:: 1673419708870
- a quadratic function of n variables has 12 (n+1)(n+2) degrees of freedom.
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63bf986f-d479-4509-bec6-f8c0274fccc6
- optimization without derivatives that employ quadratic models, and that take up the freedom in Qk+1 by minimizing ‖∇2Qk+1 −∇2Qk‖F , after satisfying the interpolation conditions (1.5) with ∇2Qk+1 symmetric.
  ls-type:: annotation
  hl-page:: 3
  hl-color:: yellow
  id:: 63bf98be-bcc8-4ce7-a1ac-ccb68ff172a0
- The change Qk+1 − Qk to the quadratic model is defined by an (m+n+1)×(m+n+1) system of linear equations, which is solved in only O(m2) operations
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63bf9964-d741-458f-8342-d336d261bc2b
- he purpose of the second example is to show the robustness and some limitations of BOBYQA in a difficult case where F has several local minima
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63bf99c7-fe18-4cfe-a03e-c638462269ea
- the problem of calculating the new quadratic model Qk+1 from Qk, when Qk+1 has to satisfy the interpolation conditions (1.5), and when the remaining freedom in Qk+1 is taken up by requiring ∇2Qk+1 to be the symmetric matrix that minimizes the Frobenius norm ‖∇2Qk+1−∇2Qk‖F , the matrix ∇2Qk being symmetric.
  ls-type:: annotation
  hl-page:: 14
  hl-color:: yellow
  id:: 63bfaf5b-94d8-40e5-a198-8f8981fed805
- [:span]
  ls-type:: annotation
  hl-page:: 14
  hl-color:: yellow
  id:: 63bfb016-9461-418a-984b-07e43215d3f1
  hl-type:: area
  hl-stamp:: 1673506837158
- Next we address the claim that expression (3.9) is the denominator of the updating formula (4.9) in the case x+ = xk +dk
  ls-type:: annotation
  hl-page:: 18
  hl-color:: yellow
  id:: 63bfb1ad-01ea-4bf7-a64e-d33565ef7f88
- f BOBYQA and NEWUOA is to avoid severe inefficiencies if the elements of ∇2Qk are much too large. For example, large second derivatives may be inherited from the initial model Q1 if F (x), x ∈ Rn, increases at a fast exponential rate in some regions of Rn, and if the initial vector of variables x0 is in such a region and far from a local minimum. Extra help may be needed to reduce ‖∇2Qk‖, because in general the change ‖∇2Qk+1−∇2Qk‖F is31 as small as possible subject to the new interpolation conditions (1.5). Therefore, after the calculation of F (xk + dk) on a “trust region” iteration, and after the updating of Section 4 is complete, the new quadratic model Qk+1 is compared with Q alt k+1(x), x ∈ Rn, say, which is the quadratic that minimizes ‖∇2Q alt k+1‖F subject to Q alt k+1(̂yj ) = F (̂yj ), j = 1, 2, . . . , m. By employing the current inverse matrix H of expression (2.7), the parameters of Q alt k+1 are generated in only O(m2) operations, including the gradient ∇Q alt k+1(xk+1). For any g ∈ Rn, let Pg be the vector in Rn that, for i = 1, 2, . . . , n, has the i-th component min [0, gi], gi or max [0, gi] in the cases (xk+1)i = ai, ai < (xk+1)i < bi or (xk+1)i = bi, respectively. We expect‖P∇Qk+1(xk+1)‖ to be much smaller than ‖P∇Q alt k+1(xk+1)‖ when the iterations are making good progress, but the ordering tends to be reversed if ‖∇2Qk+1‖ is huge. Therefore Qk+1 is replaced by Q alt k+1 if the condition‖P∇Q alt k+1(xk+1)‖2 ≤ 0.1 ‖P∇Qk+1(xk+1)‖2 (6.12) holds on three consecutive iterations that take “trust region” steps, regardless of any intermediate “alternative” iterations. The factor 0.1 provides some reluctance to make the change, because it it is hardly ever worthwhile to interrupt the usual method of BOBYQA.
  ls-type:: annotation
  hl-page:: 31
  hl-color:: yellow
  id:: 63bfb3ab-4699-4d8f-ad94-7321c67b440b