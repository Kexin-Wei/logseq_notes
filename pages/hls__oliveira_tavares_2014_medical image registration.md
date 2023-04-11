file:: [oliveira_tavares_2014_medical image registration.pdf](file://D:/Dropbox/Study/ZoteroFiles/oliveira_tavares_2014_medical image registration.pdf)
file-path:: file://D:/Dropbox/Study/ZoteroFiles/oliveira_tavares_2014_medical image registration.pdf

- [:span]
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63b53b34-1445-414f-832f-0547d8e3b9ae
  hl-type:: area
  hl-stamp:: 1672821554995
- The main idea is to search iteratively for the geometric transformation that, when applied to the moving image, optimises i.e. minimises or maximises a similarity measure, also known as the cost function. The similarity measure is related to voxel intensity and is computed in the overlapped regions of the input images. The optimiser has the function of defining the search strategy. The aim of the interpolator is to resample the voxel intensity into the new coordinate system according to the geometric transformation found.
  ls-type:: annotation
  hl-page:: 4
  hl-color:: blue
  id:: 63b53bab-5725-4aba-a874-7ba0a43dca3c
- feature-based registration
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63b53cf2-013a-4450-8c73-31e16ee07f92
- (1) the matching among features is established using some criterion
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63b53d01-82f8-4777-9984-47394c65de69
- (2) The matching and the transformation are defined concurrently based on the optimisation of a similarity measure between the features extracted from the input images
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63b53d0b-0e9f-49ec-9df6-5c612e6c6ac4
- [:span]
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63b53d59-ec25-4a48-99ab-55c6d48a24d7
  hl-type:: area
  hl-stamp:: 1672822104506
- The non-rigid transformation class includes the similarity transformation (translation, rotation and uniform scaling), affine (translation, rotation, scaling and shear), projective and curved.
  ls-type:: annotation
  hl-page:: 5
  hl-color:: yellow
  id:: 63b53d75-5cb2-4e2f-a93a-99d043bb7c8a
- The curved transformation is also commonly referred to as a deformable, elastic or fluid transformation.
  ls-type:: annotation
  hl-page:: 5
  hl-color:: yellow
  id:: 63b53d80-d83e-47fc-848a-0736435f62a9
- According to the literature, a rigid geometric transformation is mainly applied in two situations. One is in the registration of rigid structures, such as bones
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63b53d94-8237-4465-a802-1f341e64878a
- the other is in pre-registration before a more complex geometric transformation
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63b53d9c-5f8e-44af-8183-eda16cef7f2a
- The affine transformations, both rigid and non-rigid, have been used in the registration of ultrasound images(Meyer et al. 1999; Roche et al. 2001; Shekhar and Zagrodsky 2002; Shekhar et al. 2004; King et al. 2010), since the low resolution and low signal-to-noise ratio of the ultrasound images make the accurate registration difficult when more complex transformations are used.
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63b53dd4-3f19-40d5-8706-42a124f26d20
- Most approaches for medical image registration are based on curved transformations, since the almost all anatomical parts, or organs, of the human body are, in fact, deformable structures
  ls-type:: annotation
  hl-page:: 6
  hl-color:: blue
  id:: 63b53df8-1e54-471d-bf50-9eddb3645d70
- Basically, two kinds of curved deformations have been used in medical image registration: free-form transformations, in which any deformation is allowed; and guided deformations, in which the deformation is controlled by a physical model that has taken into account the material properties, such as tissue elasticity or fluid flow
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63b53e31-bf65-4c50-81f4-54f5df0445eb
- In many free-form deformation models, a grid of control points is defined in order to determine the deformation involved. The points of such a grid are moved individually in the direction that optimises the similarity measure, defining local deformations.
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63b53e7b-b926-43b8-9832-22cf825b21b4
- Transformation between control points is propagated by interpolation; for example, using linear interpolation (Kjems et al. 1999) or other convex kernels (Gaens et al. 1998; Lo ̈tjo ̈nen and Ma ̈kela ̈ 2001). The most popular interpolator used for freeform deformation is probably the cubic B-spline (Rueckert et al. 1999; Studholme et al. 2000; Rohlfing and Maurer2001; Rohlfing et al. 2003; Kybic and Unser 2003; Mattes et al. 2003; Kabus et al. 2004; Xie and Farin 2004; Balci et al. 2007; Bhagalia et al. 2009; Bai and Brady 2011; Khader and Hamza 2011); but, B-splines of other degrees can also be used (Loeckx et al. 2010).
  ls-type:: annotation
  hl-page:: 6
  hl-color:: purple
  id:: 63b53e8f-80c7-4dba-8bce-cf5446934188
- Other elastic-based registration methods are based on finite element models
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63b53eb1-1100-4b81-a37b-a82bd43b7057
- Thin-plate splines (TPS)-based registration methodologies are also based on deformable solid properties;
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63b53edb-3da9-41a8-890d-bd12b4a92aa1
- In these methodologies, a set of control points is moved along the direction that optimises the similarity measure used. The propagation of the deformation to the neighbours of the control points is defined by the thin-plate model.
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63b53ee9-820d-452f-bf08-f1f828515584
- The deformable registrations based on TPS are global, that is, when a control point is moved, its new position affects the whole deformation. The registrations based on free-form B-spline deformations are local; however, they also can be classified between a global registration model and a pure local model, since their locality can be controlled by varying the grid or mesh spacing and consequently the number of degrees-of-freedom. Since the free-form B-spline deformations are local, it is essential to correct the global misregistration before computing the deformation involved, for instance, using an affine transformation (Rueckert et al. 1999).
  ls-type:: annotation
  hl-page:: 7
  hl-color:: purple
  id:: 63b53f09-5fe3-47ff-b61f-6bb8bcdbedf5
- In flow-based registration algorithms, the registration problem is addressed as a motion problem. 
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63b53f18-b27b-4b7f-8b35-2efc88a35dff
- Flow-based registration algorithms can be divided into two classes: fluid flow and optical flow
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63b53f22-c28c-451d-b99b-fb2b6286a853
- The well-known demons algorithm and its variations(Thirion 1998; Guimond et al. 2001, 2002; Wang et al.2005; Vercauteren et al. 2007; 2009; Yeo et al. 2010a; Gooya et al. 2011) are examples of optical flow-based registration algorithms.
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63b53f35-e5f2-4c8c-ba7f-9e8101433886
- Other examples of optical flowbased algorithms can be found in Hellier et al. (2001), Tosun and Prince (2008).
  ls-type:: annotation
  hl-page:: 7
  hl-color:: purple
  id:: 63b53f40-5b5e-4e7a-88ce-4da78b47b3fd
- The registration algorithms based on B-splines address the image deformations as a combination of basic functions, particularly the B-splines, but other basis functions have also been used (Friston, Ashburner, et al.1995; Ashburner and Friston 1999).
  ls-type:: annotation
  hl-page:: 7
  hl-color:: purple
  id:: 63b53f57-3d62-424b-8f40-ba840a5308d7
- The similarity measures here are divided into two classes, the intensity- and feature-based methods
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63b53f82-b396-41f5-a716-27fc97ea7ada
- Normally, the similarity measure used for deformable image registration is composed of at least two terms: one related to the voxel intensity or structures similarity, and the other one to the deformation field (
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63b53f8c-2f46-44a1-be81-67f3e5f0a85e
- The measures based on the intensity difference are usually based on the sum of squared differences (SSD) or their normalisations
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63b53fa8-00d1-4d79-a9f5-5fe20e1cf214
- The cross-correlation and its derived measures, such as the Pearson’s correlation coefficient or correlation ratio, have also been used as image similarity measures
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63b53faf-cbed-4f26-8cad-4716f21d7032
- The information theory based similarity measures are mostly based on the mutual information (MI) or derived measures. 
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63b53fc3-5617-4267-b30a-5a2e7a702a97
- The SSD, the cross-correlation and their variants are similarity measures appropriate for monomodal image registration.
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63b53fcd-b03f-4ff6-92f2-f3eb36ccba61
- residual complexity
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63b53fd9-c16b-44ba-aaa6-8b894635263c
- The MI is based on the Shannon entropy that is computed from the joint probability distribution of the image voxel intensity.
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63b53fed-0e96-4220-aa22-b43a4b84ed7f
- MI registration has received so much attention that, a few years after being proposed for image registration, a state-ofthe-art image registration based on MI was presented in Pluim et al. (2003) addressing almost 200 works on that topic. 
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63b53fff-5448-4da2-a89e-3e8745d2794c
- It should be noted that the low registration accuracy based on the affine transformation is because this kind of transformation cannot model the image deformation adequately and not because of the similarity measure used. 
  ls-type:: annotation
  hl-page:: 8
  hl-color:: red
  id:: 63b54026-4e62-41c7-91e3-a8c54169cbd5
- MI has proven to be a very robust and reliable similarity measure for intensity-based registration of multimodal images. 
  ls-type:: annotation
  hl-page:: 9
  hl-color:: yellow
  id:: 63b54054-4d00-4cd6-8981-516913114ab6
- Re ́ny’s entropy
  ls-type:: annotation
  hl-page:: 10
  hl-color:: purple
  id:: 63b5407a-4dae-419f-9504-da54bc29757d
- Havrda-Charvat’s entropy
  ls-type:: annotation
  hl-page:: 10
  hl-color:: purple
  id:: 63b54083-fcbc-4bc5-8e7b-c9ae7de4c267
- joint intensity distribution,
  ls-type:: annotation
  hl-page:: 10
  hl-color:: purple
  id:: 63b54096-3586-41f2-8e44-0e2349528d62
- For spatial distance, the Euclidean distance is a common choice.
  ls-type:: annotation
  hl-page:: 10
  hl-color:: yellow
  id:: 63b540e7-4353-435e-bf6e-7f465f8f1836
- n-dimensional function, where n is the number of degrees-offreedom of the transformation involved
  ls-type:: annotation
  hl-page:: 10
  hl-color:: yellow
  id:: 63b54113-22fc-49cd-acda-05effbfb0777
- Powell’s method
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b54139-c467-4242-b3c0-c17bee98290e
- the downhill simplex method
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b54144-c646-44f0-877b-5fe8afd6cb34
- the Levenberg-Marquard
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b5414b-0064-4521-9463-a92fc1675ac2
- the gradient ascent or descent
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b54150-4f57-42da-9fd1-b1c60a6a34a9
- the quasi-Newton
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b54155-cd45-4b29-bd99-5e8a85c2642d
- the stochastic algorithms
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b5415d-afb3-4cd8-98fb-a8bb65c7acf3
- evolutionary algorithm
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b54165-aa1b-4d58-a8cd-726bd64c9532
- The minimisation problem is frequently converted into a problem of solving a set of partial differential equations
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b5417e-b163-47dd-9cf2-6a35ce4d9e61
- Some authors have used the support vector machine(SVM) technique in their image registration algorithms(Zhang et al. 2005; Qi et al. 2008). These algorithms are frequently based on prior information obtained from the joint intensity distribution between two or more registered images
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b54194-a70b-43c1-b17e-e329baf96f69
- Generally, the similarity measure as a function is not smooth, as it contains many local extremes. Some of these local extremes represent local best solutions, but others are a consequence of the approach implemented, such as interpolation imperfections and lack of robustness of the similarity measure.
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b541b3-9bdb-4820-bf9b-ffbdbede1c6a
- The iterative optimisation algorithms are frequently implemented with a multi-resolution or pyramidal strategy.
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b541c6-3d70-4954-a018-fccb38f0f49a
- This strategy uses a coarse-to-fine approach. Usually, the process starts by defining a pair of image pyramids that are used to down-sample the fixed and moving images. 
  ls-type:: annotation
  hl-page:: 11
  hl-color:: blue
  id:: 63b541d7-154a-47f9-82d2-b872b82f3115
- Procrustes method
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b54200-1957-4f11-87e3-9b020bc0f022
  hl-stamp:: 1672823306462
- point correspondence-based registration algorithms
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b6236f-3b74-494c-adfc-d2ce89f899fa
- it is necessary to evaluate the image intensity at the new mapped position. The goal of the interpolation step is to estimate the intensity at that new position.
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b624c0-0a6e-4864-9aca-a88ea5ed57b2
- The interpolation solution used can affect the accuracy and speed of the registration process
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b62677-efed-45b3-b6da-fdf86792309d
- nearest neighbour or linear interpolation
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b6268f-bbd2-46b3-9d96-91a569ff91de
- higher quality is used to obtain the final registered image, such as the ones based on cubic B-spline or windowed sinc interpolators.
  ls-type:: annotation
  hl-page:: 11
  hl-color:: yellow
  id:: 63b626a0-538d-42b5-af5e-7eb83a939e26
- An initial pre-registration can be defined manually by the user or by a fully automated approach using, for example, image moments as in Itti et al. (1997), Pan et al. (2011).
  ls-type:: annotation
  hl-page:: 12
  hl-color:: purple
  id:: 63b6270a-acd4-40a7-87cf-32fe98c61590
  hl-stamp:: 1672881934075
- Several image segmentation techniques exist, which can be broadly classified as region or border based. Examples of region-based techniques are: thresholding methods (Wellner1993; Otsu 1979), watershed (Beucher 1991; Grau et al.2004) and region growing (Adams and Bischof 1994)
  ls-type:: annotation
  hl-page:: 12
  hl-color:: yellow
  id:: 63b62b88-1c99-4900-bd02-0ea1fa266c8a
- Reviews on image segmentation techniques can be found in Gonzalez and Woods (2008), Ma, Zhen et al. (2010), Monteiro (2007), Zhang and Lu (2004), Zhang (2001).
  ls-type:: annotation
  hl-page:: 12
  hl-color:: purple
  id:: 63b62c82-5fc2-4200-8f6a-9bf35056e73b
- In the intensity-based registration methodologies previously referred to, a dense matching is automatically established based on the geometric transformation found. However, in this section, the matching between the features extracted from both input images is considered sparse.
  ls-type:: annotation
  hl-page:: 12
  hl-color:: yellow
  id:: 63b62d4c-8183-4f87-97a5-8d94ad1cf865
- For the iterative matching optimisation, besides the optimisation algorithms previously indicated, common algorithms are the ICP (Besl and McKay 1992) and its variations (Stewart et al. 2003; Andreetto et al. 2004; Giessen et al. 2009; Tsai et al. 2010; Pan et al. 2011).
  ls-type:: annotation
  hl-page:: 12
  hl-color:: yellow
  id:: 63b62d91-7539-42b3-8b95-983ef77bb69c
- The HAMMER algorithm (Shen and Davatzikos 2002) establishes the matching in a similar fashion to the freeform deformation, that is, based on a local search for the best matchin
  ls-type:: annotation
  hl-page:: 12
  hl-color:: yellow
  id:: 63b62d9b-df29-4ddd-8171-e0e14154a799
- Dedicated optimisation solutions can be used to establish the matching among features, such as self-organising maps (Matsopoulos et al. 2004), simulated annealing(Bayro-Corrochano and Rivera-Rovelo 2009), quasiorientation maps (Wong et al. 2006), approaches based on the Procrustes method (Rangarajan et al. 1997; Hill and Batchelor 2001), fuzzy clustering (Tarel and Boujemaa1999), homothetic boundary mapping (Davatzikos et al.1996) or contours mapping via dynamic programming(Oliveira and Tavares 2008).
  ls-type:: annotation
  hl-page:: 12
  hl-color:: yellow
  id:: 63b62ecf-7cd8-437f-8740-a1ffa2f8dc58
- In some matching algorithms, before the computation of the optimal geometric transformation, it is important to consider an algorithm to remove outlier matches
  ls-type:: annotation
  hl-page:: 12
  hl-color:: yellow
  id:: 63b62f0c-487f-4e68-9242-a56802d0b968
- The SSD and cross-correlation-based similarity measures can be efficiently evaluated in the frequency domain using the Fourier transform and its properties.
  ls-type:: annotation
  hl-page:: 13
  hl-color:: yellow
  id:: 63b62f21-e68f-4f18-b923-85a0053a15f7
- The image registration techniques based on the optimisation of the SSD and cross-correlation in the frequency domain can be clearly classified as intensity based; however, since the computation is done in the frequency domain, they have been included in this category.
  ls-type:: annotation
  hl-page:: 13
  hl-color:: yellow
  id:: 63b62f7d-2ba6-479c-8ba2-17e14b1b6e4c
- Various authors have combined two or more registration methodologies/strategies in their algorithms (Davatzikos et al. 1996; Christensen et al. 1997; Kim et al. 2003; Andreetto et al. 2004; Auer et al. 2005; Chen et al. 2010; Liao et al. 2011). Some use feature- and intensity-based registration methodologies concurrently. 
  ls-type:: annotation
  hl-page:: 13
  hl-color:: yellow
  id:: 63b62fbe-b1ed-40b0-8ff5-dd9990ae613c
- A common solution is the use of a feature-based algorithm for a coarse registration and then the use of an intensity-based methodology for a fine registration as described in Chen et al. (2010), Liao et al. (2011), Oliveira and Tavares (2011), Postelnicu et al. (2009). 
  ls-type:: annotation
  hl-page:: 13
  hl-color:: yellow
  id:: 63b62fc7-0b49-4136-bcd4-5b4364741254
- In Christensen et al. (1997), the registration is established in two steps. First, the global transformation is determined by using a low-dimensional elastic model; then, the local higher deformation is obtained using the Navier-Stokes fluid model. 
  ls-type:: annotation
  hl-page:: 13
  hl-color:: yellow
  id:: 63b630c8-e57f-467d-9aec-e54af5f4c56e
- On the other hand, in Auer et al.(2005), a coarse initial registration is defined by maximising the MI using the Powell’s method combined with a multi-resolution strategy, and then a fine pointbased registration is accomplished using an elastic TPS.
  ls-type:: annotation
  hl-page:: 13
  hl-color:: yellow
  id:: 63b630cb-6822-45e2-b86e-2810292bf49b
- However, most similarity measures frequently used have no geometric/physical significance.
  ls-type:: annotation
  hl-page:: 14
  hl-color:: yellow
  id:: 63b630f0-1742-4126-9f58-aa75ad558f44
- An approach closely related to the later is based on synthesising images by simulating the imaging acquisition physics or/and material properties and then evaluating the registration algorithm on the synthetic images produced.
  ls-type:: annotation
  hl-page:: 14
  hl-color:: yellow
  id:: 63b6310e-d3a7-44c1-9eb4-bfa2e27f1ada
- Other more reliable solutions are by manually identifying a set of corresponding points in both input images, e.g. fiducial markers placed into the patients or the organs, and use them to assess the registration accuracy
  ls-type:: annotation
  hl-page:: 14
  hl-color:: red
  id:: 63b63265-1fc8-4c79-b986-4b3639d30715
  hl-stamp:: 1672884842798
- The target registration error is an important measure of the accuracy of the performed registration. It evaluates the registration accuracy based on points correspondence. Since its value is given in terms of Euclidean distance between the corresponding points, it has an immediate physical meaning
  ls-type:: annotation
  hl-page:: 14
  hl-color:: yellow
  id:: 63b632e2-96fb-4aee-8709-af595f85df16
- A solution to overcome this limitation is proposed in Yeo et al. (2010b).
  ls-type:: annotation
  hl-page:: 14
  hl-color:: purple
  id:: 63b68783-965b-4d64-9efc-fb56f10d1f5c
- Registration methodologies are also commonly classified using the feature space image information. This information may be the intensity of the raw voxels, the intensity gradient, statistical information related to the voxel intensity or structures extracted from the images to be registered, such as, sets of points, edges, contours, graphs, surfaces and volumes.
  ls-type:: annotation
  hl-page:: 4
  hl-color:: yellow
  id:: 63b53aaa-b680-4dee-a9a3-b34860c6827c