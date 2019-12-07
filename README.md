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
  * Code is clean and well commented. TA wants higher quality docstrings.
  * Working forward mode implementation
    * <s>Able to handle real functions of one or more variables, including multiple functions each of multiple variables</s>
    * Able to handle vector functions with multiple real scalar or vector inputs
    * <s>Available to download from GitHub.org</s>
    * Installable from PyPi - need to update when finished!
    * Requirements.txt file with dependencies - need to update when finished!
    * <s>Users should be "able to use without difficulty"</s>
    * Functions that must be implemented
      * <s>Addition (commutative)</s>
      * <s>Subtraction</s>
      * <s>Multiplication (commutative)</s>
      * <s>Division</s>
      * <s>Power</s>
      * <s>Negation</s>
      * \__lt\__ - optional
      * \__gt\__ - optional
      * \__le\__ - optional
      * \__ge\__ - optional
      * <s>\__eq\__</s>
      * <s>\__ne\__</s>
      * <s>Trig functions</s>
      * <s>Inverse trig functions</s>
      * <s>Exponentials - any base, treat natural base (e) as special case</s>
      * <s>Hyperbolic functions</s>
      * <s>Logistic funciton</s>
      * <s>Logarithms - any base</s>
      * <s>Square root</s>
  
  * Test suite
    * <s>Runs with pytest</s>
    * <s>Runs automatically on Travis CI</s>
    * <s>Contains badge showing pass/fail status of build.</s>
    * <s>Badge must show we are passing all tests</s>
    * <s>Connected to CodeCov</s>
    * <s>Badge reporting coverage of code</s>
    * Confirm NO TESTS fail
    * Cover > 90% - need to confirm when finished!
  
  
  * Updated/extended documentation
    * <s>Updated documentation will be the 'final' package documentation - mix of text and hand-on demos</s>
    * <s>Please name it documentation. Do not name it milestone3.</s>
    * Updated background/how to use sections with additional functionality
    * Sections:
      * <s>Intro - describe problem, why it's important to solve</s>
      * Background - including extensions
      * How to use
        * <s>How to install</s>
        * Basic demos for user - <s>one for auto diff,</s> one for new feature, etc.
      * Software org
        * Directory structure - update when finished
        * Modules and what they do
        * <s>Where do tests live? How are they run? How are they integrated?</s>
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
