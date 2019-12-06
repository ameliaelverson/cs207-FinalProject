# cs207-FinalProject

Group 32: Amelia Elverson, Aaron Jacobson, Erica Moreira, Lin Zhu

[![Build Status](https://travis-ci.com/ELAA207/cs207-FinalProject.svg?branch=master)](https://travis-ci.com/ELAA207/cs207-FinalProject.svg?branch=master)

[![Coverage Status](https://codecov.io/gh/ELAA207/cs207-FinalProject/branch/master/graph/badge.svg)](https://codecov.io/gh/ELAA207/cs207-FinalProject)

## Introduction
This repository contains an implementation of forward automatic differentiation.
Automatic differentiation breaks down the main function into elementary functions, evaluated upon one another. 
It then uses the chain rule to update the derivative at each step and ends in the derivative of the entire function.
Please click the link for more information:
[Overview and Installation Guide](docs/milestone2.ipynb)

# TO DO: Final due 12/10 at 12pm
1. Confirm directory structure: 
<pre><code>
cs207-FinalProject/
  README.md
  docs/  
    documentation
    milestone1
    milestone2
  autodiff32/
     ...
</code></pre>

2. Software Requirements
  * Working forward mode implementation
    * Able to handle real functions of one or more variables, including multiple functions each of multiple variables
    * Able to handle vector functions with multiple real scalar or vector inputs
    * Available to download from GitHub org
    * Installable from PyPi
    * Requirements.txt file with dependencies
    * Users should be "able to use without difficulty"
    * Functions that must be implemented
      * Addition (commutative)
      * Subtraction
      * Multiplication (commutative)
      * Division
      * Power
      * Negation
      * \__lt\__ - optional
      * \__gt\__ - optional
      * \__le\__ - optional
      * \__ge\__ - optional
      * \__eq\__
      * \__ne\__
      * Trig functions
      * Inverse trig functions
      * Exponentials - any base, treat natural base (e) as special case
      * Hyperbolic functions
      * Logistic funciton
      * Logarithms - any base
      * Square root
  
  * Test suite
    * Runs with pytest
    * Runs automatically on Travis CI
    * Contains badge showing pass/fail status of build.
    * Badge must show we are passing all tests
    * Connected to CodeCov
    * Badge reporting coverage of code
    * Cover > 90%
  
  
  * Updated/extended documentation
    * Updated documentation will be the 'final' package documentation - mix of text and hand-on demos
    * Please name it documentation. Do not name it milestone3.
    * Updated background/how to use sections with additional functionality
    * Sections:
      * Intro - describe problem, why it's important to solve
      * Background - including extensions
      * How to use
        * How to install
        * Basic demos for user - one for auto diff, one for new feature, etc.
      * Software org
        * Directory structure
        * Modules and what they do
        * Where do tests live? How are they run? How are they integrated?
        * How can someone install package? Should developers and consumers following different installation procedure?
      * Implementation details
        * Description of current implementation - deeper than software org
          * Such as: core data structures, core classes, important attributes, external dependencies, elementary functions, etc.
      * Extension
        * Description of extension
        * Additional information or background needed to understand - including mathematical or other concepts 
    
  * Extension
    * Build out extension
    * Full testing of extension
    * Document extension (including motivation and concepts behind it)

 * Video deliverable
  * Must be narrated by all members of group
  * Members must speak an equal amount
  * Change speakers exactly n-1 times (everyone should speak exactly once)
  * Time distribution:
    * Intro/background - 2 mins
      * min project only
      * Don't overdo the math details - provide big ideas behind auto diff and the motivation for using it
    * Implementation details/software organization/how to use - 4 mins
      * min project only
    * Additional features and extension - 5 mins
      * include any necessary background/impelmentation/how to use, etc. for extension here.
      * May need to present math background to get audience oriented
    * Future work/possible extensions - 2 mins
  * Maximum time: 15 mins
  * Do not include actual code snippets - teaching staff has access to code.
  * Upload to YouTube as private video - share video with course staff
    * Title must include group number
  * Fill out video submission Google Form
