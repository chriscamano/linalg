# Introduction to Linear Algebra: A Manim-Jupyter Series

Welcome to "Introduction to Linear Algebra," an interactive series of Jupyter notebooks crafted to build deep intuition for the concepts that form the bedrock of linear algebra. This course is inspired by Sheldon Axler's renowned textbook, "Linear Algebra Done Right," and aims to present these fundamental ideas in a visual and engaging format using Manim, a powerful mathematical animation library.
---
## Course Structure

The course is structured to provide a solid foundation in linear algebra while emphasizing understanding over rote memorization or an overemphasis on computation/ determinants. Each chapter corresponds to key concepts, with the first chapter dedicated to vector spaces.
---
## Setting Up the Environment

To run the notebooks efficiently, it is recommended to set up a dedicated Conda environment. Follow the steps below to create a new environment and install the required dependencies.

1. **Create a new Conda environment**:

   Open your terminal and run the following command to create a new Conda environment named `anim` with Python 3.10. You can replace `anim` with any name you prefer for your Conda environment.

```bash
conda create -n anim python=3.10
```
2. **Activate the Conda environment**:

After creating the new environment, activate it using the command below:
```bash
conda activate anim
```

3. **Install the package**:

With the environment activated, navigate to the root directory of the project where the `setup.py` file is located and run:
```bash
pip install .
```

This will install the package along with all the dependencies specified in the `setup.py` file.

Now your environment is set up, and you can start using the Jupyter notebooks for the linear algebra course.

---
### Chapter 1: Vector Spaces

- **1A: $\mathbb{R}^n$ and $\mathbb{C}^n$**
  - Introduction to real and complex number systems as they pertain to vector spaces.
- **1B: Definition of Vector Space**
  - Exploration of the axioms that define a vector space.
- **1C: Subspaces**
  - Investigation of subspaces, their properties, and their significance within vector spaces.

### Chapter 2: Finite-Dimensional Vector Spaces

- **2A: Span and Linear Independence**
  - Understanding the span of vectors and the concept of linear independence.
- **2B: Bases**
  - Defining bases and their role in vector space structure.
- **2C: Dimension**
  - Discussion of dimension and its implications for vector spaces.

## Learning Outcomes

By the end of this course, learners will be able to:

- Identify and understand the structure and properties of vector spaces.
- Visualize and solve problems related to span, linear independence, bases, and dimension.
- Apply linear algebra concepts to various fields such as computer science, physics, and engineering.

## Prerequisites

A basic understanding of algebra and calculus is recommended to get the most out of this course. Familiarity with Python and some prior exposure to mathematical proofs will be beneficial.

## Tools Used

- **Manim**: An animation engine for explanatory math videos. It's used here to visualize linear algebra concepts dynamically.
- **Jupyter Notebooks**: An open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.
- **Numpy**: An open-source Linear algebra library for the python language
## Contribution

Contributions to improve the course are welcome. If you have suggestions or corrections, please open an issue or a pull request with your changes.

---

Enjoy your journey through the elegant world of linear algebra!
