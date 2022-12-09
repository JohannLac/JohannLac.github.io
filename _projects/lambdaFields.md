---
title: "Safe navigation in occupancy grids"
excerpt: "Safe navigation with physics-oriented risks metrics<br/><img src='/images/projects/LF/preview.jpg'>"
collection: projects
year: 2018
---

This project aimed at developing a novel occupancy grid framework for safe navigation.
The central motivation comes from the fact that it is not possible, using standard Bayesian occupancy grids, to infer a meaningful risk for a continuous path in the environment.

As such, we proposed a method to map the environment not with the probability of occupancy, but with the density of possible collisions.
This novel formulation lead to a heavily generalizable framework where any physical risk can be inferred (e.g., loss of kinetic energy).

For instance, the framework allows the robot to navigate in unstructured environments such as tall grass: given a probabilistic information of the obstacles' mass in front of the robot, it can either choose to go through the grass or to go around.
Such decision can be motivated by the mass of the robot itself, the confidence about the grass not hiding any hazardous obstacles, and so on.

![crossroad picture](/images/projects/LF/robot_tallgrass.jpg)

The framework have been extended to dynamic environments, where the risk inference can once again help taking meaningful decisions in case of hazardous scenarios.

![crossroad picture](/images/projects/LF/crossroads.jpg)

References
------
1 - [Lambda-Field: A Continuous Counterpart of the Bayesian Occupancy Grid for Risk Assessment](https://scholar.google.fr/citations?view_op=view_citation&hl=en&user=cVFALvkAAAAJ&citation_for_view=cVFALvkAAAAJ:d1gkVwhDpl0C)\
Johann Laconte, Christophe Debain, Roland Chapuis, François Pomerleau, Romuald Aufrère\
2019 International Conference on Intelligent Robots and Systems (IROS)

2- [Dynamic Lambda-Field: A Counterpart of the Bayesian Occupancy Grid for Risk Assessment in Dynamic Environments](https://scholar.google.fr/citations?view_op=view_citation&hl=en&user=cVFALvkAAAAJ&citation_for_view=cVFALvkAAAAJ:Y0pCki6q_DkC)\
Johann Laconte, Elie Randriamiarintsoa, Abderrahim Kasmi, François Pomerleau, Roland Chapuis, Christophe Debain, Romuald Aufrère\
2019 International Conference on Intelligent Robots and Systems (IROS)

3- [A Novel Occupancy Mapping Framework for Risk-Aware Path Planning in Unstructured Environments](https://scholar.google.fr/citations?view_op=view_citation&hl=en&user=cVFALvkAAAAJ&citation_for_view=cVFALvkAAAAJ:YsMSGLbcyi4C)\
Johann Laconte, Abderrahim Kasmi, François Pomerleau, Roland Chapuis, Laurent Malaterre, Christophe Debain, Romuald Aufrère\
Sensors 2021

